import re

with open("instructions.txt") as f:
    lines = f.read().splitlines()

reg_x = 1
cycle = 1
signal_strength_sum = 0


for line in lines:
    
    if line == 'noop':
        if (cycle-20) % 40 == 0 and cycle <= 220:
            signal_strength_sum += (cycle*reg_x)
        cycle += 1
    elif p := re.match(r"^addx (.+)$", line):
        val = int(p.group(1))
        if (cycle-20) % 40 == 0 and cycle <= 220:
            signal_strength_sum += (cycle*reg_x)
        cycle += 1
        if (cycle-20) % 40 == 0 and cycle <= 220:
            signal_strength_sum += (cycle*reg_x)
        cycle += 1
        reg_x += val

print("ans1=%d" % signal_strength_sum)

reg_x = 1
cycle = 1
crt_line = ''
crt_lines_written = 0
for line in lines:
    if line == 'noop':
        if(cycle % 40) in [reg_x, reg_x+1, reg_x+2]:
            crt_line += '# '
        else:
            crt_line += '. '
        if (cycle // 40) > crt_lines_written:
            print(crt_line)
            crt_line = ''
            crt_lines_written += 1
        cycle += 1
        
    elif p := re.match(r"^addx (.+)$", line):
        val = int(p.group(1))
        if (cycle % 40) in [reg_x, reg_x+1, reg_x+2]:
            crt_line += '# '
        else:
            crt_line += '. '
        if (cycle // 40) > crt_lines_written:
            print(crt_line)
            crt_line = ''
            crt_lines_written += 1
        cycle += 1

        if (cycle % 40) in [reg_x, reg_x+1, reg_x+2]:
            crt_line += '# '
        else:
            crt_line += '. '
        if (cycle // 40) > crt_lines_written:
            print(crt_line)
            crt_line = ''
            crt_lines_written += 1
        cycle += 1

        reg_x += val


#print("ans1=%d" % signal_strength_sum)
