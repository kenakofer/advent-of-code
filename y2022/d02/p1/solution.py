#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)

value_map = {
    "A X": 1 + 3, #Draw
    "A Y": 2 + 6, #Win
    "A Z": 3 + 0, #Loss
    "B X": 1 + 0, #Loss
    "B Y": 2 + 3, #Draw
    "B Z": 3 + 6, #Win
    "C X": 1 + 6, #Win
    "C Y": 2 + 0, #Loss
    "C Z": 3 + 3, #Draw
}
amt = 0

if __name__ == "__main__":
    with u.open_input() as input:
        for line in input:
            amt += value_map[line.strip()]
    u.output(amt)
