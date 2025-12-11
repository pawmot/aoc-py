import os
import sys

def solve_a(data):
    beams = set()
    res = 0
    for l in data:
        new_beams = set()
        for i in range(len(l)):
            if l[i] == '^' and i in beams:
                res += 1
                if i > 0:
                    new_beams.add(i-1)
                if i < len(l) - 1:
                    new_beams.add(i+1)
            elif l[i] == 'S':
                new_beams.add(i)
            elif l[i] == '.' and i in beams:
                new_beams.add(i)
        beams = new_beams

    return res


def part_solve_b(data, pos, cache):
    (r, c) = pos
    if cache[r][c] == -1:
        if data[r][c] in 'S.':
            cache[r][c] = part_solve_b(data, (r+1, c), cache)
        else: # data[r][c] = '^'
            cache[r][c] = part_solve_b(data, (r, c-1), cache) + part_solve_b(data, (r, c+1), cache)
    return cache[r][c]


def solve_b_rec(data):
    cache = [[-1 for _ in l] for l in data]
    cache[-1] = [1 for _ in cache[-1]]
    pos = (0, data[0].index('S'))
    return part_solve_b(data, pos, cache)


def solve_b(data):
    sol = [1 for _ in data[-1]]
    for r in reversed(range(len(data) - 1)):
        new_sol = []
        for c in range(len(data[r])):
            if data[r][c] in 'S.':
                new_sol.append(sol[c])
            else: # data[r][c] = '^'
                new_sol.append(sol[c-1] + sol[c+1])
        sol = new_sol
            
    return sol[data[0].index('S')]


def test_a_sample():
    data = load_data('sample')
    assert solve_a(data) == 21


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 1573


def test_b_sample():
    data = load_data('sample')
    assert solve_b(data) == 40


def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 15093663987272


def load_data(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    return lines

