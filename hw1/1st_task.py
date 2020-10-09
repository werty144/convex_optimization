def k_root_bisection(a, k, precision=1e-4):
    assert a > 0

    def f(cur):
        return a - cur ** k

    l, r = 0, a  # assuming here that k >= 1
    while r - l > 2 * precision:
        m = (l + r) / 2
        if f(m) > 0:
            l = m
        else:
            r = m
    return (l + r) / 2


def k_root_newton(a, k, iteration_n=1000):
    if a < 0:
        assert isinstance(k, int) and k % 2 == 1

    def f(x):
        return x ** k - a

    def derivative(x):
        return k * x ** (k - 1)

    x = a
    for _ in range(iteration_n):
        x = x - f(x) / derivative(x)

    return x
