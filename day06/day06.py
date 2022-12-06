with open("input/day06.txt") as f:
  input = f.read().strip()

part_one, part_two = None, None
for i in range(3, len(input)):
  if not part_one and len(set(input[i-3:i+1])) == 4:
    part_one = i + 1
  if not part_two and i >= 13 and len(set(input[i-13:i+1])) == 14:
    part_two = i + 1
  if part_one and part_two:
    break

print("Part 1:", part_one)
print("Part 2:", part_two)