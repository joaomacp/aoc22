def process_input():
  with open("input/day03.txt") as f:
    input = f.read()

  rucksacks = []
  for line in input.splitlines():
    rucksack = []
    for char in line:
      if char.islower():
        rucksack.append(ord(char) - ord("a") + 1)
      else:
        rucksack.append(ord(char) - ord("A") + 27)
    rucksacks.append(rucksack)
  
  return rucksacks

def find_common_items(items_a, items_b):
  return [item for item in items_a if item in items_b]


rucksacks = process_input()

sum_part_one = 0
for rucksack in rucksacks:
  middle_index = len(rucksack)//2
  first_part, second_part = rucksack[:middle_index], rucksack[middle_index:]
  sum_part_one += find_common_items(first_part, second_part)[0]
print("Part 1:", sum_part_one)

sum_part_two = 0
for i in range(0, len(rucksacks), 3):
  common_items = find_common_items(rucksacks[i], rucksacks[i+1])
  sum_part_two += find_common_items(common_items, rucksacks[i+2])[0]
print("Part 2:", sum_part_two)