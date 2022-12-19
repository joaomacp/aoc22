part_one_found = False
total_sand = 0

def drop_sand(grid, grid_height, sand_spawn):
  global part_one_found

  sand_loc = sand_spawn
  while True:
    if sand_loc[1] == grid_height and not part_one_found:
      print("Part 1:", total_sand)
      part_one_found = True
    elif sand_loc[1] == grid_height + 1:
      grid.add(sand_loc)
      return True
    if (sand_loc[0], sand_loc[1]+1) not in grid:
      sand_loc = (sand_loc[0], sand_loc[1]+1)
    elif (sand_loc[0]-1, sand_loc[1]+1) not in grid:
      sand_loc = (sand_loc[0]-1, sand_loc[1]+1)
    elif (sand_loc[0]+1, sand_loc[1]+1) not in grid:
      sand_loc = (sand_loc[0]+1, sand_loc[1]+1)
    else:
      if sand_loc == sand_spawn:
        return False
      grid.add(sand_loc)
      return True

def add_path_to_grid(grid, path):
  blocks = path.split(" -> ")
  for i in range(1, len(blocks)):
    prev_x, prev_y = int(blocks[i-1].split(",")[0]), int(blocks[i-1].split(",")[1])
    x, y = int(blocks[i].split(",")[0]), int(blocks[i].split(",")[1])
    if prev_x == x:
      for row in range(min(prev_y, y), max(prev_y, y) + 1):
        grid.add((x, row))
    else:
      for col in range(min(prev_x, x), max(prev_x, x) + 1):
        grid.add((col, y))
    
grid = set()
with open("input/day14.txt") as f:
  _ = [add_path_to_grid(grid, path) for path in f.read().splitlines()]
grid_height = max(loc[1] for loc in grid)

while(drop_sand(grid, grid_height, (500, 0))):
  total_sand += 1
print("Part 2:", total_sand + 1)