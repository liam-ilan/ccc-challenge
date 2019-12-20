# get packages
import copy

# collect rules
substitutionRules = [
  input().split(' '),
  input().split(' '),
  input().split(' ')
]

# collect last line of data
stepsToBeUsed, originalLine, outputLine = input().split(' ')
stepsToBeUsed = int(stepsToBeUsed)

# substitute parts of a string
def replace (line, substitute, index, substitutedLength):
  res = list(line[:index])
  res.extend(list(substitute))
  res.extend(list(line[index + substitutedLength:]))

  return ''.join(res)

# define result (result will come here later)
result = []

# recursive function, will put result in result
def findPossibilities(state, history, itteration):

  # if we have not surrpased the amount of steps needed and the result is not found
  if itteration < stepsToBeUsed and len(result) < 1:

    # for every charecter in the current state
    for charPos in range(len(state)):

      # for every rule (substitutionRules)
      for ruleNum in range(3):

        # get rule
        rule = substitutionRules[ruleNum]

        # if rule matches
        if state[charPos:len(rule[0]) + charPos] == rule[0]:

          # get the next state
          newState = replace(state, rule[1], charPos, len(rule[0]))

          # make a new history
          newHistory.append([ruleNum + 1, charPos + 1, newState])

          # find the next set of possibilities
          findPossibilities(newState, history, itteration + 1)

  # if limit reached and we have a correct history
  elif len(result) < 1 and history[stepsToBeUsed - 1][2] == outputLine:

    # add to possible outcomes
    result.extend(history)

# run
findPossibilities(originalLine, [], 0)

# render
for i in result:
  print(' '.join(list(map(str, i))))
