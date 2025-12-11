import os
from functools import reduce
from operator import mul

def solve_a(data):
    (args, ops) = data
    res = 0
    for i in range(len(ops)):
        a = [x[i] for x in args]
        op = ops[i]
        if op == '+':
            res += sum(a)
        elif op == '*':
            res += reduce(mul, a, 1)

    return res


def solve_b(data):
    (args, ops) = data
    res = 0
    for i in range(len(ops)):
        a = args[i]
        op = ops[i]
        if op == '+':
            res += sum(a)
        elif op == '*':
            res += reduce(mul, a, 1)

    return res


def test_a_sample():
    data = load_data_a('sample')
    assert solve_a(data) == 4277556


def test_a_full():
    data = load_data_a('full')
    assert solve_a(data) == 6343365546996


def test_b_sample():
    data = load_data_b('sample')
    assert solve_b(data) == 3263827


def test_b_full():
    data = load_data_b('full')
    assert solve_b(data) == 11136895955912


def load_data_a(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    args = lines[:-1]
    ops = lines[-1]
    args = [list(map(int, a.split())) for a in args]
    ops = ops.split()

    return (args, ops)

def load_data_b(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    args_raw = lines[:-1]
    ops_raw = lines[-1]
    args = []
    ops = []

    cursor = 0
    while cursor < len(ops_raw):
        print()
        print(cursor)
        cc = cursor + 1
        while True:
            print(cc)
            if cc >= len(ops_raw):
                cc += 1
                break
            if ops_raw[cc] in '+*':
                break
            cc += 1
        new_cursor = cc
        cc -= 1
        aa = []
        for _ in range(new_cursor - cursor - 1):
            cc -= 1
            arg_raw = [l[cc] for l in args_raw]
            arg_raw = ''.join(arg_raw)
            print(arg_raw)
            arg = int(arg_raw)
            aa.append(arg)
        args.append(aa)
        ops.append(ops_raw[cursor])
        cursor = new_cursor
    return (args, ops)

