import re
from functools import lru_cache

import sympy as sp


@lru_cache
def _expr_substitutesum_productlen_tuples(p1, p2):
    x, X, y, Y = sp.symbols('x, X, y, Y')
    res = (
        (x, 'sumh_x', 1),
        *(
            (x**i, f'sumh_x{i}', i)
            for i in range(2, 2*p1 + 1)
        ),
        (X, 'sumt_x', 1),
        *(
            (X**i, f'sumt_x{i}', i)
            for i in range(2, 2*p2 + 1)
        ),
        (y, 'sumh_y', 1),
        (y*y, 'sumh_y2', 2),
        (Y, 'sumt_y', 1),
        (Y*Y, 'sumt_y2', 2),
        (y*x, 'sumh_yx', 2),
        *(
            (y*x**i, f'sumh_yx{i}', i+1)
            for i in range(2, p1 + 1)
        ),
        (Y*X, 'sumt_yx', 2),
        *(
            (Y*X**i, f'sumt_yx{i}', i+1)
            for i in range(2, p2 + 1)
        )
    )
    return res

@lru_cache
def compile_pw_rv_func(p1, p2):
    y = sp.S('y')
    x = sp.S('x')
    Y = sp.S('Y')
    X = sp.S('X')
    x0 = sp.S('x0')
    a = [sp.S(f'a{j}') for j in range(p1+1)]
    b = [sp.S(f'b{j}') for j in range(p2+1)]
    k = sp.S('k')
    n = sp.S('n')
    expr1 = (y - sum(a[j] * x**j for j in range(p1+1)))**2
    expr2 = (Y - sum(a[j] * x0**j for j in range(p1+1))
               - sum(b[j] * (X**j - x0**j) for j in range(1, p2+1)))**2
    expanded1 = sp.expand(expr1)
    non_sums1 = expanded1.subs({x: 0, y: 0, X: 0, Y: 0})
    part1 = expanded1.subs(non_sums1, k*non_sums1)
    expanded2 = sp.expand(expr2)
    non_sums2 = expanded2.subs({x: 0, y: 0, X: 0, Y: 0})
    part2 = expanded2.subs(non_sums2, (n-k)*non_sums2)

    all = 1/(n-p1-p2-2)*(part1 + part2)
    esp_tuples = _expr_substitutesum_productlen_tuples(p1, p2)
    args = ['x0', 'k', 'n', 'a', 'b']
    args.extend(sumname for _, sumname, _ in esp_tuples)
    esp_tuples = sorted(esp_tuples, key=lambda t: t[2], reverse=True)
    to_sub = [(expr, subsum) for expr, subsum, _ in esp_tuples]
    body = re.sub(r'(a|b)(\d+)', r'\1[\2]', repr(all.subs(to_sub)))
    source = f"""def pw_rv_{p1}_{p2}({', '.join(args)}):
                     return {body}"""
    temp_locals = {}
    temp_globals = {**globals(), 'p1': p1, 'p2': p2}
    code = compile(source, __file__, 'exec')
    exec(code, temp_globals, temp_locals)
    func = temp_locals[f'pw_rv_{p1}_{p2}']
    return func


@lru_cache
def compile_pw_coefs_func(p1, p2):
    x = sp.S('x')
    X = sp.S('X')
    y = sp.S('y')
    Y = sp.S('Y')
    x0 = sp.S('x0')
    k = sp.S('k')
    n = sp.S('n')

    T = [[0]*(p1+p2+1) for _ in range(p1+p2+1)]
    for i in range(p1+1):
        for j in range(p1+1):
            T[i][j] = x**(i+j) + (n-k)*x0**(i+j)
    T[0][0] = n
    for i in range(p1+1):
        for j in range(1, p2+1):
            T[i][j+p1] = x0**i * (X**j - (n-k)*x0**j)
    for i in range(1, p2+1):
        for j in range(p1+1):
            T[i+p1][j] = x0**j * (X**i - (n-k)*x0**i)
    for i in range(1, p2+1):
        for j in range(1, p2+1):
            T[i+p1][j+p1] = X**(i+j) - (X**i * x0**j) - (X**j * x0**i) + (n-k)*x0**(i+j)

    R = ([y*x**i + Y*x0**i for i in range(p1+1)] 
        + [Y*X**i - Y*x0**i for i in range(1, p2+1)])

    esp_tuples = _expr_substitutesum_productlen_tuples(p1, p2)
    args = ['x0', 'k', 'n']
    args.extend(sumname for _, sumname, _ in esp_tuples)
    esp_tuples = sorted(esp_tuples, key=lambda t: t[2], reverse=True)
    to_sub = [(expr, subsum) for expr, subsum, _ in esp_tuples]
    T = [[formula.subs(to_sub) for formula in row] for row in T]
    R = [formula.subs(to_sub) for formula in R]
    a_part = ' + '.join(f'a[{i}]*x0**{i}' for i in range(p1+1))
    b_part = ' + '.join(f'b[{i}]*x0**{i}' for i in range(1, p2+1))
    source = f"""def coefs_{p1}_{p2}({', '.join(args)}):
                     x0 = float(x0)
                     T = np.array({T}, dtype=np.float64)
                     R = np.array({R}, dtype=np.float64)
                     coefs = np.linalg.solve(T, R)
                     a = coefs[:{p1+1}]
                     b = np.concatenate((np.array([-0.0]), coefs[{p1+1}:]))
                     b[0] = ({a_part}) - ({b_part})
                     return a, b"""
    temp_locals = {}
    temp_globals = {**globals()}
    code = compile(source, __file__, 'exec')
    exec(code, temp_globals, temp_locals)
    func = temp_locals[f'coefs_{p1}_{p2}']
    return func


@lru_cache
def coef_translator(p):
    x = sp.S('x')
    x_m = sp.S('x_m')
    a = [sp.S(f'a{j}') for j in range(p+1)]
    expr = sum(a[i] * (x - x_m)**i for i in range(p+1))
    expr = sp.expand(expr)
    consts = expr.subs(x, 0)
    coef = [
        consts,
        *(
            (expr - consts).subs([(sp.S('x')**j, int(i == j)) 
                                  for j in range(p, 0, -1)])
            for i in range(1, p+1)
        )
        
    ]
    body = re.sub(r'a(\d+)', r'a[\1]', repr(coef))
    source = f"""def coef_translate_{p}(a, x_m):
                     return {body}"""
    temp_locals = {}
    code = compile(source, __file__, 'exec')
    exec(code, None, temp_locals)
    func = temp_locals[f'coef_translate_{p}']
    return func