# input
minutes = int(input())

def isArethmetic (arr):

  # get difference between any 2 items
  diff = arr[1] - arr[0]

  # for each item in arr
  for i in range(len(arr) - 1):

    # get the item, and the next item
    item = arr[i]
    nextItem = arr[i + 1]

    # calculate distance between item abd next item, and see that it does not matches diff
    if nextItem - item != diff:

      # in that case, return false
      return False 

  # return true if all items have a common difference
  return True

# increments time by a minute
def incrementByMin (time):

  # split hours and minutes
  timeList = [int(x) for x in time.split(':')]

  # add a minute to the minutes
  timeList[1] += 1

  # if overflow
  if timeList[1] == 60:

    # reset minutes
    timeList[1] = 0

    # add to hour
    timeList[0] += 1
    timeList[0] %= 12

  # stitch back together
  return str(timeList[0]) + ':' + str(timeList[1]).zfill(2)

# current time
currentTime = '12:00'

# total sequences
total = 0

# for each minute
for i in range(minutes + 1):
    
  # count if is sequence
  if isArethmetic([int(x) for x in list(currentTime.replace(':', ''))]):
    total += 1 

  # increment
  currentTime = incrementByMin(currentTime)

# output
print(total)