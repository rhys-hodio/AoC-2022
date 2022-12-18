with open("trees.txt") as f:
    lines = f.read().splitlines()

visible_trees = set()
trees = [list(map(int, list(line))) for line in lines]

width = len(trees[0])
height = len(trees)

max_tree_height = None
for h in range(0,height):
    for w in range(0,width):
        if max_tree_height is None or trees[h][w] > max_tree_height:
            visible_trees.add((h,w))
            max_tree_height = trees[h][w]
    max_tree_height = None

max_tree_height = None
for h in range(0,height):
    for w in range(width-1,-1,-1):
        if max_tree_height is None or trees[h][w] > max_tree_height:
            visible_trees.add((h,w))
            max_tree_height = trees[h][w]
    max_tree_height = None

max_tree_height = None
for w in range(0,width):
    for h in range(0,height):
        if max_tree_height is None or trees[h][w] > max_tree_height:
            visible_trees.add((h,w))
            max_tree_height = trees[h][w]
    max_tree_height = None

max_tree_height = None
for w in range(0,width):
    for h in range(height-1,-1,-1):
        if max_tree_height is None or trees[h][w] > max_tree_height:
            visible_trees.add((h,w))
            max_tree_height = trees[h][w]
    max_tree_height = None

print("ans1=%d" % len(visible_trees))
tree_scores = []
for tree in visible_trees:
    l_score = 0
    r_score = 0
    u_score = 0
    d_score = 0
    current_tree = trees[tree[0]][tree[1]]
    for i in range(tree[0]+1, height):
        d_score += 1
        
        if (trees[i][tree[1]] >= current_tree):
            break
    
    for i in range(tree[0]-1, -1, -1):
        u_score += 1
        if (trees[i][tree[1]] >= current_tree):
            break
        
    
    for i in range(tree[1]+1, width):
        r_score += 1
        if (trees[tree[0]][i] >= current_tree):
            break
        

    for i in range(tree[1]-1, -1, -1):
        l_score += 1
        if (trees[tree[0]][i] >= current_tree):
            break
        

    tree_scores.append(l_score*r_score*u_score*d_score)


print("ans2=%d" % max(tree_scores))