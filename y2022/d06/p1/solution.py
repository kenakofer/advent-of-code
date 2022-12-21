#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)

LEN = 4

if __name__ == "__main__":
    with u.open_input() as input:
        char_lines = []
        for line in input:
            line = line.strip()
            for i in range(len(line)):
                if len(set(line[i:i+LEN])) == LEN:
                    u.output(i+LEN)
                    break