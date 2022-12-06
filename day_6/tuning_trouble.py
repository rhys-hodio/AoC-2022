with open("stream.txt") as f:
    lines = f.read().splitlines()

stream = lines[0]

i = 0;
while True:
    snippet = stream[i:i+4]
    if len(list(set(snippet))) == 4:
        print("ans1=%d" % (i+4))
        break
    i += 1

i = 0;
while True:
    snippet = stream[i:i+14]
    if len(list(set(snippet))) == 14:
        print("ans2=%d" % (i+14))
        break
    i += 1