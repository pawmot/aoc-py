import os
from math import sqrt
from itertools import product


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sizes = [1] * n

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def size(self, n):
        return self.sizes[self.find(n)]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.parent[pa] = pb
            self.sizes[pb] += self.sizes[pa]


def dist(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)


def solve_a(data):
    (boxes, conns) = data
    pairs = [p for p in product(range(len(boxes)), repeat = 2) if p[0] < p[1]]
    pairs.sort(key = lambda p: dist(boxes[p[0]], boxes[p[1]]))
    uf = UnionFind(len(boxes))
    for i in range(conns):
        uf.union(pairs[i][0], pairs[i][1])

    sets = {}
    for i in range(len(boxes)):
        p = uf.find(i)
        if p not in sets:
            sets[p] = 0
        sets[p] += 1

    sizes = list(sets.values())
    sizes.sort(reverse = True)
    return sizes[0] * sizes[1] * sizes[2]


def solve_b(boxes):
    pairs = [p for p in product(range(len(boxes)), repeat = 2) if p[0] < p[1]]
    pairs.sort(key = lambda p: dist(boxes[p[0]], boxes[p[1]]))
    uf = UnionFind(len(boxes))
    for i in range(len(pairs)):
        uf.union(pairs[i][0], pairs[i][1])
        s = uf.size(0)
        if s == len(boxes):
            return boxes[pairs[i][0]][0] * boxes[pairs[i][1]][0]


def test_a_sample():
    data = load_data('sample')
    assert solve_a((data, 10)) == 40


def test_a_full():
    data = load_data('full')
    assert solve_a((data, 1000)) == 181584


def test_b_sample():
    data = load_data('sample')
    assert solve_b(data) == 25272


def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 8465902405


def load_data(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    data = [[int(c) for c in l.split(',')] for l in lines]
    return data

