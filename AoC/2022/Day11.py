""" 2022/11: Monkey in the Middle """

import collections as cl
import copy
import math
import operator
import re
import sys

def parse(expr):
    # A naive expression parser; just barely sufficient for the problem.
    lhs, op, rhs = expr.split()
    return (
      lambda x:
        (operator.add if op == "+" else operator.mul)
        (int(lhs) if lhs.isdigit() else x, int(rhs) if rhs.isdigit() else x)
    )
    
monkeys = []
for monkey in open("Day11Input.txt").read().strip().split("\n\n"):
    _, inventory, op, *test = monkey.split("\n")
    
    inventory = list(map(int, re.findall(r"\d+", inventory)))
    op = parse(op.split(" = ")[-1])
    modulus, if_true, if_false = map(int, re.findall(r"\d+", "\n".join(test)))

    monkeys.append([ inventory, (op, modulus, if_true, if_false) ])

N = math.lcm(*[monkey[1][1] for monkey in monkeys])
def play(monkeys, part2 = False):
    activity = cl.Counter()
    for _ in range(10000 if part2 else 20):
        for i, (inventory, (op, modulus, if_true, if_false)) in enumerate(monkeys):
            while len(inventory) > 0:
                item = op(inventory.pop(0)) % N
                if not part2: item //= 3
                monkeys[if_true if item % modulus == 0 else if_false][0].append(item)
                activity[i] += 1
                
    return activity.most_common()[0][1] * activity.most_common()[1][1]
            
print("Part 1:", play(copy.deepcopy(monkeys)))
print("Part 2:", play(monkeys, True))