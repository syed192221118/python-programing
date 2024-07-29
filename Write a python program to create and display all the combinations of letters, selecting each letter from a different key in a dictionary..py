import itertools

def combinations_from_dict(d):
    keys = list(d.keys())
    values = [d[key] for key in keys]
    return [''.join(p) for p in itertools.product(*values)]

d = {1: ['a', 'b'], 2: ['c', 'd']}
print(combinations_from_dict(d))
