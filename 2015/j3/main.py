# get input
word = input()

# init output
output = ''

# alphabet, vowels, and their indexes
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# explanation for last index below
vowelIndexes = [0, 4, 8, 14, 20, 50]

# it is useful for us to have the placeholder value have a large index, to minimize comparisons.
# this is why / is included
vowels = 'aeiou/'

def closestVowel(char):

  # init placeholder
  firstVowel = '/'
  secondVowel = '/'

  # see if there has been an occurrence of char beforehand in loop
  seenSelf = False

  # loop over alphabet
  for x in alphabet:

    # index of letter in alphabet
    index = alphabet.find(x)

    # if seen, update seenSelf to true
    if x == char:
      seenSelf = True

    # if current letter in alphabet is a vowel, and has not been seen, it is the first vowel
    if (x in vowels) and seenSelf == False:
      firstVowel = x

    # if seen, second vowel
    elif (x in vowels) and seenSelf == True:
      secondVowel = x

      # break loop, as there is no reason to continue
      break

  # get indexes
  firstVowelIndex = vowelIndexes[vowels.index(firstVowel)]
  secondVowelIndex = vowelIndexes[vowels.index(secondVowel)]

  charIndex = alphabet.index(char)

  # check distances, and return
  if abs(firstVowelIndex - charIndex) > abs(secondVowelIndex - charIndex):
    return secondVowel
  else:
    return firstVowel

# for every char
for char in word:

  # get index
  index = alphabet.find(char)

  # init "replacement" char
  newSubstring = char

  # if the character is not a vowel
  if char not in vowels:

    # gets the next constant, could probably be done... cleaner?
    nextConstant = alphabet[index if index == len(alphabet) - 1 else (index + 1 if alphabet[index + 1] not in vowels else index + 2)]

    # add the closest vowel, and the next char
    newSubstring += closestVowel(char) + nextConstant

  # add to output
  output += newSubstring

# output
print(output)
