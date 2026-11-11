from math import prod
import os
from functools import reduce


def solve_a(data):
    res = 0
    for d in data:
        edges = [int(s) for s in d.split('x')]
        sides = [edges[0] * edges[1], edges[1] * edges[2], edges[2] * edges[0]]
        min_side = reduce(min, sides)
        res += sum(sides) * 2 + min_side
    return res


def solve_b(data):
    res = 0
    for d in data:
        edges = [int(s) for s in d.split('x')]
        face_perim = [2 * (edges[0] + edges[1]), 2 * (edges[1] + edges[2]), 2 * (edges[2] + edges[0])]
        min_face_perim = reduce(min, face_perim)
        res += min_face_perim + prod(edges)
    return res


def test_a_sample():
    data = load_data('sample')
    assert solve_a(data) == 58 + 43


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 1588178


def test_b_sample():
    data = load_data('sample')
    assert solve_b(data) == 34 + 14


def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 3783758


def load_data(set):
    with open(os.path.dirname(__file__) + f'/{set}.txt') as f:
        lines = f.read().splitlines()
    return lines

