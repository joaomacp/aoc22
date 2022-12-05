from copy import deepcopy

def add_line_to_stacks(line, stacks):
  for i in range(0, len(line), 4):
    if line[i:i+3].strip():
      stacks[i//4].append(line[i+1])

# 'parse' library would be useful here, but I'm not using external libs
# https://pypi.org/project/parse/
def parse_instruction(inst):
  inst = inst.replace("move ", "")
  inst = inst.replace(" from ", ",")
  inst = inst.replace(" to ", ",")
  return [int(num) for num in inst.split(",")]

def process_input():
  with open("input/day05.txt") as f:
    input = f.read()
  lines = input.splitlines()

  num_stacks = (len(lines[0]) + 1) // 4
  stacks = [[] for _ in range(num_stacks)]

  line_counter = 0
  while not lines[line_counter].startswith(" 1 "):
    add_line_to_stacks(lines[line_counter], stacks)
    line_counter += 1
  
  line_counter += 2
  instructions = []
  while line_counter < len(lines):
    instructions.append(parse_instruction(lines[line_counter]))
    line_counter += 1
  
  return stacks, instructions

stacks, instructions = process_input()

stacks_part_one = deepcopy(stacks)
for inst in instructions:
  amount, from_stack, to_stack = inst[0], inst[1]-1, inst[2]-1

  # Part 1
  for _ in range(amount):
    crate = stacks_part_one[from_stack].pop(0)
    stacks_part_one[to_stack].insert(0, crate)

  # Part 2
  crates = stacks[from_stack][0:amount]
  stacks[from_stack] = stacks[from_stack][amount:]
  stacks[to_stack] = crates + stacks[to_stack]

print("Part 1:", ''.join(stack[0] for stack in stacks_part_one if stack))
print("Part 2:", ''.join(stack[0] for stack in stacks if stack))