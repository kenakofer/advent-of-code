#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)

def find_matched_item_char(string_list):
    matched_set = set(string_list[0])
    for string in string_list[1:]:
        matched_set.intersection_update(set(string))
    return matched_set.pop()


def find_item_code(character):
    if character.islower():
        return ord(character) - ord('a') + 1
    else:
        return ord(character) - ord('A') + 27

if __name__ == "__main__":
    total = 0
    with u.open_input() as input:
        for line in input:
            badge = find_matched_item_char([line, input.readline(), input.readline()])
            total += find_item_code(badge)
    u.output(total)
