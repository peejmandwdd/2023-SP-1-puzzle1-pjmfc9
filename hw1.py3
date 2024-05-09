import sys
import random

def countHaystacks():
  numHaystacks = 0
  for i in range(size):
    for j in range(size):
      if field[i][j] == '@':
        numHaystacks += 1
  return numHaystacks

def isValidSpot(r, c):
  if field[r][c] == '.':
    return True
  else:
    return False

# Places cows randomly, returns nothing
def placeCows(numCows):
  for i in range(numCows):
    # Generate random row and col
    randRow = random.randint(0, size - 1)
    randCol = random.randint(0, size - 1)
    while isValidSpot(randRow, randCol) == False:
      randRow = random.randint(0, size - 1)
      randCol = random.randint(0, size - 1)
    field[randRow] = field[randRow][:randCol] + 'C' + field[randRow][randCol + 1:]
  return

# Takes a row and col as inputs, returns a bool whether or not they can be indexed
def isInBounds(r, c):
  if r < 0 or r >= size or c < 0 or c >= size:
    return False
  return True

# Calculates and returns the score of an individual cow, takes the cow's position as inputs, returns individual score
def scoreCow(r, c):
  cowScore = 0
  anotherCow = False
  haystack = False
  haystackPond = False
  # Checks for adjacent cows
  for d in range(8):
    testRow = r + offsets[d][0]
    testCol = c + offsets[d][1]
    if isInBounds(testRow, testCol) and field[testRow][testCol] == 'C':
      anotherCow = True
  # Checks for adjacent hay/ponds
  for d in range(4):
    testRow = r + offsets2[d][0]
    testCol = c + offsets2[d][1]
    if isInBounds(testRow, testCol) and field[testRow][testCol] == '@':
      haystack = True
      for f in range(4):
        pondTestRow = r + offsets2[f][0]
        pondTestCol = c + offsets2[f][1]
        if isInBounds(pondTestRow, pondTestCol) and field[pondTestRow][pondTestCol] == '#':
          haystackPond = True
  # Scores the cow
  if anotherCow == True:
    cowScore -= 3
  if haystack == True:
    cowScore += 1
    if haystackPond == True:
      cowScore += 2
  return cowScore

def calculateTotalScore():
  totalScore = 0
  for i in range(size):
    for j in range(size):
      if field[i][j] == 'C':
        totalScore += scoreCow(i, j)
  return totalScore


f = open(sys.argv[1])

# Read in the file and create an array of strings
size = int(f.readline())
field = f.read().splitlines()
f.close()



###
#             NW,       N,       NE,      W,       E,      SW,     S,      SE
offsets = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
#              N,       E,     S,       W,
offsets2 = [[-1, 0], [0, 1], [1, 0], [0, -1]]

numCows = countHaystacks()
placeCows(numCows)

# File output
o = open(sys.argv[2], "w+")
o.write(str(size) + '\n')
for i in range(size):
  o.write(field[i] + '\n')
o.write(str(calculateTotalScore()) + '\n')