# place to save our future result
result = []

# for every line of input (first input line is the amount of following inputs)
for i in range(int(input())):

  # split the input into amount and item
  line = input().split(' ')

  # add the string to the result
  result.append(int(line[0]) * line[1])

# print the result
print('\n'.join(result))