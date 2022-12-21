volcano = dict()
with open("input/day16.txt") as f:
  for line in f.read().splitlines():
    tokens = line.replace("Valve ", "").replace(" has flow rate=", ", ") \
                      .replace("; tunnels lead to valves ", ", ").replace("; tunnel leads to valve ", ", ") \
                      .split(", ")
    volcano[tokens[0]] = [int(tokens[1]), tokens[2:]]

memo = dict()
memo_exact = dict()

def optimal_pressure(current_valve, time_left, open_valves, pressure):
  if time_left == 1:
    return pressure
  if (current_valve, time_left, tuple(open_valves)) in memo_exact:
    return memo_exact[(current_valve, time_left, tuple(open_valves))] + pressure
  if (current_valve, time_left) in memo:
    closed_valves = [valve for valve in volcano if valve not in open_valves]
    potential = sum([volcano[valve][0] * (time_left-1) for valve in closed_valves])
    if potential < memo[(current_valve, time_left)]:
      return 0
    # return memo[(current_valve, time_left)] + pressure
  options = []
  if current_valve not in open_valves: # Valve is closed, opening is an option
    valve_pressure = volcano[current_valve][0]
    options.append(optimal_pressure(current_valve, time_left-1, sorted(open_valves + [current_valve]), \
                                    pressure + valve_pressure * (time_left-1)))
  for neighbour in volcano[current_valve][1]:
    options.append(optimal_pressure(neighbour, time_left-1, sorted(open_valves), \
                                    pressure))
  val = max(options)
  memo[(current_valve, time_left)] = val - pressure
  memo_exact[(current_valve, time_left, tuple(open_valves))] = val - pressure
  return val

print("Part 1:", optimal_pressure("AA", 30, [], 0))