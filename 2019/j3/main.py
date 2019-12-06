# place to save our future result
result = []

# for every line of input (first input line is the amount of following inputs)
for i in range(int(input())):

  # get the input from the user
  line = input()

  # variable to store the output line from the input
  outputLine = ''

  # how many of a certain letter there are
  count = 0

  # the currently counted letter
  currentChar = line[0]

  # for every letter in a line
  for x in line:

    # if the current letter is different from the letter we are currently looking at
    if currentChar != x:

      # push the count and letter into the output line
      outputLine += str(count) + ' ' + currentChar + ' '

      # reset the count
      count = 0

    # add 1 to the count
    count += 1

    # set the current letter
    currentChar = x

  # the last section of letters will not be pushed onto output line 
  # to compensate, we push the remaining letters into the output line
  outputLine += str(count) + ' ' + currentChar

  # add the output line to the result
  result.append(outputLine)

# print the result
print('\n'.join(result))