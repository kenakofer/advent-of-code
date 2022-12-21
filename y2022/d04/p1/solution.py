#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)

from re import split

def is_fully_contained(a1, a2, b1, b2):
    return (a1 <= b1 and b2 <= a2) or (b1 <= a1 and a2 <= b2)

if __name__ == "__main__":
    total = 0
    with u.open_input() as input:
        for line in input:
            args = map(int, split(',|-', line.strip()))
            total += is_fully_contained(*args)
    u.output(total)
