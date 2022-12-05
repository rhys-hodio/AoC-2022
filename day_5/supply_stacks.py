import re
import copy 

with open("stacks.txt") as f:
    lines = f.read().splitlines()

stacks = [[] for i in range(9)]

for line in lines:
    if re.match(r".*[0-9].*", line):
        break
    for i in range(9):
        obj = line[1 + (i*4)]
        if obj != " ":
            stacks[i].insert(0, obj)

stacks_copy = copy.deepcopy(stacks)

for line in lines:
    match = re.match(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", line)
    if match:
        amount = int(match.group(1))
        from_stack = int(match.group(2))-1
        to_stack = int(match.group(3))-1
        for i in range(amount):
            item = stacks[from_stack].pop(-1)
            stacks[to_stack].append(item)

tops = ""
for stack in stacks:
    tops += stack[-1]

print("ans1=%s" % tops)

for line in lines:
    match = re.match(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", line)
    if match:
        amount = int(match.group(1))
        from_stack = int(match.group(2))-1
        to_stack = int(match.group(3))-1
        multi_stack = []
        for i in range(amount):
            item = stacks_copy[from_stack].pop(-1)
            multi_stack.insert(0, item)
        stacks_copy[to_stack] =  stacks_copy[to_stack] + multi_stack

tops = ""
for stack in stacks_copy:
    tops += stack[-1]

print("ans2=%s" % tops)