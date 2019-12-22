# the place to store the digits of the number
digits = []

# get inputs, convert to int, put in digits
for i in range(4):
  digits.append(int(input()))

# if first digit are 8 or 9 and last digit are 8 or 9 and middle digits are equal
if (digits[0] == 8 or digits[0] == 9) and (digits[3] == 8 or digits[3] == 9) and (digits[1] == digits[2]):
  print('ignore')
else:
  print('answer')