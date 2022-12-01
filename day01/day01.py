with open("input/day01.txt") as f:
  input = f.read()

elf_food_totals = []

elves = input.split("\n\n")
for elf_food in elves:
    elf_food_sum = sum([int(cal) for cal in elf_food.strip().split("\n")])
    elf_food_totals.append(elf_food_sum)

elf_food_totals.sort(reverse=True)

print("Part 1:", elf_food_totals[0])
print("Part 2:", sum(elf_food_totals[0:3]))