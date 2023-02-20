def shift_1(a, x_m):
    return [a[0] - a[1] * x_m, a[1]]


def shift_2(a, x_m):
    return [a[0] - a[1] * x_m + a[2] * x_m**2, a[1] - 2 * a[2] * x_m, a[2]]


def shift_3(a, x_m):
    return [
        a[0] - a[1] * x_m + a[2] * x_m**2 - a[3] * x_m**3,
        a[1] - 2 * a[2] * x_m + 3 * a[3] * x_m**2,
        a[2] - 3 * a[3] * x_m,
        a[3],
    ]


def shift_4(a, x_m):
    return [
        a[0] - a[1] * x_m + a[2] * x_m**2 - a[3] * x_m**3 + a[4] * x_m**4,
        a[1] - 2 * a[2] * x_m + 3 * a[3] * x_m**2 - 4 * a[4] * x_m**3,
        a[2] - 3 * a[3] * x_m + 6 * a[4] * x_m**2,
        a[3] - 4 * a[4] * x_m,
        a[4],
    ]


def shift_5(a, x_m):
    return [
        a[0]
        - a[1] * x_m
        + a[2] * x_m**2
        - a[3] * x_m**3
        + a[4] * x_m**4
        - a[5] * x_m**5,
        a[1]
        - 2 * a[2] * x_m
        + 3 * a[3] * x_m**2
        - 4 * a[4] * x_m**3
        + 5 * a[5] * x_m**4,
        a[2] - 3 * a[3] * x_m + 6 * a[4] * x_m**2 - 10 * a[5] * x_m**3,
        a[3] - 4 * a[4] * x_m + 10 * a[5] * x_m**2,
        a[4] - 5 * a[5] * x_m,
        a[5],
    ]


def shift_6(a, x_m):
    return [
        a[0]
        - a[1] * x_m
        + a[2] * x_m**2
        - a[3] * x_m**3
        + a[4] * x_m**4
        - a[5] * x_m**5
        + a[6] * x_m**6,
        a[1]
        - 2 * a[2] * x_m
        + 3 * a[3] * x_m**2
        - 4 * a[4] * x_m**3
        + 5 * a[5] * x_m**4
        - 6 * a[6] * x_m**5,
        a[2]
        - 3 * a[3] * x_m
        + 6 * a[4] * x_m**2
        - 10 * a[5] * x_m**3
        + 15 * a[6] * x_m**4,
        a[3] - 4 * a[4] * x_m + 10 * a[5] * x_m**2 - 20 * a[6] * x_m**3,
        a[4] - 5 * a[5] * x_m + 15 * a[6] * x_m**2,
        a[5] - 6 * a[6] * x_m,
        a[6],
    ]


def shift_7(a, x_m):
    return [
        a[0]
        - a[1] * x_m
        + a[2] * x_m**2
        - a[3] * x_m**3
        + a[4] * x_m**4
        - a[5] * x_m**5
        + a[6] * x_m**6
        - a[7] * x_m**7,
        a[1]
        - 2 * a[2] * x_m
        + 3 * a[3] * x_m**2
        - 4 * a[4] * x_m**3
        + 5 * a[5] * x_m**4
        - 6 * a[6] * x_m**5
        + 7 * a[7] * x_m**6,
        a[2]
        - 3 * a[3] * x_m
        + 6 * a[4] * x_m**2
        - 10 * a[5] * x_m**3
        + 15 * a[6] * x_m**4
        - 21 * a[7] * x_m**5,
        a[3]
        - 4 * a[4] * x_m
        + 10 * a[5] * x_m**2
        - 20 * a[6] * x_m**3
        + 35 * a[7] * x_m**4,
        a[4] - 5 * a[5] * x_m + 15 * a[6] * x_m**2 - 35 * a[7] * x_m**3,
        a[5] - 6 * a[6] * x_m + 21 * a[7] * x_m**2,
        a[6] - 7 * a[7] * x_m,
        a[7],
    ]



dispatcher = {
    1: shift_1,
    2: shift_2,
    3: shift_3,
    4: shift_4,
    5: shift_5,
    6: shift_6,
    7: shift_7
}