# get inputs
distances = [0] + [int(i) for i in input().split(' ')]

currentStart = 0

# loop over distances (rows)
for x in distances:

  currentStart -= x

  # calculate the first distance
  currentDistance = currentStart

  result = []

  # loop again (columns)
  for y in distances:

    # add the distance to the current distance
    currentDistance += y
    
    # add to result
    result.append(str(abs(currentDistance)))

  # output
  print(' '.join(result))

