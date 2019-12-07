#initializing the grid
grid = [
  ["1", "2"],
  ["3", "4"]
]

# rotations

# rotating a matrix along a horizontal axis is like switching two items
# therefore rotateHorizontal() is not needed
def switchItems(arr):
  temp = arr[1]
  arr[1] = arr[0]
  arr[0] = temp

def rotateVertical(arr):
  switchItems(arr[0])
  switchItems(arr[1])

# rendering
def render(arr):
  print(' '.join(arr[0]))
  print(' '.join(arr[1]))

# parsing
def parseInstructions(instructions):

  # for every instruction
  for i in range(0, len(instructions)):

    # if V then flip vertical
    # if H then flip horizontal
    if instructions[i] == "V":
      rotateVertical(grid)
    if instructions[i] == "H":
      switchItems(grid)

# get instructions
instructions = input()

# parse instructions
parseInstructions(instructions)

# render final result
render(grid)