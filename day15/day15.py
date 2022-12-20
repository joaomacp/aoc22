def range_union(ranges):
  result = []
  for begin, end in sorted(ranges):
    if result and result[-1][1] >= begin - 1:
      result[-1][1] = max(result[-1][1], end)
    else:
      result.append([begin, end])
  return result

sensors = []
with open("input/day15.txt") as f:
  for line in f.read().splitlines():
    line = line.replace("Sensor at ", "").replace(": closest beacon is at ", ", ")
    sensors.append([int(value[2:]) for value in line.split(", ")])

def test_row(row_to_check):
  beacons = set()
  free_ranges = []
  for sensor in sensors:
    sensor_x, sensor_y, closest_x, closest_y = tuple(sensor)
    sensor_range = abs(sensor_x - closest_x) + abs(sensor_y - closest_y)
    y_dist_to_test_row = abs(sensor_y - row_to_check)
    remaining_range = sensor_range - y_dist_to_test_row
    if remaining_range >= 0:
      free_ranges.append((sensor_x - remaining_range, sensor_x + remaining_range))
      if closest_y == row_to_check:
        beacons.add((closest_x, closest_y))
  return range_union(free_ranges), beacons

free_ranges, beacons = test_row(2000000)
print("Part 1:", sum(range[1] - range[0] + 1 for range in free_ranges) - len(beacons))

for row in range(0, 4000000):
  free_ranges, _ = test_row(row)
  for range in free_ranges:
    if 0 <= range[0] <= 4000000:
      print("Part 2:", 4000000 * (range[0] - 1) + row)