#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)

max_amt = 0
amt = 0

if __name__ == "__main__":
    with u.open_input() as input:
        for line in input:
            if line.strip() == "":
                if (amt > max_amt):
                    max_amt = amt
                amt = 0
            else:
                amt += int(line)
    u.output(max_amt)
