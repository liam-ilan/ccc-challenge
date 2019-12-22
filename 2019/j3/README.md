# J3: Cold Compress

## Problem Description
Your new cellphone plan charges you for every character you send from your phone. Since you
tend to send sequences of symbols in your messages, you have come up with the following compression technique: for each symbol, write down the number of times it appears consecutively,
followed by the symbol itself. This compression technique is called run-length encoding.

More formally, a block is a substring of identical symbols that is as long as possible. A block will
be represented in compressed form as the length of the block followed by the symbol in that block.
The encoding of a string is the representation of each block in the string in the order in which they
appear in the string.

Given a sequence of characters, write a program to encode them in this format.

## Input Specification
The first line of input contains the number N, which is the number of lines that follow. The next
N lines will contain at least one and at most 80 characters, none of which are spaces.

## Output Specification
Output will be N lines. Line i of the output will be the encoding of the line i + 1 of the input.
The encoding of a line will be a sequence of pairs, separated by a space, where each pair is an
integer (representing the number of times the character appears consecutively) followed by a space,
followed by the character.

#### [Solution](./main.py)
#### [Problem PDF](https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf)
