import numpy as np

with open("input/day08.txt") as f:
  grid = np.array([[int(char) for char in line] for line in f.read().splitlines()])

interior_trees_visible = 0
best_scenic_score = 0
for i in range(1, grid.shape[0]-1):
  for j in range(1, grid.shape[1]-1):
    # Part 1
    if max(grid[0:i,j]) < grid[i,j] or \
       max(grid[i+1:,j]) < grid[i,j] or \
       max(grid[i,0:j]) < grid[i,j] or \
       max(grid[i,j+1:]) < grid[i,j]:
      interior_trees_visible += 1
    
    # Part 2
    view_distance_up = 0
    for row in range(i-1, -1, -1):
      view_distance_up += 1
      if grid[row, j] >= grid[i, j]:
        break
    view_distance_down = 0
    for row in range(i+1, grid.shape[0]):
      view_distance_down += 1
      if grid[row, j] >= grid[i, j]:
        break
    view_distance_left = 0
    for col in range(j-1, -1, -1):
      view_distance_left += 1
      if grid[i, col] >= grid[i, j]:
        break
    view_distance_right = 0
    for col in range(j+1, grid.shape[1]):
      view_distance_right += 1
      if grid[i, col] >= grid[i, j]:
        break
    scenic_score = view_distance_up * view_distance_down * view_distance_left * view_distance_right
    best_scenic_score = max(best_scenic_score, scenic_score)

print("Part 1:", interior_trees_visible + 2 * grid.shape[0] + 2 * grid.shape[1] - 4)
print("Part 2:", best_scenic_score)