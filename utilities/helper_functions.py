"""Really, we may not need to use these because of random.choice(), but here they are.

Pick one many times and pick on from nested may still be useful. 

I'd like to completely remove pick one from my code. 
"""

from random import randint, choice

"""
def pick_one_many_times(item):
    while True:
        if type(item) not in [tuple, list]:
            return item
        else:
            item=choice(item)
"""

"""
def pick_one_from_nested(item):
    while True:
        if type(item) not in [tuple, list]:
            return item
        else:
            item=choice(item)
"""

def pick_one_many_times(item, depth = None):
    if depth is None:
        while True:
            if type(item) not in [tuple, list]:
                return item
            else:
                item=choice(item)
    else:
        for i in range(depth):
            item = choice(item)
        return item


def pick_one_from_nested(item, depth = None):
    if depth is None:
        while True:
            if type(item) not in [tuple, list]:
                return item
            else:
                item=choice(item)
    else:
        for i in range(depth):
            item = choice(item)
        return item


def pick_one(item):
    item = item[randint(0, len(item)-1)]
    return item