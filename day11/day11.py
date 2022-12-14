from copy import deepcopy
import math

def simulate_monkeys(monkeys, rounds, relief):
  cycle_length = math.prod(m["divisible"] for m in monkeys)
  for _ in range(rounds):
    for monkey in monkeys:
      for old in monkey["items"]:
        old %= cycle_length
        item = eval(monkey["operation"])
        if relief:
          item //= 3
        target_monkey = monkey["true_monkey"] if item % monkey["divisible"] == 0 else monkey["false_monkey"]
        monkeys[target_monkey]["items"].append(item)
        monkey["items_inspected"] += 1
      monkey["items"] = []

  top_monkeys = sorted([m["items_inspected"] for m in monkeys], reverse=True)
  return top_monkeys[0] * top_monkeys[1]

monkeys = [] # [{items: []int, operation: str, divisible: int, true_monkey: int, false_monkey: int, items_inspected: int}, ...]

with open("input/day11.txt") as f:
  monkey_blocks = f.read().split("\n\n")
for monkey_block in monkey_blocks:
  monkey_lines = monkey_block.splitlines()
  monkey = {}
  items_string = monkey_lines[1][monkey_lines[1].index(":")+1:]
  monkey["items"] = list(map(int, items_string.split(",")))
  monkey["operation"] = monkey_lines[2][monkey_lines[2].index("=")+2:]
  monkey["divisible"] = int(monkey_lines[3].split(" ")[-1])
  monkey["true_monkey"] = int(monkey_lines[4].split(" ")[-1])
  monkey["false_monkey"] = int(monkey_lines[5].split(" ")[-1])
  monkey["items_inspected"] = 0

  monkeys.append(monkey)

print("Part 1:", simulate_monkeys(deepcopy(monkeys), 20, True))
print("Part 2:", simulate_monkeys(monkeys, 10000, False))