import os

def solve_a(data):
    (_, spaces) = data
    spaces = [s.split(": ") for s in spaces]
    spaces = [(list(map(int, s[0].split("x"))), list(map(int, s[1].split(" ")))) for s in spaces]
    f = filter(lambda s: s, (s[0][0]*s[0][1] >= 9 * sum(s[1]) for s in spaces))
    return sum(1 for _ in f)


def solve_b(data):
    pass


def test_a_sample():
    data = load_data('sample')
    assert solve_a(data) == 0


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 0


# def test_b_sample():
#     data = load_data('sample')
#     assert solve_b(data) == 0
#
#
# def test_b_full():
#     data = load_data('full')
#     assert solve_b(data) == 0


def load_data(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    idx = 0
    shapes = []
    while lines[idx][-1] == ':':
        idx += 1
        shape = []
        while lines[idx] != '':
            shape.append(lines[idx])
            idx += 1
        shapes.append(shape)
        idx += 1
    spaces = lines[idx:]
    return (shapes, spaces)

