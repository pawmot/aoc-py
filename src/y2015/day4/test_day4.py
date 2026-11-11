import os
import hashlib

def solve_a(data):
    cur = 0
    while True:
        key = data + str(cur)
        res = hashlib.md5(key.encode())
        if res.hexdigest().startswith('00000'):
            return cur
        else:
            cur += 1

def solve_b(data):
    cur = 0
    while True:
        key = data + str(cur)
        res = hashlib.md5(key.encode())
        if res.hexdigest().startswith('000000'):
            return cur
        else:
            cur += 1


def test_a_sample_1():
    data = 'abcdef'
    assert solve_a(data) == 609043


def test_a_sample_2():
    data = 'pqrstuv'
    assert solve_a(data) == 1048970


def test_a_full():
    data = load_data('full')
    assert solve_a(data[0]) == 254575


def test_b_full():
    data = load_data('full')
    assert solve_b(data[0]) == 1038736


def load_data(set):
    with open(os.path.dirname(__file__) + f'/{set}.txt') as f:
        lines = f.read().splitlines()
    return lines

