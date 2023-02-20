def rv_1_1(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumt_x,
    sumt_x2,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumt_yx,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * b[1] * sumt_x
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * b[1] * sumt_x * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            - 2 * a[0] * b[1] * x0
            + a[1] ** 2 * x0**2
            - 2 * a[1] * b[1] * x0**2
            + b[1] ** 2 * x0**2
        )
    ) / (n - 4)


def rv_1_2(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumt_yx,
    sumt_yx2,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            + a[1] ** 2 * x0**2
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + b[2] ** 2 * x0**4
        )
    ) / (n - 5)


def rv_1_3(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            + a[1] ** 2 * x0**2
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + b[3] ** 2 * x0**6
        )
    ) / (n - 6)


def rv_1_4(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            + a[1] ** 2 * x0**2
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + b[4] ** 2 * x0**8
        )
    ) / (n - 7)


def rv_1_5(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            + a[1] ** 2 * x0**2
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + b[5] ** 2 * x0**10
        )
    ) / (n - 8)


def rv_1_6(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            + a[1] ** 2 * x0**2
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + b[6] ** 2 * x0**12
        )
    ) / (n - 9)


def rv_1_7(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumt_x13,
    sumt_x14,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
    sumt_yx7,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        + 2 * a[0] * b[7] * sumt_x7
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        + 2 * a[1] * b[7] * sumt_x7 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        - 2 * b[1] * b[7] * sumt_x * x0**7
        - 2 * b[1] * b[7] * sumt_x7 * x0
        + 2 * b[1] * b[7] * sumt_x8
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        - 2 * b[2] * b[7] * sumt_x2 * x0**7
        - 2 * b[2] * b[7] * sumt_x7 * x0**2
        + 2 * b[2] * b[7] * sumt_x9
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * b[7] * sumt_x10
        - 2 * b[3] * b[7] * sumt_x3 * x0**7
        - 2 * b[3] * b[7] * sumt_x7 * x0**3
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * b[7] * sumt_x11
        - 2 * b[4] * b[7] * sumt_x4 * x0**7
        - 2 * b[4] * b[7] * sumt_x7 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * b[7] * sumt_x12
        - 2 * b[5] * b[7] * sumt_x5 * x0**7
        - 2 * b[5] * b[7] * sumt_x7 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * b[7] * sumt_x13
        - 2 * b[6] * b[7] * sumt_x6 * x0**7
        - 2 * b[6] * b[7] * sumt_x7 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + b[7] ** 2 * sumt_x14
        - 2 * b[7] ** 2 * sumt_x7 * x0**7
        + 2 * b[7] * sumt_y * x0**7
        - 2 * b[7] * sumt_yx7
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            - 2 * a[0] * b[7] * x0**7
            + a[1] ** 2 * x0**2
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            - 2 * a[1] * b[7] * x0**8
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + 2 * b[1] * b[7] * x0**8
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + 2 * b[2] * b[7] * x0**9
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + 2 * b[3] * b[7] * x0**10
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + 2 * b[4] * b[7] * x0**11
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + 2 * b[5] * b[7] * x0**12
            + b[6] ** 2 * x0**12
            + 2 * b[6] * b[7] * x0**13
            + b[7] ** 2 * x0**14
        )
    ) / (n - 10)


def rv_2_1(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumt_x,
    sumt_x2,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumt_yx,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * b[1] * sumt_x
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * b[1] * sumt_x * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * b[1] * sumt_x * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            - 2 * a[0] * b[1] * x0
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            - 2 * a[1] * b[1] * x0**2
            + a[2] ** 2 * x0**4
            - 2 * a[2] * b[1] * x0**3
            + b[1] ** 2 * x0**2
        )
    ) / (n - 5)


def rv_2_2(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumt_yx,
    sumt_yx2,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            + a[2] ** 2 * x0**4
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + b[2] ** 2 * x0**4
        )
    ) / (n - 6)


def rv_2_3(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            + a[2] ** 2 * x0**4
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + b[3] ** 2 * x0**6
        )
    ) / (n - 7)


def rv_2_4(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            + a[2] ** 2 * x0**4
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + b[4] ** 2 * x0**8
        )
    ) / (n - 8)


def rv_2_5(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            + a[2] ** 2 * x0**4
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + b[5] ** 2 * x0**10
        )
    ) / (n - 9)


def rv_2_6(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            + a[2] ** 2 * x0**4
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + b[6] ** 2 * x0**12
        )
    ) / (n - 10)


def rv_2_7(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumt_x13,
    sumt_x14,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
    sumt_yx7,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        + 2 * a[0] * b[7] * sumt_x7
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        + 2 * a[1] * b[7] * sumt_x7 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        + 2 * a[2] * b[7] * sumt_x7 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        - 2 * b[1] * b[7] * sumt_x * x0**7
        - 2 * b[1] * b[7] * sumt_x7 * x0
        + 2 * b[1] * b[7] * sumt_x8
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        - 2 * b[2] * b[7] * sumt_x2 * x0**7
        - 2 * b[2] * b[7] * sumt_x7 * x0**2
        + 2 * b[2] * b[7] * sumt_x9
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * b[7] * sumt_x10
        - 2 * b[3] * b[7] * sumt_x3 * x0**7
        - 2 * b[3] * b[7] * sumt_x7 * x0**3
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * b[7] * sumt_x11
        - 2 * b[4] * b[7] * sumt_x4 * x0**7
        - 2 * b[4] * b[7] * sumt_x7 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * b[7] * sumt_x12
        - 2 * b[5] * b[7] * sumt_x5 * x0**7
        - 2 * b[5] * b[7] * sumt_x7 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * b[7] * sumt_x13
        - 2 * b[6] * b[7] * sumt_x6 * x0**7
        - 2 * b[6] * b[7] * sumt_x7 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + b[7] ** 2 * sumt_x14
        - 2 * b[7] ** 2 * sumt_x7 * x0**7
        + 2 * b[7] * sumt_y * x0**7
        - 2 * b[7] * sumt_yx7
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            - 2 * a[0] * b[7] * x0**7
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            - 2 * a[1] * b[7] * x0**8
            + a[2] ** 2 * x0**4
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            - 2 * a[2] * b[7] * x0**9
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + 2 * b[1] * b[7] * x0**8
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + 2 * b[2] * b[7] * x0**9
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + 2 * b[3] * b[7] * x0**10
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + 2 * b[4] * b[7] * x0**11
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + 2 * b[5] * b[7] * x0**12
            + b[6] ** 2 * x0**12
            + 2 * b[6] * b[7] * x0**13
            + b[7] ** 2 * x0**14
        )
    ) / (n - 11)


def rv_3_1(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumt_x,
    sumt_x2,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumt_yx,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * b[1] * sumt_x
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * b[1] * sumt_x * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * b[1] * sumt_x * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * b[1] * sumt_x * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            - 2 * a[0] * b[1] * x0
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            - 2 * a[1] * b[1] * x0**2
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            - 2 * a[2] * b[1] * x0**3
            + a[3] ** 2 * x0**6
            - 2 * a[3] * b[1] * x0**4
            + b[1] ** 2 * x0**2
        )
    ) / (n - 6)


def rv_3_2(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumt_yx,
    sumt_yx2,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            + a[3] ** 2 * x0**6
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + b[2] ** 2 * x0**4
        )
    ) / (n - 7)


def rv_3_3(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            + a[3] ** 2 * x0**6
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + b[3] ** 2 * x0**6
        )
    ) / (n - 8)


def rv_3_4(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            + a[3] ** 2 * x0**6
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + b[4] ** 2 * x0**8
        )
    ) / (n - 9)


def rv_3_5(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            + a[3] ** 2 * x0**6
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + b[5] ** 2 * x0**10
        )
    ) / (n - 10)


def rv_3_6(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            + a[3] ** 2 * x0**6
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + b[6] ** 2 * x0**12
        )
    ) / (n - 11)


def rv_3_7(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumt_x13,
    sumt_x14,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
    sumt_yx7,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        + 2 * a[0] * b[7] * sumt_x7
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        + 2 * a[1] * b[7] * sumt_x7 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        + 2 * a[2] * b[7] * sumt_x7 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        + 2 * a[3] * b[7] * sumt_x7 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        - 2 * b[1] * b[7] * sumt_x * x0**7
        - 2 * b[1] * b[7] * sumt_x7 * x0
        + 2 * b[1] * b[7] * sumt_x8
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        - 2 * b[2] * b[7] * sumt_x2 * x0**7
        - 2 * b[2] * b[7] * sumt_x7 * x0**2
        + 2 * b[2] * b[7] * sumt_x9
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * b[7] * sumt_x10
        - 2 * b[3] * b[7] * sumt_x3 * x0**7
        - 2 * b[3] * b[7] * sumt_x7 * x0**3
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * b[7] * sumt_x11
        - 2 * b[4] * b[7] * sumt_x4 * x0**7
        - 2 * b[4] * b[7] * sumt_x7 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * b[7] * sumt_x12
        - 2 * b[5] * b[7] * sumt_x5 * x0**7
        - 2 * b[5] * b[7] * sumt_x7 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * b[7] * sumt_x13
        - 2 * b[6] * b[7] * sumt_x6 * x0**7
        - 2 * b[6] * b[7] * sumt_x7 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + b[7] ** 2 * sumt_x14
        - 2 * b[7] ** 2 * sumt_x7 * x0**7
        + 2 * b[7] * sumt_y * x0**7
        - 2 * b[7] * sumt_yx7
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            - 2 * a[0] * b[7] * x0**7
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            - 2 * a[1] * b[7] * x0**8
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            - 2 * a[2] * b[7] * x0**9
            + a[3] ** 2 * x0**6
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            - 2 * a[3] * b[7] * x0**10
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + 2 * b[1] * b[7] * x0**8
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + 2 * b[2] * b[7] * x0**9
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + 2 * b[3] * b[7] * x0**10
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + 2 * b[4] * b[7] * x0**11
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + 2 * b[5] * b[7] * x0**12
            + b[6] ** 2 * x0**12
            + 2 * b[6] * b[7] * x0**13
            + b[7] ** 2 * x0**14
        )
    ) / (n - 12)


def rv_4_1(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumt_x,
    sumt_x2,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumt_yx,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * b[1] * sumt_x
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * b[1] * sumt_x * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * b[1] * sumt_x * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * b[1] * sumt_x * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * b[1] * sumt_x * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            - 2 * a[0] * b[1] * x0
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            - 2 * a[1] * b[1] * x0**2
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            - 2 * a[2] * b[1] * x0**3
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            - 2 * a[3] * b[1] * x0**4
            + a[4] ** 2 * x0**8
            - 2 * a[4] * b[1] * x0**5
            + b[1] ** 2 * x0**2
        )
    ) / (n - 7)


def rv_4_2(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumt_yx,
    sumt_yx2,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            + a[4] ** 2 * x0**8
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + b[2] ** 2 * x0**4
        )
    ) / (n - 8)


def rv_4_3(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            + a[4] ** 2 * x0**8
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + b[3] ** 2 * x0**6
        )
    ) / (n - 9)


def rv_4_4(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            + a[4] ** 2 * x0**8
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + b[4] ** 2 * x0**8
        )
    ) / (n - 10)


def rv_4_5(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            + a[4] ** 2 * x0**8
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + b[5] ** 2 * x0**10
        )
    ) / (n - 11)


def rv_4_6(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        + 2 * a[4] * b[6] * sumt_x6 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            + a[4] ** 2 * x0**8
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            - 2 * a[4] * b[6] * x0**10
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + b[6] ** 2 * x0**12
        )
    ) / (n - 12)


def rv_4_7(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumt_x13,
    sumt_x14,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
    sumt_yx7,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        + 2 * a[0] * b[7] * sumt_x7
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        + 2 * a[1] * b[7] * sumt_x7 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        + 2 * a[2] * b[7] * sumt_x7 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        + 2 * a[3] * b[7] * sumt_x7 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        + 2 * a[4] * b[6] * sumt_x6 * x0**4
        + 2 * a[4] * b[7] * sumt_x7 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        - 2 * b[1] * b[7] * sumt_x * x0**7
        - 2 * b[1] * b[7] * sumt_x7 * x0
        + 2 * b[1] * b[7] * sumt_x8
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        - 2 * b[2] * b[7] * sumt_x2 * x0**7
        - 2 * b[2] * b[7] * sumt_x7 * x0**2
        + 2 * b[2] * b[7] * sumt_x9
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * b[7] * sumt_x10
        - 2 * b[3] * b[7] * sumt_x3 * x0**7
        - 2 * b[3] * b[7] * sumt_x7 * x0**3
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * b[7] * sumt_x11
        - 2 * b[4] * b[7] * sumt_x4 * x0**7
        - 2 * b[4] * b[7] * sumt_x7 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * b[7] * sumt_x12
        - 2 * b[5] * b[7] * sumt_x5 * x0**7
        - 2 * b[5] * b[7] * sumt_x7 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * b[7] * sumt_x13
        - 2 * b[6] * b[7] * sumt_x6 * x0**7
        - 2 * b[6] * b[7] * sumt_x7 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + b[7] ** 2 * sumt_x14
        - 2 * b[7] ** 2 * sumt_x7 * x0**7
        + 2 * b[7] * sumt_y * x0**7
        - 2 * b[7] * sumt_yx7
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            - 2 * a[0] * b[7] * x0**7
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            - 2 * a[1] * b[7] * x0**8
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            - 2 * a[2] * b[7] * x0**9
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            - 2 * a[3] * b[7] * x0**10
            + a[4] ** 2 * x0**8
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            - 2 * a[4] * b[6] * x0**10
            - 2 * a[4] * b[7] * x0**11
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + 2 * b[1] * b[7] * x0**8
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + 2 * b[2] * b[7] * x0**9
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + 2 * b[3] * b[7] * x0**10
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + 2 * b[4] * b[7] * x0**11
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + 2 * b[5] * b[7] * x0**12
            + b[6] ** 2 * x0**12
            + 2 * b[6] * b[7] * x0**13
            + b[7] ** 2 * x0**14
        )
    ) / (n - 13)


def rv_5_1(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumt_x,
    sumt_x2,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumt_yx,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * b[1] * sumt_x
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * b[1] * sumt_x * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * b[1] * sumt_x * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * b[1] * sumt_x * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * b[1] * sumt_x * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * b[1] * sumt_x * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            - 2 * a[0] * b[1] * x0
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            - 2 * a[1] * b[1] * x0**2
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            - 2 * a[2] * b[1] * x0**3
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            - 2 * a[3] * b[1] * x0**4
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            - 2 * a[4] * b[1] * x0**5
            + a[5] ** 2 * x0**10
            - 2 * a[5] * b[1] * x0**6
            + b[1] ** 2 * x0**2
        )
    ) / (n - 8)


def rv_5_2(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumt_yx,
    sumt_yx2,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            + a[5] ** 2 * x0**10
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + b[2] ** 2 * x0**4
        )
    ) / (n - 9)


def rv_5_3(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            + a[5] ** 2 * x0**10
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + b[3] ** 2 * x0**6
        )
    ) / (n - 10)


def rv_5_4(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            + a[5] ** 2 * x0**10
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + b[4] ** 2 * x0**8
        )
    ) / (n - 11)


def rv_5_5(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        + 2 * a[5] * b[5] * sumt_x5 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            + a[5] ** 2 * x0**10
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            - 2 * a[5] * b[5] * x0**10
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + b[5] ** 2 * x0**10
        )
    ) / (n - 12)


def rv_5_6(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        + 2 * a[4] * b[6] * sumt_x6 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        + 2 * a[5] * b[5] * sumt_x5 * x0**5
        + 2 * a[5] * b[6] * sumt_x6 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            - 2 * a[4] * b[6] * x0**10
            + a[5] ** 2 * x0**10
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            - 2 * a[5] * b[5] * x0**10
            - 2 * a[5] * b[6] * x0**11
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + b[6] ** 2 * x0**12
        )
    ) / (n - 13)


def rv_5_7(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumt_x13,
    sumt_x14,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
    sumt_yx7,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        + 2 * a[0] * b[7] * sumt_x7
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        + 2 * a[1] * b[7] * sumt_x7 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        + 2 * a[2] * b[7] * sumt_x7 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        + 2 * a[3] * b[7] * sumt_x7 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        + 2 * a[4] * b[6] * sumt_x6 * x0**4
        + 2 * a[4] * b[7] * sumt_x7 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        + 2 * a[5] * b[5] * sumt_x5 * x0**5
        + 2 * a[5] * b[6] * sumt_x6 * x0**5
        + 2 * a[5] * b[7] * sumt_x7 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        - 2 * b[1] * b[7] * sumt_x * x0**7
        - 2 * b[1] * b[7] * sumt_x7 * x0
        + 2 * b[1] * b[7] * sumt_x8
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        - 2 * b[2] * b[7] * sumt_x2 * x0**7
        - 2 * b[2] * b[7] * sumt_x7 * x0**2
        + 2 * b[2] * b[7] * sumt_x9
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * b[7] * sumt_x10
        - 2 * b[3] * b[7] * sumt_x3 * x0**7
        - 2 * b[3] * b[7] * sumt_x7 * x0**3
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * b[7] * sumt_x11
        - 2 * b[4] * b[7] * sumt_x4 * x0**7
        - 2 * b[4] * b[7] * sumt_x7 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * b[7] * sumt_x12
        - 2 * b[5] * b[7] * sumt_x5 * x0**7
        - 2 * b[5] * b[7] * sumt_x7 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * b[7] * sumt_x13
        - 2 * b[6] * b[7] * sumt_x6 * x0**7
        - 2 * b[6] * b[7] * sumt_x7 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + b[7] ** 2 * sumt_x14
        - 2 * b[7] ** 2 * sumt_x7 * x0**7
        + 2 * b[7] * sumt_y * x0**7
        - 2 * b[7] * sumt_yx7
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            - 2 * a[0] * b[7] * x0**7
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            - 2 * a[1] * b[7] * x0**8
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            - 2 * a[2] * b[7] * x0**9
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            - 2 * a[3] * b[7] * x0**10
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            - 2 * a[4] * b[6] * x0**10
            - 2 * a[4] * b[7] * x0**11
            + a[5] ** 2 * x0**10
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            - 2 * a[5] * b[5] * x0**10
            - 2 * a[5] * b[6] * x0**11
            - 2 * a[5] * b[7] * x0**12
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + 2 * b[1] * b[7] * x0**8
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + 2 * b[2] * b[7] * x0**9
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + 2 * b[3] * b[7] * x0**10
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + 2 * b[4] * b[7] * x0**11
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + 2 * b[5] * b[7] * x0**12
            + b[6] ** 2 * x0**12
            + 2 * b[6] * b[7] * x0**13
            + b[7] ** 2 * x0**14
        )
    ) / (n - 14)


def rv_6_1(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumt_x,
    sumt_x2,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumt_yx,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * b[1] * sumt_x
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * b[1] * sumt_x * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * b[1] * sumt_x * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * b[1] * sumt_x * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * b[1] * sumt_x * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * b[1] * sumt_x * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * b[1] * sumt_x * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            - 2 * a[0] * b[1] * x0
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            - 2 * a[1] * b[1] * x0**2
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            - 2 * a[2] * b[1] * x0**3
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            - 2 * a[3] * b[1] * x0**4
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            - 2 * a[4] * b[1] * x0**5
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            - 2 * a[5] * b[1] * x0**6
            + a[6] ** 2 * x0**12
            - 2 * a[6] * b[1] * x0**7
            + b[1] ** 2 * x0**2
        )
    ) / (n - 9)


def rv_6_2(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumt_yx,
    sumt_yx2,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            + a[6] ** 2 * x0**12
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + b[2] ** 2 * x0**4
        )
    ) / (n - 10)


def rv_6_3(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            + a[6] ** 2 * x0**12
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + b[3] ** 2 * x0**6
        )
    ) / (n - 11)


def rv_6_4(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        + 2 * a[6] * b[4] * sumt_x4 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            + a[6] ** 2 * x0**12
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            - 2 * a[6] * b[4] * x0**10
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + b[4] ** 2 * x0**8
        )
    ) / (n - 12)


def rv_6_5(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        + 2 * a[5] * b[5] * sumt_x5 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        + 2 * a[6] * b[4] * sumt_x4 * x0**6
        + 2 * a[6] * b[5] * sumt_x5 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            - 2 * a[5] * b[5] * x0**10
            + a[6] ** 2 * x0**12
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            - 2 * a[6] * b[4] * x0**10
            - 2 * a[6] * b[5] * x0**11
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + b[5] ** 2 * x0**10
        )
    ) / (n - 13)


def rv_6_6(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        + 2 * a[4] * b[6] * sumt_x6 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        + 2 * a[5] * b[5] * sumt_x5 * x0**5
        + 2 * a[5] * b[6] * sumt_x6 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        + 2 * a[6] * b[4] * sumt_x4 * x0**6
        + 2 * a[6] * b[5] * sumt_x5 * x0**6
        + 2 * a[6] * b[6] * sumt_x6 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            - 2 * a[4] * b[6] * x0**10
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            - 2 * a[5] * b[5] * x0**10
            - 2 * a[5] * b[6] * x0**11
            + a[6] ** 2 * x0**12
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            - 2 * a[6] * b[4] * x0**10
            - 2 * a[6] * b[5] * x0**11
            - 2 * a[6] * b[6] * x0**12
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + b[6] ** 2 * x0**12
        )
    ) / (n - 14)


def rv_6_7(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumt_x13,
    sumt_x14,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
    sumt_yx7,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        + 2 * a[0] * b[7] * sumt_x7
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        + 2 * a[1] * b[7] * sumt_x7 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        + 2 * a[2] * b[7] * sumt_x7 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        + 2 * a[3] * b[7] * sumt_x7 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        + 2 * a[4] * b[6] * sumt_x6 * x0**4
        + 2 * a[4] * b[7] * sumt_x7 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        + 2 * a[5] * b[5] * sumt_x5 * x0**5
        + 2 * a[5] * b[6] * sumt_x6 * x0**5
        + 2 * a[5] * b[7] * sumt_x7 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        + 2 * a[6] * b[4] * sumt_x4 * x0**6
        + 2 * a[6] * b[5] * sumt_x5 * x0**6
        + 2 * a[6] * b[6] * sumt_x6 * x0**6
        + 2 * a[6] * b[7] * sumt_x7 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        - 2 * b[1] * b[7] * sumt_x * x0**7
        - 2 * b[1] * b[7] * sumt_x7 * x0
        + 2 * b[1] * b[7] * sumt_x8
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        - 2 * b[2] * b[7] * sumt_x2 * x0**7
        - 2 * b[2] * b[7] * sumt_x7 * x0**2
        + 2 * b[2] * b[7] * sumt_x9
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * b[7] * sumt_x10
        - 2 * b[3] * b[7] * sumt_x3 * x0**7
        - 2 * b[3] * b[7] * sumt_x7 * x0**3
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * b[7] * sumt_x11
        - 2 * b[4] * b[7] * sumt_x4 * x0**7
        - 2 * b[4] * b[7] * sumt_x7 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * b[7] * sumt_x12
        - 2 * b[5] * b[7] * sumt_x5 * x0**7
        - 2 * b[5] * b[7] * sumt_x7 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * b[7] * sumt_x13
        - 2 * b[6] * b[7] * sumt_x6 * x0**7
        - 2 * b[6] * b[7] * sumt_x7 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + b[7] ** 2 * sumt_x14
        - 2 * b[7] ** 2 * sumt_x7 * x0**7
        + 2 * b[7] * sumt_y * x0**7
        - 2 * b[7] * sumt_yx7
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            - 2 * a[0] * b[7] * x0**7
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            - 2 * a[1] * b[7] * x0**8
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            - 2 * a[2] * b[7] * x0**9
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            - 2 * a[3] * b[7] * x0**10
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            - 2 * a[4] * b[6] * x0**10
            - 2 * a[4] * b[7] * x0**11
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            - 2 * a[5] * b[5] * x0**10
            - 2 * a[5] * b[6] * x0**11
            - 2 * a[5] * b[7] * x0**12
            + a[6] ** 2 * x0**12
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            - 2 * a[6] * b[4] * x0**10
            - 2 * a[6] * b[5] * x0**11
            - 2 * a[6] * b[6] * x0**12
            - 2 * a[6] * b[7] * x0**13
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + 2 * b[1] * b[7] * x0**8
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + 2 * b[2] * b[7] * x0**9
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + 2 * b[3] * b[7] * x0**10
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + 2 * b[4] * b[7] * x0**11
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + 2 * b[5] * b[7] * x0**12
            + b[6] ** 2 * x0**12
            + 2 * b[6] * b[7] * x0**13
            + b[7] ** 2 * x0**14
        )
    ) / (n - 15)


def rv_7_1(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumh_x13,
    sumh_x14,
    sumt_x,
    sumt_x2,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumh_yx7,
    sumt_yx,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * a[7] * sumh_x7
        + 2 * a[0] * b[1] * sumt_x
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * a[7] * sumh_x8
        + 2 * a[1] * b[1] * sumt_x * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * a[7] * sumh_x9
        + 2 * a[2] * b[1] * sumt_x * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * a[7] * sumh_x10
        + 2 * a[3] * b[1] * sumt_x * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * a[7] * sumh_x11
        + 2 * a[4] * b[1] * sumt_x * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * a[7] * sumh_x12
        + 2 * a[5] * b[1] * sumt_x * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * a[7] * sumh_x13
        + 2 * a[6] * b[1] * sumt_x * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        + a[7] ** 2 * sumh_x14
        + 2 * a[7] * b[1] * sumt_x * x0**7
        - 2 * a[7] * sumh_yx7
        - 2 * a[7] * sumt_y * x0**7
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            + 2 * a[0] * a[7] * x0**7
            - 2 * a[0] * b[1] * x0
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            + 2 * a[1] * a[7] * x0**8
            - 2 * a[1] * b[1] * x0**2
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            + 2 * a[2] * a[7] * x0**9
            - 2 * a[2] * b[1] * x0**3
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            + 2 * a[3] * a[7] * x0**10
            - 2 * a[3] * b[1] * x0**4
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            + 2 * a[4] * a[7] * x0**11
            - 2 * a[4] * b[1] * x0**5
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            + 2 * a[5] * a[7] * x0**12
            - 2 * a[5] * b[1] * x0**6
            + a[6] ** 2 * x0**12
            + 2 * a[6] * a[7] * x0**13
            - 2 * a[6] * b[1] * x0**7
            + a[7] ** 2 * x0**14
            - 2 * a[7] * b[1] * x0**8
            + b[1] ** 2 * x0**2
        )
    ) / (n - 10)


def rv_7_2(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumh_x13,
    sumh_x14,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumh_yx7,
    sumt_yx,
    sumt_yx2,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * a[7] * sumh_x7
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * a[7] * sumh_x8
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * a[7] * sumh_x9
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * a[7] * sumh_x10
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * a[7] * sumh_x11
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * a[7] * sumh_x12
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * a[7] * sumh_x13
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        + a[7] ** 2 * sumh_x14
        + 2 * a[7] * b[1] * sumt_x * x0**7
        + 2 * a[7] * b[2] * sumt_x2 * x0**7
        - 2 * a[7] * sumh_yx7
        - 2 * a[7] * sumt_y * x0**7
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            + 2 * a[0] * a[7] * x0**7
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            + 2 * a[1] * a[7] * x0**8
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            + 2 * a[2] * a[7] * x0**9
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            + 2 * a[3] * a[7] * x0**10
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            + 2 * a[4] * a[7] * x0**11
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            + 2 * a[5] * a[7] * x0**12
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            + a[6] ** 2 * x0**12
            + 2 * a[6] * a[7] * x0**13
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            + a[7] ** 2 * x0**14
            - 2 * a[7] * b[1] * x0**8
            - 2 * a[7] * b[2] * x0**9
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + b[2] ** 2 * x0**4
        )
    ) / (n - 11)


def rv_7_3(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumh_x13,
    sumh_x14,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumh_yx7,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * a[7] * sumh_x7
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * a[7] * sumh_x8
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * a[7] * sumh_x9
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * a[7] * sumh_x10
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * a[7] * sumh_x11
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * a[7] * sumh_x12
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * a[7] * sumh_x13
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        + a[7] ** 2 * sumh_x14
        + 2 * a[7] * b[1] * sumt_x * x0**7
        + 2 * a[7] * b[2] * sumt_x2 * x0**7
        + 2 * a[7] * b[3] * sumt_x3 * x0**7
        - 2 * a[7] * sumh_yx7
        - 2 * a[7] * sumt_y * x0**7
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            + 2 * a[0] * a[7] * x0**7
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            + 2 * a[1] * a[7] * x0**8
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            + 2 * a[2] * a[7] * x0**9
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            + 2 * a[3] * a[7] * x0**10
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            + 2 * a[4] * a[7] * x0**11
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            + 2 * a[5] * a[7] * x0**12
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            + a[6] ** 2 * x0**12
            + 2 * a[6] * a[7] * x0**13
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            + a[7] ** 2 * x0**14
            - 2 * a[7] * b[1] * x0**8
            - 2 * a[7] * b[2] * x0**9
            - 2 * a[7] * b[3] * x0**10
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + b[3] ** 2 * x0**6
        )
    ) / (n - 12)


def rv_7_4(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumh_x13,
    sumh_x14,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumh_yx7,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * a[7] * sumh_x7
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * a[7] * sumh_x8
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * a[7] * sumh_x9
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * a[7] * sumh_x10
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * a[7] * sumh_x11
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * a[7] * sumh_x12
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * a[7] * sumh_x13
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        + 2 * a[6] * b[4] * sumt_x4 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        + a[7] ** 2 * sumh_x14
        + 2 * a[7] * b[1] * sumt_x * x0**7
        + 2 * a[7] * b[2] * sumt_x2 * x0**7
        + 2 * a[7] * b[3] * sumt_x3 * x0**7
        + 2 * a[7] * b[4] * sumt_x4 * x0**7
        - 2 * a[7] * sumh_yx7
        - 2 * a[7] * sumt_y * x0**7
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            + 2 * a[0] * a[7] * x0**7
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            + 2 * a[1] * a[7] * x0**8
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            + 2 * a[2] * a[7] * x0**9
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            + 2 * a[3] * a[7] * x0**10
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            + 2 * a[4] * a[7] * x0**11
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            + 2 * a[5] * a[7] * x0**12
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            + a[6] ** 2 * x0**12
            + 2 * a[6] * a[7] * x0**13
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            - 2 * a[6] * b[4] * x0**10
            + a[7] ** 2 * x0**14
            - 2 * a[7] * b[1] * x0**8
            - 2 * a[7] * b[2] * x0**9
            - 2 * a[7] * b[3] * x0**10
            - 2 * a[7] * b[4] * x0**11
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + b[4] ** 2 * x0**8
        )
    ) / (n - 13)


def rv_7_5(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumh_x13,
    sumh_x14,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumh_yx7,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * a[7] * sumh_x7
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * a[7] * sumh_x8
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * a[7] * sumh_x9
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * a[7] * sumh_x10
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * a[7] * sumh_x11
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * a[7] * sumh_x12
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        + 2 * a[5] * b[5] * sumt_x5 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * a[7] * sumh_x13
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        + 2 * a[6] * b[4] * sumt_x4 * x0**6
        + 2 * a[6] * b[5] * sumt_x5 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        + a[7] ** 2 * sumh_x14
        + 2 * a[7] * b[1] * sumt_x * x0**7
        + 2 * a[7] * b[2] * sumt_x2 * x0**7
        + 2 * a[7] * b[3] * sumt_x3 * x0**7
        + 2 * a[7] * b[4] * sumt_x4 * x0**7
        + 2 * a[7] * b[5] * sumt_x5 * x0**7
        - 2 * a[7] * sumh_yx7
        - 2 * a[7] * sumt_y * x0**7
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            + 2 * a[0] * a[7] * x0**7
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            + 2 * a[1] * a[7] * x0**8
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            + 2 * a[2] * a[7] * x0**9
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            + 2 * a[3] * a[7] * x0**10
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            + 2 * a[4] * a[7] * x0**11
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            + 2 * a[5] * a[7] * x0**12
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            - 2 * a[5] * b[5] * x0**10
            + a[6] ** 2 * x0**12
            + 2 * a[6] * a[7] * x0**13
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            - 2 * a[6] * b[4] * x0**10
            - 2 * a[6] * b[5] * x0**11
            + a[7] ** 2 * x0**14
            - 2 * a[7] * b[1] * x0**8
            - 2 * a[7] * b[2] * x0**9
            - 2 * a[7] * b[3] * x0**10
            - 2 * a[7] * b[4] * x0**11
            - 2 * a[7] * b[5] * x0**12
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + b[5] ** 2 * x0**10
        )
    ) / (n - 14)


def rv_7_6(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumh_x13,
    sumh_x14,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumh_yx7,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * a[7] * sumh_x7
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * a[7] * sumh_x8
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * a[7] * sumh_x9
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * a[7] * sumh_x10
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * a[7] * sumh_x11
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        + 2 * a[4] * b[6] * sumt_x6 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * a[7] * sumh_x12
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        + 2 * a[5] * b[5] * sumt_x5 * x0**5
        + 2 * a[5] * b[6] * sumt_x6 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * a[7] * sumh_x13
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        + 2 * a[6] * b[4] * sumt_x4 * x0**6
        + 2 * a[6] * b[5] * sumt_x5 * x0**6
        + 2 * a[6] * b[6] * sumt_x6 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        + a[7] ** 2 * sumh_x14
        + 2 * a[7] * b[1] * sumt_x * x0**7
        + 2 * a[7] * b[2] * sumt_x2 * x0**7
        + 2 * a[7] * b[3] * sumt_x3 * x0**7
        + 2 * a[7] * b[4] * sumt_x4 * x0**7
        + 2 * a[7] * b[5] * sumt_x5 * x0**7
        + 2 * a[7] * b[6] * sumt_x6 * x0**7
        - 2 * a[7] * sumh_yx7
        - 2 * a[7] * sumt_y * x0**7
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            + 2 * a[0] * a[7] * x0**7
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            + 2 * a[1] * a[7] * x0**8
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            + 2 * a[2] * a[7] * x0**9
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            + 2 * a[3] * a[7] * x0**10
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            + 2 * a[4] * a[7] * x0**11
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            - 2 * a[4] * b[6] * x0**10
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            + 2 * a[5] * a[7] * x0**12
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            - 2 * a[5] * b[5] * x0**10
            - 2 * a[5] * b[6] * x0**11
            + a[6] ** 2 * x0**12
            + 2 * a[6] * a[7] * x0**13
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            - 2 * a[6] * b[4] * x0**10
            - 2 * a[6] * b[5] * x0**11
            - 2 * a[6] * b[6] * x0**12
            + a[7] ** 2 * x0**14
            - 2 * a[7] * b[1] * x0**8
            - 2 * a[7] * b[2] * x0**9
            - 2 * a[7] * b[3] * x0**10
            - 2 * a[7] * b[4] * x0**11
            - 2 * a[7] * b[5] * x0**12
            - 2 * a[7] * b[6] * x0**13
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + b[6] ** 2 * x0**12
        )
    ) / (n - 15)


def rv_7_7(
    x0,
    k,
    n,
    a,
    b,
    sumh_x,
    sumh_x2,
    sumh_x3,
    sumh_x4,
    sumh_x5,
    sumh_x6,
    sumh_x7,
    sumh_x8,
    sumh_x9,
    sumh_x10,
    sumh_x11,
    sumh_x12,
    sumh_x13,
    sumh_x14,
    sumt_x,
    sumt_x2,
    sumt_x3,
    sumt_x4,
    sumt_x5,
    sumt_x6,
    sumt_x7,
    sumt_x8,
    sumt_x9,
    sumt_x10,
    sumt_x11,
    sumt_x12,
    sumt_x13,
    sumt_x14,
    sumh_y,
    sumh_y2,
    sumt_y,
    sumt_y2,
    sumh_yx,
    sumh_yx2,
    sumh_yx3,
    sumh_yx4,
    sumh_yx5,
    sumh_yx6,
    sumh_yx7,
    sumt_yx,
    sumt_yx2,
    sumt_yx3,
    sumt_yx4,
    sumt_yx5,
    sumt_yx6,
    sumt_yx7,
):
    return (
        a[0] ** 2 * k
        + 2 * a[0] * a[1] * sumh_x
        + 2 * a[0] * a[2] * sumh_x2
        + 2 * a[0] * a[3] * sumh_x3
        + 2 * a[0] * a[4] * sumh_x4
        + 2 * a[0] * a[5] * sumh_x5
        + 2 * a[0] * a[6] * sumh_x6
        + 2 * a[0] * a[7] * sumh_x7
        + 2 * a[0] * b[1] * sumt_x
        + 2 * a[0] * b[2] * sumt_x2
        + 2 * a[0] * b[3] * sumt_x3
        + 2 * a[0] * b[4] * sumt_x4
        + 2 * a[0] * b[5] * sumt_x5
        + 2 * a[0] * b[6] * sumt_x6
        + 2 * a[0] * b[7] * sumt_x7
        - 2 * a[0] * sumh_y
        - 2 * a[0] * sumt_y
        + a[1] ** 2 * sumh_x2
        + 2 * a[1] * a[2] * sumh_x3
        + 2 * a[1] * a[3] * sumh_x4
        + 2 * a[1] * a[4] * sumh_x5
        + 2 * a[1] * a[5] * sumh_x6
        + 2 * a[1] * a[6] * sumh_x7
        + 2 * a[1] * a[7] * sumh_x8
        + 2 * a[1] * b[1] * sumt_x * x0
        + 2 * a[1] * b[2] * sumt_x2 * x0
        + 2 * a[1] * b[3] * sumt_x3 * x0
        + 2 * a[1] * b[4] * sumt_x4 * x0
        + 2 * a[1] * b[5] * sumt_x5 * x0
        + 2 * a[1] * b[6] * sumt_x6 * x0
        + 2 * a[1] * b[7] * sumt_x7 * x0
        - 2 * a[1] * sumh_yx
        - 2 * a[1] * sumt_y * x0
        + a[2] ** 2 * sumh_x4
        + 2 * a[2] * a[3] * sumh_x5
        + 2 * a[2] * a[4] * sumh_x6
        + 2 * a[2] * a[5] * sumh_x7
        + 2 * a[2] * a[6] * sumh_x8
        + 2 * a[2] * a[7] * sumh_x9
        + 2 * a[2] * b[1] * sumt_x * x0**2
        + 2 * a[2] * b[2] * sumt_x2 * x0**2
        + 2 * a[2] * b[3] * sumt_x3 * x0**2
        + 2 * a[2] * b[4] * sumt_x4 * x0**2
        + 2 * a[2] * b[5] * sumt_x5 * x0**2
        + 2 * a[2] * b[6] * sumt_x6 * x0**2
        + 2 * a[2] * b[7] * sumt_x7 * x0**2
        - 2 * a[2] * sumh_yx2
        - 2 * a[2] * sumt_y * x0**2
        + a[3] ** 2 * sumh_x6
        + 2 * a[3] * a[4] * sumh_x7
        + 2 * a[3] * a[5] * sumh_x8
        + 2 * a[3] * a[6] * sumh_x9
        + 2 * a[3] * a[7] * sumh_x10
        + 2 * a[3] * b[1] * sumt_x * x0**3
        + 2 * a[3] * b[2] * sumt_x2 * x0**3
        + 2 * a[3] * b[3] * sumt_x3 * x0**3
        + 2 * a[3] * b[4] * sumt_x4 * x0**3
        + 2 * a[3] * b[5] * sumt_x5 * x0**3
        + 2 * a[3] * b[6] * sumt_x6 * x0**3
        + 2 * a[3] * b[7] * sumt_x7 * x0**3
        - 2 * a[3] * sumh_yx3
        - 2 * a[3] * sumt_y * x0**3
        + a[4] ** 2 * sumh_x8
        + 2 * a[4] * a[5] * sumh_x9
        + 2 * a[4] * a[6] * sumh_x10
        + 2 * a[4] * a[7] * sumh_x11
        + 2 * a[4] * b[1] * sumt_x * x0**4
        + 2 * a[4] * b[2] * sumt_x2 * x0**4
        + 2 * a[4] * b[3] * sumt_x3 * x0**4
        + 2 * a[4] * b[4] * sumt_x4 * x0**4
        + 2 * a[4] * b[5] * sumt_x5 * x0**4
        + 2 * a[4] * b[6] * sumt_x6 * x0**4
        + 2 * a[4] * b[7] * sumt_x7 * x0**4
        - 2 * a[4] * sumh_yx4
        - 2 * a[4] * sumt_y * x0**4
        + a[5] ** 2 * sumh_x10
        + 2 * a[5] * a[6] * sumh_x11
        + 2 * a[5] * a[7] * sumh_x12
        + 2 * a[5] * b[1] * sumt_x * x0**5
        + 2 * a[5] * b[2] * sumt_x2 * x0**5
        + 2 * a[5] * b[3] * sumt_x3 * x0**5
        + 2 * a[5] * b[4] * sumt_x4 * x0**5
        + 2 * a[5] * b[5] * sumt_x5 * x0**5
        + 2 * a[5] * b[6] * sumt_x6 * x0**5
        + 2 * a[5] * b[7] * sumt_x7 * x0**5
        - 2 * a[5] * sumh_yx5
        - 2 * a[5] * sumt_y * x0**5
        + a[6] ** 2 * sumh_x12
        + 2 * a[6] * a[7] * sumh_x13
        + 2 * a[6] * b[1] * sumt_x * x0**6
        + 2 * a[6] * b[2] * sumt_x2 * x0**6
        + 2 * a[6] * b[3] * sumt_x3 * x0**6
        + 2 * a[6] * b[4] * sumt_x4 * x0**6
        + 2 * a[6] * b[5] * sumt_x5 * x0**6
        + 2 * a[6] * b[6] * sumt_x6 * x0**6
        + 2 * a[6] * b[7] * sumt_x7 * x0**6
        - 2 * a[6] * sumh_yx6
        - 2 * a[6] * sumt_y * x0**6
        + a[7] ** 2 * sumh_x14
        + 2 * a[7] * b[1] * sumt_x * x0**7
        + 2 * a[7] * b[2] * sumt_x2 * x0**7
        + 2 * a[7] * b[3] * sumt_x3 * x0**7
        + 2 * a[7] * b[4] * sumt_x4 * x0**7
        + 2 * a[7] * b[5] * sumt_x5 * x0**7
        + 2 * a[7] * b[6] * sumt_x6 * x0**7
        + 2 * a[7] * b[7] * sumt_x7 * x0**7
        - 2 * a[7] * sumh_yx7
        - 2 * a[7] * sumt_y * x0**7
        - 2 * b[1] ** 2 * sumt_x * x0
        + b[1] ** 2 * sumt_x2
        - 2 * b[1] * b[2] * sumt_x * x0**2
        - 2 * b[1] * b[2] * sumt_x2 * x0
        + 2 * b[1] * b[2] * sumt_x3
        - 2 * b[1] * b[3] * sumt_x * x0**3
        - 2 * b[1] * b[3] * sumt_x3 * x0
        + 2 * b[1] * b[3] * sumt_x4
        - 2 * b[1] * b[4] * sumt_x * x0**4
        - 2 * b[1] * b[4] * sumt_x4 * x0
        + 2 * b[1] * b[4] * sumt_x5
        - 2 * b[1] * b[5] * sumt_x * x0**5
        - 2 * b[1] * b[5] * sumt_x5 * x0
        + 2 * b[1] * b[5] * sumt_x6
        - 2 * b[1] * b[6] * sumt_x * x0**6
        - 2 * b[1] * b[6] * sumt_x6 * x0
        + 2 * b[1] * b[6] * sumt_x7
        - 2 * b[1] * b[7] * sumt_x * x0**7
        - 2 * b[1] * b[7] * sumt_x7 * x0
        + 2 * b[1] * b[7] * sumt_x8
        + 2 * b[1] * sumt_y * x0
        - 2 * b[1] * sumt_yx
        - 2 * b[2] ** 2 * sumt_x2 * x0**2
        + b[2] ** 2 * sumt_x4
        - 2 * b[2] * b[3] * sumt_x2 * x0**3
        - 2 * b[2] * b[3] * sumt_x3 * x0**2
        + 2 * b[2] * b[3] * sumt_x5
        - 2 * b[2] * b[4] * sumt_x2 * x0**4
        - 2 * b[2] * b[4] * sumt_x4 * x0**2
        + 2 * b[2] * b[4] * sumt_x6
        - 2 * b[2] * b[5] * sumt_x2 * x0**5
        - 2 * b[2] * b[5] * sumt_x5 * x0**2
        + 2 * b[2] * b[5] * sumt_x7
        - 2 * b[2] * b[6] * sumt_x2 * x0**6
        - 2 * b[2] * b[6] * sumt_x6 * x0**2
        + 2 * b[2] * b[6] * sumt_x8
        - 2 * b[2] * b[7] * sumt_x2 * x0**7
        - 2 * b[2] * b[7] * sumt_x7 * x0**2
        + 2 * b[2] * b[7] * sumt_x9
        + 2 * b[2] * sumt_y * x0**2
        - 2 * b[2] * sumt_yx2
        - 2 * b[3] ** 2 * sumt_x3 * x0**3
        + b[3] ** 2 * sumt_x6
        - 2 * b[3] * b[4] * sumt_x3 * x0**4
        - 2 * b[3] * b[4] * sumt_x4 * x0**3
        + 2 * b[3] * b[4] * sumt_x7
        - 2 * b[3] * b[5] * sumt_x3 * x0**5
        - 2 * b[3] * b[5] * sumt_x5 * x0**3
        + 2 * b[3] * b[5] * sumt_x8
        - 2 * b[3] * b[6] * sumt_x3 * x0**6
        - 2 * b[3] * b[6] * sumt_x6 * x0**3
        + 2 * b[3] * b[6] * sumt_x9
        + 2 * b[3] * b[7] * sumt_x10
        - 2 * b[3] * b[7] * sumt_x3 * x0**7
        - 2 * b[3] * b[7] * sumt_x7 * x0**3
        + 2 * b[3] * sumt_y * x0**3
        - 2 * b[3] * sumt_yx3
        - 2 * b[4] ** 2 * sumt_x4 * x0**4
        + b[4] ** 2 * sumt_x8
        - 2 * b[4] * b[5] * sumt_x4 * x0**5
        - 2 * b[4] * b[5] * sumt_x5 * x0**4
        + 2 * b[4] * b[5] * sumt_x9
        + 2 * b[4] * b[6] * sumt_x10
        - 2 * b[4] * b[6] * sumt_x4 * x0**6
        - 2 * b[4] * b[6] * sumt_x6 * x0**4
        + 2 * b[4] * b[7] * sumt_x11
        - 2 * b[4] * b[7] * sumt_x4 * x0**7
        - 2 * b[4] * b[7] * sumt_x7 * x0**4
        + 2 * b[4] * sumt_y * x0**4
        - 2 * b[4] * sumt_yx4
        + b[5] ** 2 * sumt_x10
        - 2 * b[5] ** 2 * sumt_x5 * x0**5
        + 2 * b[5] * b[6] * sumt_x11
        - 2 * b[5] * b[6] * sumt_x5 * x0**6
        - 2 * b[5] * b[6] * sumt_x6 * x0**5
        + 2 * b[5] * b[7] * sumt_x12
        - 2 * b[5] * b[7] * sumt_x5 * x0**7
        - 2 * b[5] * b[7] * sumt_x7 * x0**5
        + 2 * b[5] * sumt_y * x0**5
        - 2 * b[5] * sumt_yx5
        + b[6] ** 2 * sumt_x12
        - 2 * b[6] ** 2 * sumt_x6 * x0**6
        + 2 * b[6] * b[7] * sumt_x13
        - 2 * b[6] * b[7] * sumt_x6 * x0**7
        - 2 * b[6] * b[7] * sumt_x7 * x0**6
        + 2 * b[6] * sumt_y * x0**6
        - 2 * b[6] * sumt_yx6
        + b[7] ** 2 * sumt_x14
        - 2 * b[7] ** 2 * sumt_x7 * x0**7
        + 2 * b[7] * sumt_y * x0**7
        - 2 * b[7] * sumt_yx7
        + sumh_y2
        + sumt_y2
        + (-k + n)
        * (
            a[0] ** 2
            + 2 * a[0] * a[1] * x0
            + 2 * a[0] * a[2] * x0**2
            + 2 * a[0] * a[3] * x0**3
            + 2 * a[0] * a[4] * x0**4
            + 2 * a[0] * a[5] * x0**5
            + 2 * a[0] * a[6] * x0**6
            + 2 * a[0] * a[7] * x0**7
            - 2 * a[0] * b[1] * x0
            - 2 * a[0] * b[2] * x0**2
            - 2 * a[0] * b[3] * x0**3
            - 2 * a[0] * b[4] * x0**4
            - 2 * a[0] * b[5] * x0**5
            - 2 * a[0] * b[6] * x0**6
            - 2 * a[0] * b[7] * x0**7
            + a[1] ** 2 * x0**2
            + 2 * a[1] * a[2] * x0**3
            + 2 * a[1] * a[3] * x0**4
            + 2 * a[1] * a[4] * x0**5
            + 2 * a[1] * a[5] * x0**6
            + 2 * a[1] * a[6] * x0**7
            + 2 * a[1] * a[7] * x0**8
            - 2 * a[1] * b[1] * x0**2
            - 2 * a[1] * b[2] * x0**3
            - 2 * a[1] * b[3] * x0**4
            - 2 * a[1] * b[4] * x0**5
            - 2 * a[1] * b[5] * x0**6
            - 2 * a[1] * b[6] * x0**7
            - 2 * a[1] * b[7] * x0**8
            + a[2] ** 2 * x0**4
            + 2 * a[2] * a[3] * x0**5
            + 2 * a[2] * a[4] * x0**6
            + 2 * a[2] * a[5] * x0**7
            + 2 * a[2] * a[6] * x0**8
            + 2 * a[2] * a[7] * x0**9
            - 2 * a[2] * b[1] * x0**3
            - 2 * a[2] * b[2] * x0**4
            - 2 * a[2] * b[3] * x0**5
            - 2 * a[2] * b[4] * x0**6
            - 2 * a[2] * b[5] * x0**7
            - 2 * a[2] * b[6] * x0**8
            - 2 * a[2] * b[7] * x0**9
            + a[3] ** 2 * x0**6
            + 2 * a[3] * a[4] * x0**7
            + 2 * a[3] * a[5] * x0**8
            + 2 * a[3] * a[6] * x0**9
            + 2 * a[3] * a[7] * x0**10
            - 2 * a[3] * b[1] * x0**4
            - 2 * a[3] * b[2] * x0**5
            - 2 * a[3] * b[3] * x0**6
            - 2 * a[3] * b[4] * x0**7
            - 2 * a[3] * b[5] * x0**8
            - 2 * a[3] * b[6] * x0**9
            - 2 * a[3] * b[7] * x0**10
            + a[4] ** 2 * x0**8
            + 2 * a[4] * a[5] * x0**9
            + 2 * a[4] * a[6] * x0**10
            + 2 * a[4] * a[7] * x0**11
            - 2 * a[4] * b[1] * x0**5
            - 2 * a[4] * b[2] * x0**6
            - 2 * a[4] * b[3] * x0**7
            - 2 * a[4] * b[4] * x0**8
            - 2 * a[4] * b[5] * x0**9
            - 2 * a[4] * b[6] * x0**10
            - 2 * a[4] * b[7] * x0**11
            + a[5] ** 2 * x0**10
            + 2 * a[5] * a[6] * x0**11
            + 2 * a[5] * a[7] * x0**12
            - 2 * a[5] * b[1] * x0**6
            - 2 * a[5] * b[2] * x0**7
            - 2 * a[5] * b[3] * x0**8
            - 2 * a[5] * b[4] * x0**9
            - 2 * a[5] * b[5] * x0**10
            - 2 * a[5] * b[6] * x0**11
            - 2 * a[5] * b[7] * x0**12
            + a[6] ** 2 * x0**12
            + 2 * a[6] * a[7] * x0**13
            - 2 * a[6] * b[1] * x0**7
            - 2 * a[6] * b[2] * x0**8
            - 2 * a[6] * b[3] * x0**9
            - 2 * a[6] * b[4] * x0**10
            - 2 * a[6] * b[5] * x0**11
            - 2 * a[6] * b[6] * x0**12
            - 2 * a[6] * b[7] * x0**13
            + a[7] ** 2 * x0**14
            - 2 * a[7] * b[1] * x0**8
            - 2 * a[7] * b[2] * x0**9
            - 2 * a[7] * b[3] * x0**10
            - 2 * a[7] * b[4] * x0**11
            - 2 * a[7] * b[5] * x0**12
            - 2 * a[7] * b[6] * x0**13
            - 2 * a[7] * b[7] * x0**14
            + b[1] ** 2 * x0**2
            + 2 * b[1] * b[2] * x0**3
            + 2 * b[1] * b[3] * x0**4
            + 2 * b[1] * b[4] * x0**5
            + 2 * b[1] * b[5] * x0**6
            + 2 * b[1] * b[6] * x0**7
            + 2 * b[1] * b[7] * x0**8
            + b[2] ** 2 * x0**4
            + 2 * b[2] * b[3] * x0**5
            + 2 * b[2] * b[4] * x0**6
            + 2 * b[2] * b[5] * x0**7
            + 2 * b[2] * b[6] * x0**8
            + 2 * b[2] * b[7] * x0**9
            + b[3] ** 2 * x0**6
            + 2 * b[3] * b[4] * x0**7
            + 2 * b[3] * b[5] * x0**8
            + 2 * b[3] * b[6] * x0**9
            + 2 * b[3] * b[7] * x0**10
            + b[4] ** 2 * x0**8
            + 2 * b[4] * b[5] * x0**9
            + 2 * b[4] * b[6] * x0**10
            + 2 * b[4] * b[7] * x0**11
            + b[5] ** 2 * x0**10
            + 2 * b[5] * b[6] * x0**11
            + 2 * b[5] * b[7] * x0**12
            + b[6] ** 2 * x0**12
            + 2 * b[6] * b[7] * x0**13
            + b[7] ** 2 * x0**14
        )
    ) / (n - 16)


dispatcher = {
    (1, 1): rv_1_1,
    (1, 2): rv_1_2,
    (1, 3): rv_1_3,
    (1, 4): rv_1_4,
    (1, 5): rv_1_5,
    (1, 6): rv_1_6,
    (1, 7): rv_1_7,
    (2, 1): rv_2_1,
    (2, 2): rv_2_2,
    (2, 3): rv_2_3,
    (2, 4): rv_2_4,
    (2, 5): rv_2_5,
    (2, 6): rv_2_6,
    (2, 7): rv_2_7,
    (3, 1): rv_3_1,
    (3, 2): rv_3_2,
    (3, 3): rv_3_3,
    (3, 4): rv_3_4,
    (3, 5): rv_3_5,
    (3, 6): rv_3_6,
    (3, 7): rv_3_7,
    (4, 1): rv_4_1,
    (4, 2): rv_4_2,
    (4, 3): rv_4_3,
    (4, 4): rv_4_4,
    (4, 5): rv_4_5,
    (4, 6): rv_4_6,
    (4, 7): rv_4_7,
    (5, 1): rv_5_1,
    (5, 2): rv_5_2,
    (5, 3): rv_5_3,
    (5, 4): rv_5_4,
    (5, 5): rv_5_5,
    (5, 6): rv_5_6,
    (5, 7): rv_5_7,
    (6, 1): rv_6_1,
    (6, 2): rv_6_2,
    (6, 3): rv_6_3,
    (6, 4): rv_6_4,
    (6, 5): rv_6_5,
    (6, 6): rv_6_6,
    (6, 7): rv_6_7,
    (7, 1): rv_7_1,
    (7, 2): rv_7_2,
    (7, 3): rv_7_3,
    (7, 4): rv_7_4,
    (7, 5): rv_7_5,
    (7, 6): rv_7_6,
    (7, 7): rv_7_7
}