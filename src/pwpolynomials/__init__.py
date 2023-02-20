import json
import urllib.request
from datetime import datetime, timedelta
from functools import partial
from types import SimpleNamespace

import numpy as np
from numpy.polynomial import Polynomial

import coefshifters
import leastsquares
import rvfinders

__version__ = "0.0.1"

__all__ = [
    "PiecewisePolynomial",
    "gen_test_pwpoly",
    "twopolyfit_iterative",
    "twopolyfit",
    "twopolyfit_given_knot",
    "AIC",
    "BIC",
    "find_knots",
    "multipolyfit",
    "fetch_binance"
]


class PiecewisePolynomial:
    floatfmt = '.4g'

    def __init__(self, coefs, knots=None):
        if knots is None:
            knots = []
        if len(coefs) != len(knots) + 1:
            raise ValueError("Incorrect number of knots in-between slopes")
        knots = np.asanyarray(knots)
        self.polynomials = [np.polynomial.Polynomial(coef)
                            for coef in coefs]
        self.knots = knots

    def __call__(self, x):
        if len(self.polynomials) == 1:
            return self.polynomials[0](x)
        condlist = [
            x <= self.knots[0],
            *((lo < x)&(x <= hi) for lo, hi in zip(self.knots[:-1], self.knots[1:])),
            x > self.knots[-1]
        ]
        return np.piecewise(x, condlist, self.polynomials)

    @classmethod
    def _poly_str(cls, poly):
        p = poly.degree()
        coef = poly.coef
        trans = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
        signch = {1: '+', -1: '-'}
        fmt = lambda f: format(f, cls.floatfmt)
        parts = [fmt(coef[0]), signch[np.sign(coef[1])], fmt(abs(coef[1])) + '·x']
        for i in range(2, p+1):
            parts.append(signch[np.sign(coef[i])])
            parts.append(fmt(abs(coef[i])) + '·x' + str(i).translate(trans))
        return ' '.join(parts)

    def __repr__(self):
        n_eqs = len(self.polynomials)
        floatfmt = self.floatfmt
        eqs = [self._poly_str(poly) for poly in self.polynomials]
        if n_eqs == 1:
            return eqs[0]
        elif n_eqs == 2:
            brakets = "⎰⎱"
        elif n_eqs % 2 == 1:
            extension = "⎪"*((n_eqs-3)//2)
            brakets = "⎧" + extension + "⎨" + extension + "⎩"
        else:
            extension = "⎪"*((n_eqs-4)//2)
            brakets = "⎧" + extension + "⎭⎫" + extension + "⎩"
        maxlen = max(len(eq) for eq in eqs)
        padded_eqs = [f"{eq},".ljust(maxlen + 1) for eq in eqs]
        lines = [
            f"{brakets[0]} {padded_eqs[0]} x ≤ {self.knots[0]:{floatfmt}},",
            *(
                f"{br} {eq} {lo:{floatfmt}} < x ≤ {hi:{floatfmt}}," 
                for br, eq, lo, hi in zip(brakets[1:-1],
                                          padded_eqs[1:-1],
                                          self.knots[:-1], 
                                          self.knots[1:])
            ),
            f"{brakets[-1]} {padded_eqs[-1]} x > {self.knots[-1]:{floatfmt}}."
        ]
        return '\n'.join(lines)


    def _repr_latex_(self):
        if len(self.polynomials) == 1:
            return self.polynomials[0]._repr_latex_().replace(r'x \mapsto ', '')
        eqs = [poly._repr_latex_()[11:-1] for poly in self.polynomials]
        return "".join([
            r"$\begin{cases} %s, & x \leq \text{%s},\\" % (eqs[0], self.knots[0]),
            *(
                r"%s, & \text{%s} < x \leq \text{%s},\\" % (eq, lo, hi)
                for eq, lo, hi in zip(eqs[1:-1], self.knots[:-1], self.knots[1:])
            ),
            r"%s, & x > \text{%s}. \end{cases}$" % (eqs[-1], self.knots[-1])
        ])


def gen_test_pwpoly(p1, p2, size=300, randseed=None, errscale=None):
    errscale = errscale if errscale is not None else max(p1, p2)
    rng = np.random.default_rng(randseed)
    x = np.linspace(-3, 3, num=size)
    error = rng.normal(scale=errscale, size=size)  # min +- 2*errscale
    a = rng.uniform(-0.3, 1, size=p1+1)
    b = rng.uniform(-0.1, 0.03, size=p2+1) 
    x0 = rng.uniform(-1, 1)
    b[0] = (sum([a[i]*x0**i for i in range(p1+1)]) 
            - sum([b[i]*x0**i for i in range(1, p2+1)]))
    pw_true = PiecewisePolynomial([a, b], [x0])
    y = pw_true(x) + error
    return x, y, pw_true


class PrecomputedSum:
  """
  Thin interface for sum of any subarray  

  Calculates cums of an array once and allows to get 
  sum of any subarray without recomputation

  Slices with step != 1 are not supported
  
  Examples
  --------
  >>> x = [1, 4, 6, 8, 15, 18, 21, 53, 72, 83, 95]
  >>> x_sum = PrecomputedSum(x)
  >>> k = 3
  >>> sum(x[:k]), x_sum[:k]
  (11, 11)
  >>> sum(x[k:]), x_sum[k:]
  (365, 365)
  >>> m = 8
  >>> sum(x[k:m]), x_sum[k:m]
  (115, 115)
  """
  __slots__ = ('sums',)

  def __init__(self, a, input_is_cumsum=False):
    if input_is_cumsum:
      self.sums = a
    else:
      self.sums = np.cumsum(a)
  
  def __getitem__(self, sl: slice):
    if sl.step not in (1, None):
      raise ValueError('Slices with step != 1 are not supported')
    loss = 0 if sl.start in (0, None) else self.sums[sl.start-1]
    stop = len(self.sums) if sl.stop is None else sl.stop
    head_sum = self.sums[min(stop, len(self.sums))-1]
    return head_sum - loss

  def subcopy(self, start=None, stop=None):
    loss = 0 if start in (0, None) else self.sums[start-1]
    return self.__class__(self.sums[start:stop] - loss, 
                          input_is_cumsum=True)
    

class PrecomputedPWPolySums(SimpleNamespace):
    def argsummatrix(self, p1=None, p2=None):
        p1, p2 = p1 or self.p1, p2 or self.p2
        n = len(self.x.sums)
        mat = np.empty((n, 3*p1 + 3*p2 + 4))
        x_cumsums = [self.x.sums, 
                     *(getattr(self, f'x{i+1}').sums for i in range(1, 2*max(p1, p2)))]
        for i in range(2*p1):
            mat[:, i] = x_cumsums[i]
        for i in range(2*p2):
            mat[:, 2*p1 + i] = x_cumsums[i][-1] - x_cumsums[i]
        mat[:, 2*p1 + 2*p2] = self.y.sums
        mat[:, 2*p1 + 2*p2 + 1] = self.y2.sums
        mat[:, 2*p1 + 2*p2 + 2] = self.y.sums[-1] - self.y.sums
        mat[:, 2*p1 + 2*p2 + 3] = self.y2.sums[-1] - self.y2.sums
        yx_cumsums = [self.yx.sums, 
                      *(getattr(self, f'yx{i+1}').sums for i in range(1, max(p1, p2)))]
        for i in range(p1):
            mat[:, 2*p1 + 2*p2 + 4 + i] = yx_cumsums[i]
        for i in range(p2):
            mat[:, 3*p1 + 2*p2 + 4 + i] = yx_cumsums[i][-1] - yx_cumsums[i]
        return mat

    def to_args(self, k, p1=None, p2=None):
        p1, p2 = p1 or self.p1, p2 or self.p2
        args = (
            self.x[:k],
            *(
                getattr(self, f'x{i}')[:k]
                for i in range(2, 2*p1 + 1)
            ),
            self.x[k:],
            *(
                getattr(self, f'x{i}')[k:]
                for i in range(2, 2*p2 + 1)
            ),
            self.y[:k],
            self.y2[:k],
            self.y[k:],
            self.y2[k:],
            self.yx[:k],
            *(
                getattr(self, f'yx{i}')[:k]
                for i in range(2, p1 + 1)
            ),
            self.yx[k:],
            *(
                getattr(self, f'yx{i}')[k:]
                for i in range(2, p2 + 1)
            )
        )
        return args

    def subcopy(self, start=None, stop=None):
        psums = PrecomputedPWPolySums(**{
            name: psum.subcopy(start, stop)
            for name, psum in vars(self).items()
            if name not in ['p1', 'p2']
        })
        psums.p1, psums.p2 = self.p1, self.p2
        return psums


def precompute_pwpoly_sums(x, y, p1, p2):
    psums = PrecomputedPWPolySums()
    psums.x = PrecomputedSum(x)
    for i in range(2, 2*max(p1, p2)+1):
        setattr(psums, f'x{i}', PrecomputedSum(x**i))
    psums.y = PrecomputedSum(y)
    psums.y2 = PrecomputedSum(y**2)
    psums.yx = PrecomputedSum(y*x)
    for i in range(2, max(p1, p2)+1):
        setattr(psums, f'yx{i}', PrecomputedSum(y*x**i))
    psums.p1, psums.p2 = p1, p2
    return psums


def _argsums(x, y, k, p1, p2):
    args = [np.sum(x[:k]**p) for p in range(1, 2*p1 + 1)]
    args.extend(np.sum(x[k:]**p) for p in range(1, 2*p2 + 1))
    args.extend([
        np.sum(y[:k]),
        np.sum(y[:k]**2),
        np.sum(y[k:]),
        np.sum(y[k:]**2)
    ])
    args.extend(np.sum(y[:k] * x[:k]**p) for p in range(1, p1 + 1))
    args.extend(np.sum(y[k:] * x[k:]**p) for p in range(1, p2 + 1))
    return args


def twopolyfit_iterative(x, y, p1, p2, pad=5, precomputed_sums=None):
    n = len(x)
    x = np.asanyarray(x)
    y = np.asanyarray(y)
    psums = precomputed_sums or precompute_pwpoly_sums(x, y, p1, p2)
    min_rv = np.inf
    best_coefs = None
    best_x0 = None
    argsummatrix = psums.argsummatrix(p1, p2)
    pw_lstsq = leastsquares.dispatcher[p1, p2]
    pw_rv = rvfinders.dispatcher[p1, p2]
    # rvs = []
    for k in range(pad + 1, n - pad):
        x0 = x[k-1]
        sums = argsummatrix[k-1]
        try:
            coefs = pw_lstsq(x0, k, n, *sums)
        except np.linalg.LinAlgError as e:
            print(e, f'k={k}, x0={x0:.4g}, n={n}')
            continue
        rv = pw_rv(x0, k, n, coefs[0], coefs[1], *sums)
        # rvs.append(rv)
        if rv < min_rv:
            best_coefs = coefs
            best_x0 = x0
            min_rv = rv
    return PiecewisePolynomial(best_coefs, [best_x0])#, rvs


def dichotomy(f, a, b, eps=1e-3, key=lambda x: x):
    x_min = a
    delta = eps / 10
    while b - a >= eps:
        alpha = (a + b - delta) / 2
        mu = (a + b + delta) / 2
        f_alpha = f(alpha)
        f_mu = f(mu)
        if key(f_alpha) <= key(f_mu):
            b = mu
            min_point = alpha, f_alpha
        else:
            a = alpha
            min_point = mu, f_mu
    return min_point


def twopolyfit(x, y, p1, p2, pad=5, precomputed_sums=None):
    n = len(x)
    x = np.asanyarray(x)
    y = np.asanyarray(y)
    psums = precomputed_sums or precompute_pwpoly_sums(x, y, p1, p2)
    a, b = x[pad + 1], x[-pad]
    pw_lstsq = leastsquares.dispatcher[p1, p2]    
    pw_rv = rvfinders.dispatcher[p1, p2]
    argsummatrix = psums.argsummatrix(p1, p2)
    def func_to_minimise(x0):
        k = np.searchsorted(x, x0)
        sums = argsummatrix[k-1]
        coefs = pw_lstsq(x0, k, n, *sums)
        rv = pw_rv(x0, k, n, coefs[0], coefs[1], *sums)
        return coefs, rv
    x0, (coefs, rv) = dichotomy(func_to_minimise, a, b, key=lambda res: res[1])
    return PiecewisePolynomial(coefs, [x0])


def twopolyfit_given_knot(x, y, x0_or_k, p1, p2, precomputed_sums=None, passed_k=False):
    if passed_k:
        k = x0_or_k
        x0 = x[k-1]
    else:
        x0 = x0_or_k
        k = np.searchsorted(x, x0)
    if precomputed_sums is None:
        sums = _argsums(x, y, k, p1, p2)
    else:
        sums = precompute_pwpoly_sums(x, y, p1, p2).to_args(k, p1, p2)
    coefs = leastsquares.dispatcher[p1, p2](x0, k, len(x), *sums)
    return PiecewisePolynomial(coefs, [x0])


def best_poly(x, y, p, scorer):
    n = len(x)
    powers = list(range(1, p + 1)) if isinstance(p, int) else p
    models = [
        (Polynomial.fit(x, y, i, window=x[[0, -1]]), i+1)
        for i in powers
    ]
    model_scores = [
        (m, scorer(s, n, np.sum((m(x) - y)**2)))
        for m, s in models
    ]
    return min(model_scores, key=lambda t: t[1])


def best_pwpoly(x, y, p, scorer, pad=5, precomputed_sums=None, k=None):
    n = len(x)
    powers = list(range(1, p + 1)) if isinstance(p, int) else p
    if k is None:
        fit = partial(twopolyfit_iterative, x, y, pad=pad, precomputed_sums=precomputed_sums)
    else:
        fit = partial(twopolyfit_given_knot, x, y, k, passed_k=True, 
                      precomputed_sums=precomputed_sums)
    models = [
        (fit(i, j), i+j+2)
        for i in powers
        for j in powers
    ]
    model_scores = [
        (m, scorer(s, n, np.sum((m(x) - y)**2)))
        for m, s in models
    ]
    return min(model_scores, key=lambda t: t[1])


def AIC(s, n, sse):
    return 2*s + n*(1+np.log(2*np.pi*sse/n))


def BIC(s, n, sse):
    return s*np.log(n) + n*(1+np.log(2*np.pi*sse/n))


def find_knots(x, y, p, scorer=BIC, min_slope=10):
    n = len(x)
    if n <= 2*min_slope + 1:
        return [best_poly(x, y, p, scorer)[0].degree()], []
    i_beg, i_end = 0, n
    m = [i_beg,]
    spline_powers = []
    suggested_p = p
    psums = precompute_pwpoly_sums(x, y, p, p)
    while True:
        sub_x = x[i_beg:i_end]
        sub_y = y[i_beg:i_end]
        sub_psums = psums.subcopy(i_beg, i_end)
        poly, poly_score = best_poly(sub_x, sub_y, suggested_p, scorer)
        degree = poly.degree()
        pwpoly, pwpoly_score = best_pwpoly(sub_x, sub_y, p, scorer, 
                                            min_slope, sub_psums)
        if pwpoly_score < poly_score:
            k = np.searchsorted(x, pwpoly.knots[0])
            if k - i_beg <= 2*min_slope + 1:
                m.append(k)
                spline_powers.append(pwpoly.polynomials[0].degree())
                degree = pwpoly.polynomials[1].degree()
            else:
                suggested_p = [pwpoly.polynomials[0].degree()]
                i_end = k
                continue
        suggested_p = p
        spline_powers.append(degree)
        m.append(i_end)
        if len(m) > 2:
            x_test = x[m[-3] : m[-1]+1]
            y_test = y[m[-3] : m[-1]+1]
            test_psums = psums.subcopy(m[-3], m[-1]+1)
            k = m[-2] - m[-3]
            poly, poly_score = best_poly(x_test, y_test, p, scorer)
            pwpoly, pwpoly_score = best_pwpoly(x_test, y_test, p, scorer, 
                                               min_slope, test_psums, k)
            if poly_score < pwpoly_score:
                del m[-2]
                spline_powers.pop()
                spline_powers[-1] = poly.degree()
        if i_end == n:
            break
        i_beg = i_end
        i_end = n
        if i_end - i_beg <= min_slope:
            break
        if i_end - i_beg <= 2*min_slope + 1:
            poly, _ = best_poly(x[i_beg:i_end], y[i_beg:i_end], p, scorer)
            spline_powers.append(poly.degree())
            m.append(i_end)
            break
    # end while True
    return m, spline_powers


def multipolyfit(x, y, p, scorer=BIC, min_slope=10, connect=True):
    x = np.asanyarray(x)
    y = np.asanyarray(y)
    m, spline_powers = find_knots(x, y, p, scorer, min_slope)
    if connect:
        n_slines = len(m)-1
        x_spline_0 = x[: m[1]]
        y_spline_0 = y[: m[1]]
        D0 = x_spline_0 - x[0]
        poly = Polynomial.fit(D0, y_spline_0, spline_powers[0], window=D0[[0, -1]])
        shifted_coefs = [poly.coef]
        for i in range(1, n_slines):
            x_spline_i = x[m[i]+1 : m[i+1]]
            y_spline_i = y[m[i]+1 : m[i+1]]
            spline_p = spline_powers[i]
            Dx = x[m[i]] - x[m[i-1]]
            coef = np.empty(spline_p + 1)
            coef[0] = sum(c*Dx**j for j, c in enumerate(shifted_coefs[i-1]))
            D = x_spline_i - x[m[i]]
            if spline_p == 1:
                coef[1] = np.sum(D * (y_spline_i- coef[0])) / np.sum(D**2)
            else:
                D_sums = [*(np.sum(D**j) for j in range(2, 2*spline_p + 1))]
                divisor = m[i+1] - m[i]
                T = np.array([
                    [D_sums[i_ + j_] / divisor for j_ in range(spline_p)]
                    for i_ in range(spline_p)
                ])
                R = np.array([
                    np.sum(D**j * (y_spline_i - coef[0])) / divisor
                    for j in range(1, spline_p+1)
                ])
                coef[1:] = np.linalg.solve(T, R)
            #end else
            shifted_coefs.append(coef)
        #end for i in range(1, n_slines)
        coefs = [
            coefshifters.dispatcher[len(coef)-1](coef, x[m[i]])
            for i, coef in enumerate(shifted_coefs)
        ]
    else:
        coefs = [
            Polynomial.fit(x[m[i] : m[i+1]], 
                        y[m[i] : m[i+1]], 
                        spline_powers[i], 
                        window=x[[m[i], m[i+1]-1]]).coef
            for i in range(len(m)-1)
        ]
    del m[-1]
    del m[0]
    return PiecewisePolynomial(coefs, x[m])


def fetch_binance(start=None, end=None, 
                  pair='BTCUSDT', interval='15m',
                  limit=1000, return_arguments=False):
    end = end or datetime.now()
    start = start or end - timedelta(days=1)
    end_ms = int(end.timestamp() * 1000)
    start_ms = int(start.timestamp() * 1000)
    pair = pair.upper()
    baseurl = 'https://www.binance.com/api/v3/klines?'
    query = 'symbol=%s&interval=%s&startTime=%s&endTime=%s&limit=%s'
    url = baseurl + query %  (pair, interval, start_ms, end_ms, limit)
    with urllib.request.urlopen(url) as resp:
        data = json.load(resp)
    closetimes = [datetime.fromtimestamp(row[6]/1000) for row in data]
    prices = np.array([float(row[4]) for row in data])
    if return_arguments:
        args = {
            'start': start, 
            'end': end, 
            'pair': pair, 
            'interval': interval, 
            'limit': limit
        }
        return closetimes, prices, args
    return closetimes, prices
    