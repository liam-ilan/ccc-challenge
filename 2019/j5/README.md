# J5: Rule of Three

## Problem Description
A substitution rule describes how to take a sequence of symbols and convert it into a different
sequence of symbols. For example, ABA → BBB, is a substitution rule which means that ABA
can be replaced with BBB. Using this rule, the sequence AABAA would be transformed into the
sequence ABBBA (the substituted symbols are in bold).

In this task, you will be given three substitution rules, a starting sequence of symbols and a final
sequence of symbols. You are to use the substitution rules to convert the starting sequence into the
final sequence, using a specified number of substitutions.

For example, if the three substitution rules were:

1. AA → AB
2. AB → BB
3. B → AA

we could convert the sequence AB into AAAB in 4 steps, by the following substitutions:

AB → BB → AAB → AAAA → AAAB,

where the symbols to be replaced are shown in bold. More specifically, from the initial sequence
AB, substitute rule 2 starting at position 1, to get the result BB. From BB, substitute rule 3, starting

at position 1, to get the result AAB. From AAB, substitute rule 3, starting at position 3, to get the
result AAAA. From AAAA, substitute rule 1, starting at position 3, to get the result AAAB, which
is the final sequence.

## Input Specification
The first three lines will contain the substitution rules. Each substitution rule will be a sequence
of A’s and B’s, followed by a space following by another sequence of A’s and B’s. Both sequences
will have between one and five symbols.

The next line contains three space separated values, S, I and F. The value S (1 ≤ S ≤ 15) is an
integer specifying the number of steps that must be used, and the values I (the initial sequence)
and F (the final sequence) are sequences of A’s and B’s, where there are at least one and at most 5
symbols in I and at least one and at most 50 symbols in F.

For 7 of the 15 marks available, S ≤ 6.

For an additional 7 of the 15 available marks, S ≤ 12.

## Output Specification
The output will be S lines long and describes the substitutions in order.

### [solution](./main.py)
### [Problem PDF](https://www.cemc.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf)