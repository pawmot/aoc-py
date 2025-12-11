import os
from itertools import product


def area(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)


def solve_a(data):
    pairs = (p for p in product(range(len(data)), repeat = 2) if p[0] < p[1])
    return max(map(lambda p: area(data[p[0]], data[p[1]]), pairs))


def solve_b(data):
    ends = data[1:]
    ends.append(data[0])
    sides = list(zip(data, ends))
    print(len(sides))
    hor = list(filter(lambda s: s[0][0] == s[1][0], sides))
    ver = list(filter(lambda s: s[0][1] == s[1][1], sides))

    pairs = (p for p in product(range(len(data)), repeat = 2) if p[0] < p[1])
    max_area = 0
    for p in pairs:
        a = data[p[0]]
        b = data[p[1]]
        min_r = min(a[0], b[0])
        max_r = max(a[0], b[0])
        min_c = min(a[1], b[1])
        max_c = max(a[1], b[1])

        if any((min_c < v[0][1] < max_c) and not(max(v[0][0], v[1][0]) <= min_r or min(v[0][0], v[1][0]) >= max_r) for v in ver):
            continue

        if any((min_r < h[0][0] < max_r) and not(max(h[0][1], h[1][1]) <= min_c or min(h[0][1], h[1][1]) >= max_c) for h in hor):
            continue

        max_area = max(max_area, area(a, b))

    return max_area


def test_a_sample():
    data = load_data('sample')
    assert solve_a(data) == 50


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 4763932976


def test_b_sample():
    data = load_data('sample')
    assert solve_b(data) == 24


def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 1501292304


def load_data(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    data = [[int(c) for c in l.split(',')] for l in lines]
    return data

