import os

def solve_a(data):
    (ranges, ids) = data
    res = 0
    for id in ids:
        in_range = False
        for r in ranges:
            (start, end) = r
            if start <= id <= end:
                in_range = True
                break
        if in_range:
            res += 1

    return res


def solve_b(data):
    (ranges, _) = data
    ranges.sort(key = lambda x: x[0])
    res = 0
    last = 0
    for r in ranges:
        (start, end) = r
        if end <= last:
            continue
        if start <= last:
            start = last + 1
        res += end - start + 1
        last = end

    return res


def test_a_sample():
    data = load_data('sample')
    assert solve_a(data) == 3


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 896


def test_b_sample():
    data = load_data('sample')
    assert solve_b(data) == 14


def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 346240317247002


def load_data(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    i = lines.index("")
    ranges = [list(map(int, r.split("-"))) for r in lines[:i]]
    ids = [int(id) for id in lines[i+1:] if id]

    return (ranges, ids)

