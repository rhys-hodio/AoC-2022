import ast

with open("packets.txt") as f:
    lines = f.read().splitlines()

def evaluate(l, r):
    if type(l)==int and type(r) == int:
        
        if l < r:
            return 1
        elif l > r:
            return 0
        else:
            return None

    elif type(l)==list and type(r) == list:
        

        for i in range(max(len(l), len(r))):
            if len(l) == i and len(r) > i:
                return 1
            elif len(l) > i and len(r) == i:
                return 0
            elif len(l) == i and len(r) == i:
                return None
            else:
                p = evaluate(l[i], r[i])
                if p is None:
                    continue
                else:
                    return p
        return None

    else:
        if type(l)==int:
            new_l = [l]
            return evaluate(new_l, r)
        else:
            new_r = [r]
            return evaluate(l, new_r)




array = []
pairs = {}
pair_idx = 1
pair0=None
pair1=None
for line in lines:
    if line ==  '':
        pairs[pair_idx]={}
        pairs[pair_idx]["pair0"] = pair0
        pairs[pair_idx]["pair1"] = pair1
        pair0=None
        pair1=None
        pair_idx += 1
    elif pair0 is None:
        pair0 = ast.literal_eval(line)
        array.append(ast.literal_eval(line))
    elif pair1 is None:
        pair1 = ast.literal_eval(line)
        array.append(ast.literal_eval(line))

pairs[pair_idx]={}
pairs[pair_idx]["pair0"] = pair0
pairs[pair_idx]["pair1"] = pair1

total = 0
for key, value in pairs.items():
    in_order = evaluate(value["pair0"], value["pair1"])
    if in_order:
        total += key

print("ans1=%d" % total)

array.append([[6]])
array.append([[2]])
n = len(array)

for i in range(n):

    # Create a flag that will allow the function to
    # terminate early if there's nothing left to sort
    already_sorted = True

    # Start looking at each item of the list one by one,
    # comparing it with its adjacent value. With each
    # iteration, the portion of the array that you look at
    # shrinks because the remaining items have already been
    # sorted.
    for j in range(n - i - 1):
        if not evaluate(array[j], array[j + 1]):
            # If the item you're looking at is greater than its
            # adjacent value, then swap them
            array[j], array[j + 1] = array[j + 1], array[j]

            # Since you had to swap two elements,
            # set the `already_sorted` flag to `False` so the
            # algorithm doesn't finish prematurely
            already_sorted = False

    # If there were no swaps during the last iteration,
    # the array is already sorted, and you can terminate
    if already_sorted:
        break

decoder_key = (array.index([[6]])+1)*(array.index([[2]])+1)
print("ans2=%d" % decoder_key)