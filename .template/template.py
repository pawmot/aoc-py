import os

def solve_a(data):
    pass


def solve_b(data):
    pass


def test_a_sample():
    data = load_data('sample')
    assert solve_a(data) == 0


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 0


def test_b_sample():
    data = load_data('sample')
    assert solve_b(data) == 0


def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 0


def load_data(set: str):
    with open(os.path.dirname(__file__) + f'/{set}.txt') as f:
        lines = f.read().splitlines()
    return lines

