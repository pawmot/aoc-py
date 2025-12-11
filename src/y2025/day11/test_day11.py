import os


def build_graph(data):
    g = {}
    for d in data:
        p = d.split(' ')
        v = p[0][:-1]
        n = p[1:]
        g[v] = n
    return g


def solve_a(data):
    g = build_graph(data)
    target = 'out'
    def count_paths(begin, cache):
        if begin == target:
            return 1
        if begin not in cache:
            cache[begin] = sum(count_paths(n, cache) for n in g[begin])
        return cache[begin]
    return count_paths('you', {})


def solve_b(data):
    g = build_graph(data)
    target = 'out'
    def count_paths(begin, visited, cache):
        if begin == target:
            return 1 if all(visited) else 0
        if (begin, visited) not in cache:
            if begin == 'fft' or begin == 'dac':
                visited = (
                    True if begin == 'fft' else visited[0],
                    True if begin == 'dac' else visited[1]
                )
            cache[(begin, visited)] = sum(count_paths(n, visited, cache) for n in g[begin])
        return cache[(begin, visited)]
    return count_paths('svr', (False, False), {})


def test_a_sample():
    data = load_data('sampleA')
    assert solve_a(data) == 5


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 674


def test_b_sample():
    data = load_data('sampleB')
    assert solve_b(data) == 2


def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 438314708837664


def load_data(set):
    lines = open(os.path.dirname(__file__) + f'/{set}.txt').read().splitlines()
    return lines

