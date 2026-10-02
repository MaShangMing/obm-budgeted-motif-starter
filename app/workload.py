"""Public synthetic device graph families; no solver or expected answers."""
import random

def cycle_case(width=32, depth=8, seed=0):
    randomizer = random.Random(seed)
    names = [[f'h{level:02}_{i:03}' for i in range(width)] for level in range(depth)]
    shifts = [randomizer.randrange(width) for _ in range(depth-1)]
    shifts.append((-sum(shifts)) % width)
    host_nodes = [{'id': names[l][i], 'kind': f'k{l}', 'zone': 'shared',
                   'cost': randomizer.randrange(100)} for l in range(depth) for i in range(width)]
    host_edges = [{'from': names[l][i], 'to': names[(l+1)%depth][(i+shifts[l])%width],
                   'label': f'wire{l}'} for l in range(depth) for i in range(width)]
    pattern_nodes = [{'id': f'p{l:02}', 'kinds': [f'k{l}'], 'demand': 1} for l in range(depth)]
    pattern_edges = [{'from': f'p{l:02}', 'to': f'p{(l+1)%depth:02}', 'label': f'wire{l}'}
                    for l in range(depth)]
    return {'host': {'nodes': host_nodes, 'edges': host_edges},
            'pattern': {'nodes': pattern_nodes, 'edges': pattern_edges},
            'domains': {f'p{l:02}': list(reversed(names[l])) for l in range(depth)},
            'capacities': {'shared': depth}}

def capacity_case(width=32, depth=8, seed=0):
    case = cycle_case(width, depth, seed)
    case['host']['edges'] = []
    case['pattern']['edges'] = []
    case['capacities']['shared'] = depth-1
    return case
