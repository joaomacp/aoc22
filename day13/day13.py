import math
from functools import cmp_to_key

def compare(left, right):
  if not left or not right:
    return len(right) - len(left)
  if type(left[0]).__name__ == "int" and type(right[0]).__name__ == "int":
    if left[0] != right[0]:
      return right[0] - left[0]
  elif type(left[0]).__name__ == "list" and type(right[0]).__name__ == "list":
    result = compare(left[0], right[0])
    if result != 0:
      return result
  else:
    if type(left[0]).__name__ == "int":
      return compare([left[0]], right[0])
    else:
      return compare(left[0], [right[0]])
  return compare(left[1:], right[1:])

sum_part_one = 0
all_signals = []
with open("input/day13.txt") as f:
  for idx, pair in enumerate(f.read().split("\n\n")):
    sum_part_one += (idx + 1) * (1 if compare(*[eval(signal) for signal in pair.splitlines()]) > 0 else 0)
    all_signals += [eval(signal) for signal in pair.splitlines()]
print("Part 1:", sum_part_one)

EXTRA_SIGNALS = [[[2]], [[6]]]
all_signals += EXTRA_SIGNALS
all_signals.sort(key=cmp_to_key(compare), reverse=True)
print("Part 2:", math.prod(all_signals.index(signal) + 1 for signal in EXTRA_SIGNALS))