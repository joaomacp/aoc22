import math

with open("input/day09.txt") as f:
  head_movements = [[part for part in line.strip().split(" ")] for line in f.readlines()]

DIRS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def process_head_movements(head_movements, rope_length):
  knots = [[0, 0] for _ in range(rope_length)]
  visited_tail_positions = set()

  for mov in head_movements:
    for _ in range(int(mov[1])):
      knots[0][0] += DIRS[mov[0]][0]
      knots[0][1] += DIRS[mov[0]][1]

      for i in range(1, len(knots)):
        delta_x, delta_y = knots[i-1][0] - knots[i][0], knots[i-1][1] - knots[i][1]
        if math.sqrt(delta_x**2 + delta_y**2) >= 2:
          knots[i][0] += math.copysign(min(1, abs(delta_x)), delta_x)
          knots[i][1] += math.copysign(min(1, abs(delta_y)), delta_y)
      visited_tail_positions.add(tuple(knots[-1]))
  
  return len(visited_tail_positions)

print("Part 1: ", process_head_movements(head_movements, 2))
print("Part 2: ", process_head_movements(head_movements, 10))