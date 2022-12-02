def process_input():
  with open("input/day02.txt") as f:
    input = f.read()

  # Convert to numbers: 1 = Rock, 2 = Paper, 3 = Scissors
  games = []
  for line in input.splitlines():
    game = line.split()
    game[0] = ord(game[0]) - ord("A") + 1
    game[1] = ord(game[1]) - ord("X") + 1
    games.append(game)
  return games

def game_score(game):
  theirs, ours = game[0], game[1]
  diff = ours - theirs
  if abs(diff) == 0:
    score = 3
  elif abs(diff) == 1:
    score = 6 if diff > 0 else 0
  else:
    score = 6 if diff < 0 else 0
  return score + ours

def interpret_instruction(instruction):
  # Turn their play into 0, 1, 2, turn outcome into -1, 0, 1: loss, draw, win
  their_play_norm, outcome = instruction[0]-1, instruction[1]-2
  our_play = (their_play_norm + outcome) % 3 + 1
  return game_score([instruction[0], our_play])


games = process_input()

part_1_score = 0
part_2_score = 0
for game in games:
  part_1_score += game_score(game)
  part_2_score += interpret_instruction(game)

print("Part 1:", part_1_score)
print("Part 2:", part_2_score)