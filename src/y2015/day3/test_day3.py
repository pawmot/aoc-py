import os

def solve_a(data):
    cur = (0, 0)
    set = {cur}
    for c in data:
        if c == '<':
            cur = (cur[0] - 1, cur[1])
        elif c == '>':
            cur = (cur[0] + 1, cur[1])
        elif c == 'v':
            cur = (cur[0], cur[1] - 1)
        elif c == '^':
            cur = (cur[0], cur[1] + 1)
        set.add(cur)
    return len(set)


def solve_b(data):
    curA = (0, 0)
    curB = (0, 0)
    set = {curA, curB}
    for (i, c) in enumerate(data):
        if i % 2 == 0:
            cur = curA
        else:
            cur = curB
        if c == '<':
            cur = (cur[0] - 1, cur[1])
        elif c == '>':
            cur = (cur[0] + 1, cur[1])
        elif c == 'v':
            cur = (cur[0], cur[1] - 1)
        elif c == '^':
            cur = (cur[0], cur[1] + 1)
        set.add(cur)
        if i % 2 == 0:
            curA = cur
        else:
            curB = cur
    return len(set)


def test_a_sample_1():
    data = '>'
    assert solve_a(data) == 2


def test_a_sample_2():
    data = '^>v<'
    assert solve_a(data) == 4


def test_a_sample_3():
    data = '^v^v^v^v^v'
    assert solve_a(data) == 2


def test_a_full():
    data = load_data('full')
    assert solve_a(data[0]) == 2572


def test_b_sample_1():
    data = '^v'
    assert solve_b(data) == 3


def test_b_sample_2():
    data = '^>v<'
    assert solve_b(data) == 3


def test_b_sample_3():
    data = '^v^v^v^v^v'
    assert solve_b(data) == 11


def test_b_full():
    data = load_data('full')
    assert solve_b(data[0]) == 2631


def load_data(set):
    with open(os.path.dirname(__file__) + f'/{set}.txt') as f:
        lines = f.read().splitlines()
    return lines

