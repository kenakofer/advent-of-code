#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)

NUM_TO_TRACK = 3

max_amts = [0] * NUM_TO_TRACK
amt = 0

if __name__ == "__main__":
    with u.open_input() as input_file:
        for line in input_file:
            if line.strip() == "":
                if (amt > max_amts[0]):
                    max_amts[0] = amt # Push out the first (lowest amount)
                    max_amts.sort() # Keep the lowest in the bottom spot
                amt = 0
            else:
                amt += int(line)
    u.output(sum(max_amts))
