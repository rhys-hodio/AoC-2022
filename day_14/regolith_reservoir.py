with open("cave.txt") as f:
    lines = f.read().splitlines()

cave = set()

for line in lines:
    points = line.split(' -> ')
    for i in range(len(points)-1):
        x0, y0 = map(int, points[i].split(','))
        x1, y1 = map(int, points[i+1].split(','))
        if x0 == x1:
            diff = y1-y0
            if diff > 0:
                for j in range(y0, y1+1):
                    cave.add((x0, j))
            elif diff < 0:
                for j in range(y0, y1-1, -1):
                    cave.add((x0, j))

        elif y0 == y1:
            diff = x1-x0
            if diff > 0:
                for j in range(x0, x1+1):
                    cave.add((j, y0))
            elif diff < 0:
                for j in range(x0, x1-1, -1):
                    cave.add((j, y0))


def print_cave(cave):
    xs = [x[0] for x in list(cave)]
    max_x = max(xs)
    min_x = min(xs)
    ys = [y[1] for y in list(cave)]
    max_y = max(ys)
    for y in range(max_y+1):
        l = ''
        for x in range(min_x, max_x+1):
            if (x,y) in cave:
                l += '#'
            else:
                l += '.'
        print(l)

print_cave(cave)

ys = [y[1] for y in list(cave)]
max_y = max(ys)
sand_coord = [500, 0]
count = 0
while True:
    
    sand_coord_down = (sand_coord[0], sand_coord[1]+1)
    sand_coord_down_occupied = sand_coord_down in cave or sand_coord[1]+1 == max_y+2
    sand_coord_left = (sand_coord[0]-1, sand_coord[1]+1)
    sand_coord_left_occupied = sand_coord_left in cave or sand_coord[1]+1 == max_y+2
    sand_coord_right = (sand_coord[0]+1, sand_coord[1]+1) 
    sand_coord_right_occupied = sand_coord_right in cave or sand_coord[1]+1 == max_y+2
    if not sand_coord_down_occupied:
        sand_coord = sand_coord_down
    elif not sand_coord_left_occupied:
        sand_coord = sand_coord_left
    elif not sand_coord_right_occupied:
        sand_coord = sand_coord_right
    else:
        count += 1
        if (sand_coord == [500, 0]):
            break
        cave.add(sand_coord)
        
        sand_coord = [500, 0]

print_cave(cave)
print("ans1=%d" % count)


