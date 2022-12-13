with open("input/day10.txt") as f:
  instrs = f.readlines()

part_one_cycles = [20, 60, 100, 140, 180, 220]

x, clock = 1, 0
sum_part_one = 0

def process_clock(ticks):
  global clock, sum_part_one
  for _ in range(ticks):
    # Part one
    if part_one_cycles and clock == part_one_cycles[0] - 1:
      sum_part_one += part_one_cycles[0] * x
      del part_one_cycles[0]

    # Part two
    if clock % 40 == 0:
      print()
    print("#" if clock % 40 >= x - 1 and clock % 40 < x + 2 else '.', end='')

    clock += 1

for inst in instrs:
  if inst.strip() == "noop":
    process_clock(1)
  else:
    process_clock(2)
    x += int(inst.split(" ")[1])

print("Part 1:", sum_part_one)