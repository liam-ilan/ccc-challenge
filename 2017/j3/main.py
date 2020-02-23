# get inputs
pointA = [int(x) for x in input().split(' ')]
pointB = [int(x) for x in input().split(' ')]
charge = int(input())

# calc distance
dis = abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])

# output
if dis <= charge and (charge - dis) % 2 == 0:
  print('Y');
else:
  print('N');