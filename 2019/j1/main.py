# init scores
apples = 0
bananas = 0

# get inputs and tally up scores
for i in range(3):
  apples += (3 - i) * int(input())

for i in range(3):
  bananas += (3 - i) * int(input())

# evalutate and output
if apples > bananas:
  print('A')
elif bananas > apples:
  print('B')
else:
  print('T')