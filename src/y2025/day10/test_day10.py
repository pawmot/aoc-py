import os
from itertools import chain, combinations
from functools import reduce
import queue
from math import isclose


def indicator_to_int(indicator):
    return sum(map(lambda s: 2**s[0], filter(lambda p: p[1] == '#', enumerate(indicator[1:-1]))))


def button_to_int(button):
    return sum(map(lambda s: 2**s, map(int, button[1:-1].split(','))))


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def solve_a(data):
    res = 0
    for (ind, btns, _) in data:
        ind = indicator_to_int(ind)
        btns = list(map(button_to_int, btns))
        min_len = reduce(
            lambda m, bs: min(m, len(bs)) if ind == reduce(lambda a, c: a ^ c, bs, 0) else m,
            powerset(btns),
            1000
        )
        res += min_len
    return res


def printMatrix(m):
    for r in m:
        print(r)
    print()


def createAugmentedMatrix(btns, jlt):
    n = len(jlt)
    m = len(btns) + 1
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m - 1):
            if i in btns[j]:
                res[i][j] = 1
        res[i][m-1] = jlt[i]
    return res


def solveLinearSystem(am):
    n = len(am)
    m = len(am[0])
    dependent = []
    cur_col = 0
    cur_row = 0
    while cur_row < n and cur_col < m - 1:
        free = True
        for i in range(cur_row, n):
            if am[i][cur_col] != 0:
                # swap rows
                am[cur_row], am[i] = am[i], am[cur_row]
                free = False
                break
        if free:
            cur_col += 1
            continue
        dependent.append(cur_col)
        # normalize
        factor = am[cur_row][cur_col]
        am[cur_row] = list(map(lambda x: x / factor, am[cur_row]))
        # eliminate
        for i in range(n):
            if i == cur_row:
                continue
            if am[i][cur_col] != 0:
                factor = am[i][cur_col]
                am[i] = list(map(lambda x, y: x - factor * y, am[i], am[cur_row]))
        cur_row += 1
        cur_col += 1


    free = list(filter(lambda x: x not in dependent, range(m - 1)))
    return (am, dependent, free)


def solve_b(data):
    res = 0
    ix = 0
    for (_, btns, jlt) in data:
        jlt = list(map(int, jlt[1:-1].split(',')))
        btns = [list(map(int, b[1:-1].split(','))) for b in btns]
        am = createAugmentedMatrix(btns, jlt)
        am, dependent, free = solveLinearSystem(am)
        q = queue.Queue()
        q.put([0] * len(free))
        min_press = 10000500000
        visited = set()
        # print(f'Doing case {ix}')
        found_better = 0
        while not q.empty():
            cur = q.get()
            if tuple(cur) in visited:
                continue
            visited.add(tuple(cur))
            state = [0.0] * len(btns)
            for i in range(len(state)):
                if i in free:
                    idx = free.index(i)
                    state[i] = cur[idx]
                else:
                    idx = dependent.index(i)
                    r = am[idx][-1]
                    for (fi, f) in enumerate(free):
                        r -= am[idx][f] * cur[fi] 
                    state[i] = r

            # print(f'{state}: {round(sum(state))}')
            # print(f'Queue size: {q.qsize()}, visited size: {len(visited)}, min_press: {min_press}, found better: {found_better}', end='\r')
            # if any(s < -50 for s in state):
            #     continue

            if all(round(s) >= 0 for s in state) and all(isclose(s, round(s), abs_tol=1e-9) for s in state) and sum(state) < min_press:
                # print(f'{state}: {int(sum(state))}')
                min_press = round(sum(state))
                found_better += 1

            # if sum(state) > 1000:
            #     continue

            for i in range(len(cur)):
                next = cur[:]
                next[i] += 1
                next_state = [0.0] * len(btns)
                for i in range(len(next_state)):
                    if i in free:
                        idx = free.index(i)
                        next_state[i] = next[idx]
                    else:
                        idx = dependent.index(i)
                        r = am[idx][-1]
                        for (fi, f) in enumerate(free):
                            r -= am[idx][f] * next[fi] 
                        next_state[i] = r
                if any(v[0] < v[1] and v[0] < -1 for v in zip(next_state, state)):
                    continue
                q.put(next)
        # if found_better == 0:
        #     print(f'--- Case {ix} --- dependent: {dependent}, free: {free}')
        #     print(f'Min presses for case: {min_press}, found better times {found_better}')
        ix += 1
        res += int(min_press)
    return res


def test_a_sample():
    data = load_data('sample')
    assert solve_a(data) == 7


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 385


def test_b_sample():
    data = load_data('sample')
    assert solve_b(data) == 33
#
#
def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 16757


def load_data(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    data = [l.split(' ') for l in lines]
    data = [(d[0], d[1:-1], d[-1]) for d in data]
    return data

