with open("input/day04.txt") as f:
  input = f.read()

pairs = [[[int(num) for num in pair.split('-')] for pair in line.split(',')] for line in input.splitlines()]

sum_contained = 0
sum_intersection = 0
for pair in pairs:
  if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or \
     (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]):
    sum_contained += 1
  elif (pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]) or \
       (pair[0][1] >= pair[1][0] and pair[0][1] <= pair[1][1]):
    sum_intersection += 1

print ("Part 1:", sum_contained)
print ("Part 2:", sum_contained + sum_intersection)