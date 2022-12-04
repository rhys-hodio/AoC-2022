import re

with open("assignments.txt") as f:
    lines = f.read().splitlines()

total_lines_fully_contain = 0
total_lines_overlap = 0

for line in lines:
    match = re.match(r"([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)", line)
    range0_min = int(match.group(1))
    range0_max = int(match.group(2))
    range1_min = int(match.group(3))
    range1_max =int( match.group(4))
    if (range0_min >= range1_min and range0_max <= range1_max) or (range1_min >= range0_min and range1_max <= range0_max):
        total_lines_fully_contain += 1

    if (range0_min >= range1_min and range0_min <= range1_max) or (range1_min >= range0_min and range1_min <= range0_max):
        total_lines_overlap += 1

print("ans1=%d" % total_lines_fully_contain)
print("ans2=%d" % total_lines_overlap)