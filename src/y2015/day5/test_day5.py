import os
from common.iter_common import sliding_window

def solve_a(data: list[str]):
    unwanted = {'ab', 'cd', 'pq', 'xy'}
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res = 0
    for d in data:
        has_unwanted = [x in d for x in unwanted]
        if any(has_unwanted):
            continue
        no_of_vowels = 0
        has_pair = False
        prev = None
        for c in d:
            if c in vowels:
                no_of_vowels += 1
            if c == prev:
                has_pair = True
            prev = c
            if has_pair and no_of_vowels >= 3:
                print(f'{d} is nice')
                res += 1
                break
    return res


def solve_b(data: list[str]):
    res = 0
    for d in data:
        has_nonoverlapping_clones = False
        pair_to_idx = {}
        for (i, w) in enumerate(sliding_window(d, 2)):
            if w in pair_to_idx:
                if i - pair_to_idx[w] >= 2:
                    has_nonoverlapping_clones = True
                    break
            else:
                pair_to_idx[w] = i
        has_separated_pair = False
        for w in sliding_window(d, 3):
            if w[0] == w[2]:
                has_separated_pair = True
                break
        if has_nonoverlapping_clones and has_separated_pair:
            res += 1
    return res


def test_a_sample():
    data = load_data('sample_a')
    assert solve_a(data) == 2


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 255


def test_b_sample():
    data = load_data('sample_b')
    assert solve_b(data) == 2


def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 55


def load_data(set: str) -> list[str]:
    with open(os.path.dirname(__file__) + f'/{set}.txt') as f:
        lines = f.read().splitlines()
    return lines

