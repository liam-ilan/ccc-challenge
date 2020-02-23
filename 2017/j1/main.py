# get inputs
x, y = int(input()), int(input())

# check quadrants (there is probably a better way to do this)
if x > 0 and y > 0:
  print(1)
elif x < 0 and y > 0:
  print(2)
elif x < 0 and y < 0:
  print(3)
elif x > 0 and y < 0:
  print(4)