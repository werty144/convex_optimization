from math import exp


def min_trisection(a, b, c, d, precision=1e-4):
    def f(x):
        return exp(a * x) + exp(-b * x) + c * (x - d) ** 2

    l, r = -abs(10 * d), abs(10 * d)
    while r - l > 2 * precision:
        snd = l + (1/3) * (r - l)
        trd = l + (2/3) * (r - l)
        if f(snd) < f(trd):
            r = trd
        else:
            l = snd

    return f((l + r) / 2)


def min_bisection(a, b, c, d, precision=1e-4):
    def f(x):
        return exp(a * x) + exp(-b * x) + c * (x - d) ** 2

    def derivative(x):
        return a * exp(a * x) - b * exp(-b * x) + 2 * c * (x - d)

    l, r = -abs(10 * d), abs(10 * d)
    while r - l > 2 * precision:
        m = (l + r) / 2
        if derivative(m) > 0:
            r = m
        else:
            l = m

    return f((l + r) / 2)


def min_newton(a, b, c, d, iteration_n=1000):
    def f(x):
        return exp(a * x) + exp(-b * x) + c * (x - d) ** 2

    def derivative(x):
        return a * exp(a * x) - b * exp(-b * x) + 2 * c * (x - d)

    def snd_derivative(x):
        return a ** 2 * exp(a * x) + b ** 2 * exp(- b * x) + 2 * c

    cur = 10 * d
    for _ in range(iteration_n):
        cur = cur - derivative(cur) / snd_derivative(cur)

    return f(cur)
