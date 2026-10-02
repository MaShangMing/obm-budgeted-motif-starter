"""Small placement baseline: enumerate domain products and return the first match."""
from itertools import product

def solve(document):
    host = {v['id']: v for v in document['host']['nodes']}
    pattern = {v['id']: v for v in document['pattern']['nodes']}
    order = sorted(pattern)
    links = {(e['from'], e['to']): e['label'] for e in document['host']['edges']}
    for values in product(*(document['domains'][p] for p in order)):
        if len(set(values)) != len(values):
            continue
        mapping = dict(zip(order, values))
        if any(host[mapping[p]]['kind'] not in pattern[p]['kinds'] for p in order):
            continue
        if any(links.get((mapping[e['from']], mapping[e['to']])) != e['label']
               for e in document['pattern']['edges']):
            continue
        return {'count': 1, 'min_cost': sum(host[h]['cost'] for h in values),
                'witness': mapping}
    return {'count': 0, 'min_cost': None, 'witness': None}
