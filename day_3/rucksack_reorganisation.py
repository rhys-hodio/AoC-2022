import string

alphabet= '0' + string.ascii_lowercase + string.ascii_uppercase

def get_common_item(sets):
    item = list(sets[0].intersection(sets[1]).intersection(sets[2]))
    return item[0]


with open("rucksacks.txt") as f:
    lines = f.read().splitlines()

total_priority = 0

for line in lines:
    num_items = len(line)
    compartment0 = set(line[0:num_items//2])
    compartment1 = set(line[num_items//2:])
    item = list(compartment0.intersection(compartment1))[0]
    priority = alphabet.find(item)
    total_priority += priority

print("ans1=%d" % total_priority)

total_priority = 0
elf_group_sets = []

for line in lines:
    elf_group_sets.append(set(line))
    if len(elf_group_sets) == 3:
        item = get_common_item(elf_group_sets)
        elf_group_sets = []
        priority = alphabet.find(item)
        total_priority += priority

print("ans2=%d" % total_priority)