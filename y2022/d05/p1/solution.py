#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)

def transpose_list(lists):
    return [ [lists[y][x] for y in range(len(lists))] for x in range(len(lists[0]))]

def pop_spaces(lists):
    for l in lists:
        while l[-1] == " ":
            l.pop()

if __name__ == "__main__":
    total = 0
    with u.open_input() as input:
        char_lines = []
        for line in input:
            if line == "\n":
                break
            print(line)
            char_lines.append(list(line[1::4])) # Character 1 to the end by 5, see input
        char_lines.reverse()
        print(char_lines)
        char_lines = transpose_list(char_lines)
        pop_spaces(char_lines)
        print(char_lines)

        for line in input: # Continues from the first line of the instructions
            # Example line: "move 6 from 9 to 3"
            quantity, source, dest  = map(int, line.split(" ")[1::2])
            # Source and dest are 1 indexed, fix that
            source -= 1
            dest -= 1
            # Do the pops/pushes
            for i in range(quantity):
                char_lines[dest].append(char_lines[source].pop())

    u.output(''.join( [ char_lines[x][-1] for x in range(len(char_lines)) ] ))
