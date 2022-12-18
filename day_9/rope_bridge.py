import re

with open("motions.txt") as f:
    lines = f.read().splitlines()

def print_diagram(rope):
    # max_x = max([h_pos[0], t_pos[0]])
    # max_y = max([h_pos[1], t_pos[1]])
    # if max_x <= 5:
    #     max_x = 5
    # if max_y <= 5:
    #     max_y = 5
    max_x = 25
    max_y = 25
    for y in range(max_y-1, -1, -1):
        line_p = ''
        for x in range(0, max_x):
            str_ = '. '
            for i in range(len(rope)-1, -1, -1):
                if [x,y] == rope[i]:
                    str_ = str(i) + ' '
            line_p += str_
        print(line_p)
    print("")

def adjust(pos0, pos1):
    x_diff = pos0[0] - pos1[0]
    y_diff = pos0[1] - pos1[1]

    if abs(x_diff) == 2 and  abs(y_diff) == 2:
        if x_diff > 0 and y_diff > 0:
            pos1[0] += 1
            pos1[1] += 1
        elif x_diff > 0 and y_diff < 0:
            pos1[0] += 1
            pos1[1] -= 1
        elif x_diff < 0 and y_diff > 0:
            pos1[0] -= 1
            pos1[1] += 1
        elif x_diff < 0 and y_diff < 0:
            pos1[0] -= 1
            pos1[1] -= 1     
    else:    

        if abs(x_diff) == 2:
            if x_diff > 0:
                pos1[0] += 1
                pos1[1] = pos0[1]
            elif x_diff < 0:
                pos1[0] -= 1
                pos1[1] = pos0[1]
        
        if abs(y_diff) == 2:
            if y_diff > 0:
                pos1[1] += 1
                pos1[0] = pos0[0]
            elif y_diff < 0:
                pos1[1] -= 1
                pos1[0] = pos0[0]


rope = [[0, 0] for i in range(2)]
t_positions = set()

for line in lines:
    match = re.match(r"^([A-Z]) ([0-9]+)$", line)
    direction = match.group(1)
    amount = int(match.group(2))
    for i in range(0, amount):
        if direction == 'L':
            rope[0][0] -= 1
        if direction == 'R':
            rope[0][0] += 1
        if direction == 'U':
            rope[0][1] += 1
        if direction == 'D':
            rope[0][1] -= 1

        for j in range(len(rope)-1):
            adjust(rope[j], rope[j+1])

        t_positions.add((rope[-1][0],rope[-1][1]))
        
print("ans1=%d" % len(t_positions))

rope = [[0, 0] for i in range(10)]
t_positions = set()

for line in lines:
    match = re.match(r"^([A-Z]) ([0-9]+)$", line)
    direction = match.group(1)
    amount = int(match.group(2))
    for i in range(0, amount):
        if direction == 'L':
            rope[0][0] -= 1
        if direction == 'R':
            rope[0][0] += 1
        if direction == 'U':
            rope[0][1] += 1
        if direction == 'D':
            rope[0][1] -= 1

        for j in range(len(rope)-1):
            adjust(rope[j], rope[j+1])

        t_positions.add((rope[-1][0],rope[-1][1]))
        #print_diagram(rope)
        
print("ans2=%d" % len(t_positions))

