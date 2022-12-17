def dist(row, col, end_row, end_col):
  return abs(row - end_row) + abs(col - end_col)

def get_neighbours(grid, row, col):
  neighbours = {(row-1, col), (row+1, col), (row, col-1), (row, col+1)}
  for neighbour in neighbours.copy():
    if neighbour[0] < 0 or neighbour[0] >= len(grid) \
    or neighbour[1] < 0 or neighbour[1] >= len(grid[0]) \
    or ord(grid[neighbour[0]][neighbour[1]]) > ord(grid[row][col]) + 1:
      neighbours.remove(neighbour)
  return neighbours

def reconstruct_path(came_from, current):
  total_path = [current]
  while current in came_from.keys():
    current = came_from[current]
    total_path.insert(0, current)
  return total_path

def a_star(grid, start_row, start_col, end_row, end_col):
  open_set = {(start_row, start_col)}
  came_from = dict()
  g_score = {(start_row, start_col): 0}
  f_score = {(start_row, start_col): dist(start_row, start_col, end_row, end_col)}

  while len(open_set) > 0:
    current = sorted(open_set, key=lambda x: f_score.get(x, 1_000_000))[0]
    if current == (end_row, end_col):
      return reconstruct_path(came_from, current)
    
    open_set.remove(current)
    for neighbour in get_neighbours(grid, current[0], current[1]):
      tentative_g_score =  g_score[current] + 1
      if tentative_g_score < g_score.get(neighbour, 1_000_000):
        came_from[neighbour] = current
        g_score[neighbour] = tentative_g_score
        f_score[neighbour] = tentative_g_score + dist(neighbour[0], neighbour[1], end_row, end_col)
        open_set.add(neighbour)

starting_positions = []

with open("input/day12.txt") as f:
  grid = f.read().splitlines()
for idx_line, line in enumerate(grid):
  for idx_char, char in enumerate(line):
    if char == "a":
      starting_positions.append((idx_line, idx_char))
    elif char == "S":
      start_row, start_col = idx_line, idx_char
      grid[idx_line] = grid[idx_line].replace("S", "a")
      starting_positions.append((idx_line, idx_char))
    elif char == 'E':
      end_row, end_col = idx_line, idx_char
      grid[idx_line] = grid[idx_line].replace("E", "z")

print("Part 1:", len(a_star(grid, start_row, start_col, end_row, end_col)) - 1)

paths_from_a = [a_star(grid, pos[0], pos[1], end_row, end_col) for pos in starting_positions]
print("Part 2:", min([len(path) - 1 for path in paths_from_a if path]))