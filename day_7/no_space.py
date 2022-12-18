import re

with open("files.txt") as f:
    lines = f.read().splitlines()

class Node:
    def __init__(self, name, parent, is_file, size):
        self.children = []
        self.is_file = is_file
        self.size = size
        self.parent = parent
        self.name = name
        self.dir_sizes = []

    def get_child(self, name):
        child = [x for x in self.children if x.name == name]
        if len(child) > 1:
            raise Exception("Child length error")
        else:
            return child[0]
    
    def get_parent(self):
        return self.parent
    
    def get_size(self):
        if self.is_file:
            return self.size
        else:
            sizes = [x.get_size() for x in self.children]
            return sum(sizes)
    
    def get_dir_sizes(self):
        for child in self.children:
            if not child.is_file:
                self.dir_sizes.append(child.get_size())
                self.dir_sizes += child.get_dir_sizes()
        return self.dir_sizes

dirs = 0
in_output_mode = 0
root = Node("/", None, False, None)
current_node = root
for line in lines[1:]:
    if in_output_mode and not re.match("^\$", line):
        if p := re.match("^dir (.+)$", line): 
            dirs += 1
            n = Node(p.group(1), current_node, False, None)
            current_node.children.append(n)
        elif p := re.match("^([0-9]+) (.+)$", line):
            n = Node(p.group(2), current_node, True, int(p.group(1)))
            current_node.children.append(n) 
        else:
            raise Exception("shouldn't be here")
    else:
        in_output_mode = 0
        if p := re.match("^\$ cd (.+)$", line):
            if p.group(1) == "..":
                current_node = current_node.get_parent()
            else:
                current_node = current_node.get_child(p.group(1))

        elif re.match("^\$ ls$", line):
            in_output_mode = 1

root.get_dir_sizes()

dir_sizes_sum = 0
for size in root.dir_sizes:
    if size <= 100000:
        dir_sizes_sum += size

print("ans1=%d" % dir_sizes_sum)

free_up = root.get_size()-40000000

candidates = []
for size in root.dir_sizes:
    if size >= free_up:
        candidates.append(size)

print("ans2=%d" % min(candidates))