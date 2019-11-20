from collections import OrderedDict
from itertools import chain


coords = OrderedDict()


def is_dominated(x, y) -> bool:
    for key, value in coords.items():
        if x < key:
            return y < value
    return False


def remove_dominated(x, y):
    global coords
    remove_idx = []
    lower_bound_idx = None
    for idx, (key, value) in enumerate(coords.items()):
        if x > key and y > value:
            remove_idx.append(idx)
        elif x < key:
            lower_bound_idx = idx
            break
    if remove_idx:
        nondomi_before = list(coords.items())[:remove_idx[0]]
        nondomi_post = list(coords.items())[remove_idx[-1]+1:]
        new_coords = OrderedDict()
        for key, value in chain(nondomi_before, [(x,y)], nondomi_post):
            new_coords[key] = value
        coords = new_coords
    else:
        before = list(coords.items())[:lower_bound_idx]
        post = list(coords.items())[lower_bound_idx:]
        new_coords = OrderedDict()
        for key, value in chain(before, [(x, y)], post):
            new_coords[key] = value
        coords = new_coords


def registered(x, y) -> int:
    if is_dominated(x, y):
        return len(coords.keys())
    elif coords:
        remove_dominated(x, y)
    elif not coords:
        coords[x] = y
    return len(coords.keys())


nerds = [[72, 50], [57, 67], [74, 55], [64, 60]]
nerds = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]
answer = []
for nerd in nerds:
    answer.append(registered(nerd[0], nerd[1]))
    print(coords)
print(sum(answer))