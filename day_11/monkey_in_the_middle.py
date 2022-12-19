import parser
import re
from functools import reduce

def lcm(a, b):
    return (a * b) 

class Monkey:
    
    def __init__(self, start_items, op, test_int, true_monkey, false_monkey):
        self.items = start_items
        self.op = op
        self.test_int = test_int
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.items_inspected = 0

    def do(self):
        item = self.items.pop(0)
        self.items_inspected += 1      
        old = item
        item = eval(parser.expr(self.op).compile())
        #item = item // 3
        if (item % self.test_int) == 0:
            return item, self.true_monkey
        else:
            return item, self.false_monkey  

class KeepAway:

    def __init__(self):
        self.monkies = []

    def new_monkey(self, monkey):
        self.monkies.append(monkey)

    def do_round(self):
        for monkey in self.monkies:
            while len(monkey.items) > 0:
                thrown_item, monkey_idx = monkey.do()
                lcm_ = reduce(lcm, self.get_monkey_divisors())
                thrown_item = thrown_item % lcm_
                self.monkies[monkey_idx].items.append(thrown_item)
        #self.print_round_info()
    
    def get_monkey_divisors(self):
        return [monkey.test_int for monkey in self.monkies]


    def print_round_info(self):
       for i, monkey in enumerate(self.monkies):
            print("Monkey %d: %s" % (i, monkey.items))

    def print_inspections(self):
       for i, monkey in enumerate(self.monkies):
            print("Monkey %d inspected items %d times" % (i, monkey.items_inspected))
    
    def calculate_monkey_business(self):
        items_inspected_per_monkey = []
        for monkey in self.monkies:
            items_inspected_per_monkey.append(monkey.items_inspected)
        items_inspected_per_monkey.sort()
        return items_inspected_per_monkey[-1]*items_inspected_per_monkey[-2]



with open("monkies.txt") as f:
    lines = f.read().splitlines()

game = KeepAway()

start_items = [] 
op = '' 
test_int = 0 
true_monkey = 0
false_monkey = 0
for line in lines:
    
    if p := re.match(r"^\s+Starting items: (.+)$", line):
        start_items = list(map(lambda x: int(x.strip()), p.group(1).split(',')))
    elif p := re.match(r"^\s+Operation: new = (.+)$", line):
        op = p.group(1)
    elif p := re.match(r"^\s+Test: divisible by ([0-9]+)$", line):
        test_int = int(p.group(1))
    elif p := re.match(r"^\s+If true: throw to monkey ([0-9]+)$", line):
        true_monkey = int(p.group(1))
    elif p := re.match(r"^\s+If false: throw to monkey ([0-9]+)$", line):
        false_monkey = int(p.group(1))
    elif re.match("Monkey", line):
        pass
    else:
        monkey = Monkey(start_items, op, test_int, true_monkey, false_monkey)
        game.new_monkey(monkey)

for i in range(10000):
    print(i)
    game.do_round()
game.print_inspections()

print("ans1=%d" % game.calculate_monkey_business())

