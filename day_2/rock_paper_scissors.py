with open("guide.txt") as f:
    lines = f.read().splitlines()

conv = {'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3}
total_score = 0 

for line in lines:
    opponent = conv[line[0]]
    player = conv[line[2]]

    total_score += player

    if opponent == player:
        total_score += 3
    elif (player == opponent+1) or (player == (opponent % 3)+1):
        total_score += 6
    

print("ans1=%d" % total_score)

total_score = 0 

for line in lines:
    opponent = conv[line[0]]
    outcome = line[2]

    if outcome == 'X':
        player = 3 if (opponent-1==0) else opponent-1
        total_score += player
    elif outcome == 'Y':
        total_score += (3 + opponent)
    elif outcome == 'Z':
        player = 1 if (opponent+1==4) else opponent+1
        total_score += (6 + player)

    

print("ans2=%d" % total_score)