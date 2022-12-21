#!/usr/bin/env python3
from ...common import utils as u
u.init_file_paths(__file__)


class Dir:
    def __init__(self):
        self.contents = {}

    def get_size(self):
        return sum( [ c.get_size() for c in self.contents.values() ] )
    
    def get_sum_children_lt_max(self, max_size):
        total = 0
        for c in self.contents.values():
            if isinstance(c, Dir):
                total += c.get_sum_children_lt_max(max_size)
        if self.get_size() <= max_size:
            total += self.get_size()
        return total

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

    # root_dir.print_structure()
    u.output(root_dir.get_sum_children_lt_max(MAX))




