import os


def solve_a(data):
    res = 0
    for c in data:
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
    return res


def solve_b(data):
    floor = 0
    for (i, c) in enumerate(data):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor < 0:
            return i + 1


def test_a_sample_1():
    data = '(())'
    assert solve_a(data) == 0


def test_a_sample_2():
    data = '()()'
    assert solve_a(data) == 0

def test_a_sample_3():
    data = '((('
    assert solve_a(data) == 3

def test_a_sample_4():
    data = '(()(()('
    assert solve_a(data) == 3

def test_a_sample_5():
    data = '))((((('
    assert solve_a(data) == 3

def test_a_sample_6():
    data = '())'
    assert solve_a(data) == -1

def test_a_sample_7():
    data = '))('
    assert solve_a(data) == -1

def test_a_sample_8():
    data = ')))'
    assert solve_a(data) == -3

def test_a_sample_9():
    data = ')())())'
    assert solve_a(data) == -3

def test_a_full():
    data = load_data('full')
    assert solve_a(data[0]) == 138


def test_b_sample_1():
    data = ')'
    assert solve_b(data) == 1

def test_b_sample_2():
    data = '()())'
    assert solve_b(data) == 5

def test_b_full():
    data = load_data('full')
    assert solve_b(data[0]) == 1771


def load_data(set):
    with open(os.path.dirname(__file__) + f'/{set}.txt') as f:
        lines = f.read().splitlines()
    return lines

