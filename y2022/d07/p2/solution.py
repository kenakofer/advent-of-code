#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)


class Dir:
    def __init__(self):
        self.contents = {}

    def get_size(self):
        return sum( [ c.get_size() for c in self.contents.values() ] )
    
    def smallest_dir_at_least(self, min_size):
        start = 999999999999
        best = start
        size = self.get_size()
        if size < min_size:
            return start # Not big enough on its own

        # Big enough, but can we get smaller:

        for c in self.contents.values():
            if isinstance(c, Dir):
                best_contained_size = c.smallest_dir_at_least(min_size)
                if best_contained_size < best and best_contained_size >= min_size:
                    best = best_contained_size

        # If best wasn't set by a smaller directory, this directory may be the best
        if best == start:
            best = size

        return best

    def print_structure(self, prefix=""):
        for k in self.contents:
            print(f"{prefix}{k}")
            self.contents[k].print_structure(prefix + "  ")


        

class File:
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def print_structure(self, prefix=""):
        pass

MAX = 100000

def read_input_to_root(root_dir):
    path = [root_dir]

    with u.open_input() as input:
        for line in input:
            line = line.strip()
            if line.startswith("$"):
                if line.startswith("$ ls"):
                    pass
                elif line.startswith("$ cd /"):
                    path = [root_dir]
                elif line.startswith("$ cd .."):
                    path.pop()
                elif line.startswith("$ cd"):
                    name = line.split()[2]
                    if not name in path[-1].contents:
                        path[-1].contents[name] = Dir()
                    path.append(path[-1].contents[name])
            else:
                # Not a command, must be either dir or file:
                # dir lvrzvt
                # 224312 vngq 
                if line.startswith("dir"):
                    pass # Dirs are presumed to have zero size until we cd and ls it.
                else:
                    size, name = line.split()
                    size = int(size)
                    path[-1].contents[name] = File(size)

if __name__ == "__main__":
    root_dir = Dir()
    read_input_to_root(root_dir)

    total_space = 70000000
    needed =      30000000
    taken = root_dir.get_size()
    extra_needed = needed + taken - total_space
    print(f"space taken: {taken}. Need to clear {extra_needed}")

    u.output(root_dir.smallest_dir_at_least(extra_needed))




