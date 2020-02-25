# inputs
month = int(input())
day = int(input())

# if the month is past February, or it is February and the day is past the 18th
if month > 2 or (day > 18 and month == 2):
  print('After')

# if the the month is before February, or the day is less than 18, and the condition above is false
elif month < 2 or day < 18:
  print('Before')

# final case must be Special
else:
  print('Special')