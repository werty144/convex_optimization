class Polynom:
    def __init__(self, *params):
        self.params = params

    def evaluate(self, x):
        res = 0
        xi = 1
        for param in self.params:
            res += param * xi
            xi *= x
        return res

    def derivative(self):
        return Polynom(*[i * param for i, param in enumerate(self.params)][1:])


def locate_roots(poly: Polynom, l, r, step=1e-3):
    segs = []
    last = l
    cur = l + step
    while cur < r:
        if poly.evaluate(cur) * poly.evaluate(last) < 0:
            segs.append((last, cur))
            last = cur
        if poly.evaluate(cur) == 0:
            segs.append((last, cur + step / 2))
            last = cur + step / 2
        cur += step
    return segs


def root_in_seg(poly, l, r, precision=1e-4):
    assert poly.evaluate(l) * poly.evaluate(r) < 0

    def f(x):
        val = poly.evaluate(x)
        if poly.evaluate(r) > 0:
            return val
        else:
            return -val

    while r - l > precision * 2:
        m = (l + r) / 2
        if f(m) > 0:
            r = m
        else:
            l = m

    return (l + r) / 2


def find_roots(p, l, r, **kwargs):
    roots = []
    for l, r in locate_roots(p, l, r, **kwargs):
        roots.append(root_in_seg(p, l, r, **kwargs))

    return roots


def find_min(p: Polynom, l, r, **kwargs):
    derivative = p.derivative()
    candidates = [l, r] + find_roots(derivative, l, r, **kwargs)
    return min(map(lambda x: p.evaluate(x), candidates))
