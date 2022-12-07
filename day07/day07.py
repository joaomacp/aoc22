from pathlib import Path

with open("input/day07.txt") as f:
  lines = f.read().splitlines()[1:]

dir_sizes = {}
current_dir = Path("/")

for line in lines:
  if line.startswith("$ cd"):
    cd_target = line.split(" ")[2]
    if cd_target == "..":
      current_dir = current_dir.parent
    else:
      current_dir = current_dir.joinpath(cd_target)
  elif line != "$ ls":
    entry = line.split(' ')[0]
    if entry != 'dir':
      dir_sizes[current_dir] = dir_sizes.get(current_dir, 0) + int(entry)
      for parent in current_dir.parents:
        dir_sizes[parent] = dir_sizes.get(parent, 0) + int(entry)

print("Part 1:", sum([size for size in dir_sizes.values() if size <= 100000]))

## Part 2
DISK_SPACE = 70000000
FREE_SPACE_REQUIRED_FOR_UPDATE = 30000000
free_space = DISK_SPACE - dir_sizes[Path("/")]
min_space_to_free = FREE_SPACE_REQUIRED_FOR_UPDATE - free_space

print("Part 2:", min([size for size in dir_sizes.values() if size >= min_space_to_free]))