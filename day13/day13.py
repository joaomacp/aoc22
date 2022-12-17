def compare(pair):
  print(pair)
  return True

part_one_sum = 0
with open("input/day13.txt") as f:
  for idx, pair in enumerate(f.read().split("\n\n")):
    part_one_sum += (idx + 1) * compare(pair.splitlines())
print("Part 1:", part_one_sum)