import os

def solveA(lines):
    [l.max() for l in lines]
    pass

def loadData(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    return [
        [int(char) for char in line] 
        for line in lines
    ]

def test_a_sample():
    dataset = loadData('sample')
    assert solveA(dataset) == 357
