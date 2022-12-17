#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)

def find_bad_item_char(string):
    first_half = set(string[:len(string)//2])
    second_half = set(string[len(string)//2:])
    return first_half.intersection(second_half).pop()

def find_item_code(character):
    if character.islower():
        return ord(character) - ord('a') + 1
    else:
        return ord(character) - ord('A') + 27

if __name__ == "__main__":
    total = 0
    with u.open_input() as input:
        for line in input:
            total += find_item_code(find_bad_item_char(line.strip()))
    u.output(total)
