#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)

value_map = {
    "A X": 3 + 0, #Loss (Scissors)
    "A Y": 1 + 3, #Draw (Rock)
    "A Z": 2 + 6, #Win (Paper)
    "B X": 1 + 0, #Loss (Rock)
    "B Y": 2 + 3, #Draw (Paper)
    "B Z": 3 + 6, #Win (Scissors)
    "C X": 2 + 0, #Loss (Paper) 
    "C Y": 3 + 3, #Draw (Scissors)
    "C Z": 1 + 6, #Win (Rock)
}
amt = 0

if __name__ == "__main__":
    with u.open_input() as input:
        for line in input:
            amt += value_map[line.strip()]
    u.output(amt)
