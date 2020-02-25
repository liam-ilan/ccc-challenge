# input
string = input()

# count
happy = string.count(':-)')
sad = string.count(':-(')

# check if none, unsure, happy, or sad
if happy + sad == 0:
  print('none')
elif happy == sad:
  print('unsure')
elif happy > sad:
  print('happy')
else:
  print('sad')