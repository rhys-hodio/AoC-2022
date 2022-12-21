height_key = 'SabcdefghijklmnopqrstuvwxyzE'

with open("height_map.txt") as f:
    lines = f.read().splitlines()

map_width = len(lines[0])
map_height = len(lines)
map_heights = {}
start_idx = 0
end_idx = 0

for i, line in enumerate(lines):
    for j, letter in enumerate(line):
        idx = i*map_width + j
        if letter == 'S':
            start_idx = idx
        elif letter == 'E':
            end_idx = idx
        map_heights[idx] = height_key.index(letter)

def get_neighbours_uphill(idx, map):
    potential_neighbours = []
    if (idx+1) % map_width != 0:
        potential_neighbours.append(idx+1)
    if idx % map_width != 0:
        potential_neighbours.append(idx-1)
    if idx >= map_width:
        potential_neighbours.append(idx-map_width)
    if idx < (map_width*map_height)-map_width:
        potential_neighbours.append(idx+map_width)

    neighbours = [n for n in potential_neighbours if (map_heights[n]-map_heights[idx]) <= 1]
    return neighbours

def get_neighbours_downhill(idx, map):
    potential_neighbours = []
    if (idx+1) % map_width != 0:
        potential_neighbours.append(idx+1)
    if idx % map_width != 0:
        potential_neighbours.append(idx-1)
    if idx >= map_width:
        potential_neighbours.append(idx-map_width)
    if idx < (map_width*map_height)-map_width:
        potential_neighbours.append(idx+map_width)

    neighbours = [n for n in potential_neighbours if (map_heights[n]-map_heights[idx]) >= -1]
    return neighbours

def heuristic(a, b):
   # Manhattan distance on a square grid
   a_x = a % map_height
   b_x = b % map_height
   a_y = a // map_width
   b_y = b // map_width
   return abs(a_x - b_x) + abs(a_y - b_y)

frontier = []
frontier.append(start_idx)
came_from = dict()
cost_so_far = dict()
came_from[start_idx] = None
cost_so_far[start_idx] = 0

while not len(frontier) == 0:
    current = frontier.pop(0)

    if current == end_idx: 
        break           

    for n in get_neighbours_uphill(current, map_heights):
        new_cost = cost_so_far[current] + 1 #graph.cost(current, next)
        if n not in cost_so_far or new_cost < cost_so_far[n]:
            cost_so_far[n] = new_cost
            priority = new_cost + heuristic(end_idx, n)
            frontier.insert(priority, n)
            came_from[n] = current

current = end_idx 
path = []
while current != start_idx: 
   path.append(current)
   current = came_from[current]
path.reverse() # optional



for i, line in enumerate(lines):
    new_line = ''
    for j, letter in enumerate(line):
        idx = i*map_width + j
        if idx in path:
            new_line += '#'
        else:
            new_line += letter
    print(new_line)

print("ans1=%d" % len(path))




frontier = []
frontier.append(end_idx)
came_from = dict()
cost_so_far = dict()
came_from[end_idx] = None
cost_so_far[end_idx] = 0
last_idx = 0
while not len(frontier) == 0:
    current = frontier.pop(0)

    if map_heights[current] == 1:
        last_idx = current 
        break           

    for n in get_neighbours_downhill(current, map_heights):
        new_cost = cost_so_far[current] + 1 #graph.cost(current, next)
        if n not in cost_so_far or new_cost < cost_so_far[n]:
            cost_so_far[n] = new_cost
            priority = new_cost + heuristic(end_idx, n)
            frontier.insert(priority, n)
            came_from[n] = current

current = last_idx 
path = []
while current != end_idx: 
   path.append(current)
   current = came_from[current]
   print(path)
path.reverse() # optional



for i, line in enumerate(lines):
    new_line = ''
    for j, letter in enumerate(line):
        idx = i*map_width + j
        if idx in path:
            new_line += '#'
        else:
            new_line += letter
    print(new_line)

print("ans2=%d" % len(path))