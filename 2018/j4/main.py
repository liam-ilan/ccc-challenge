'''
this solution was taken from last year. 
I figured that there is no need to rewrite it. 
My style changed a lot since then, so the code looks out of place.
There are also some parts where a more efficient method could be used.
Not to mention that there are many functions and a lot of unneeded code splitting.
'''

# get the matrix from the input
def get_table ():

  # the width and height of the table
  n = int(input())

  # the array where we store the raw data
  rawTable = []

  # get all inputs
  count = 0

  while count < n:
    rawTable.append(str(input()))
    count += 1

  table = []

  # convert the raw data into a matrix
  for x in range(0, len(rawTable)):
    table.append([int(x) for x in rawTable[x].split(' ')])

  # return the matrix
  return table

# rotates the table 90 degrees right
def rotate_table (table):

  # make out new table
  new_table = [[0 for row in table] for collumn in table]

  # for every item in the matrix
  for rows in range(0, len(table)):
    for collumns in range(0, len(table[rows])):

      # set the new_table item
      new_table[collumns][rows] = table[rows][collumns]

  # make our final table
  final_table = [[0 for row in table] for collumn in table]

  # flip the table along horizontal axis
  for rows in range(0, len(new_table)):
    final_table[len(new_table) - 1 - rows] = new_table[rows]

  # return the table
  return final_table


def validate_table (table):

  # the first height of the previous plant
  # this is -1, to let the first plant become the previous_first_height, when there is no previous plant
  previous_first_height = -1

  # for every row
  for rows in range(0, len(table)):

    # if the previous plant is bigger than our current plant, return false
    if table[rows][0] <= previous_first_height:
      return False

    # set the previous height to our current plant
    previous_first_height = table[rows][0]

    # the height of the plant a day ago
    # this is -1, to let the first measurment become the previous_plant_height, when there is no previous measurment
    previous_plant_height = -1

    # for every collumn
    for collumns in range(0, len(table[rows])):

      # if the previous measure is bigger than our current measure, return false
      if table[rows][collumns] <= previous_plant_height:
        return False

      # set the previous height to our current measure
      previous_plant_height = table[rows][collumns]

  # return that the table has passed
  return True

# convert the table to a string
def table_to_string (table):
  res = [[0 for row in table] for collumn in table]
 
  for rows in range(0, len(table)):
    for collumns in range(0, len(table[rows])):
      table[rows][collumns] = str(table[rows][collumns])
    res[rows] = ' '.join(table[rows])

  res = '\n'.join(res)
  return res

# solve the problem
def solve_table ():

  completed = False
  table = get_table()
  
  # continue to rotate the array until the table is validated
  while True:
    if validate_table(table):
      return table_to_string (table)
    table = rotate_table(table)


print(solve_table())



