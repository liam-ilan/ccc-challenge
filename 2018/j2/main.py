# get length
length = int(input())

# get lines
lines = [input(), input()]

# result
result = 0

# for every spot in the first line
for i in range(length):

  # if two parking spaces are taken, and the first item is equal to C
  # note: we don't have to check both items
  # if the first and second condition is true, then the second item must equal C
  
  if lines[0][i] == lines[1][i] and lines[0][i] == 'C':

    # add one to the result
    result += 1

# output
print(result)
