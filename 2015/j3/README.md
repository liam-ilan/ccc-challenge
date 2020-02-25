# J3: Rovarspraket

## Problem Description
In Sweden, there is a simple child’s game similar to Pig Latin called Rovarspraket (Robbers Language).

In the CCC version of Rovarspraket, every consonant is replaced by three letters, in the following order:

- the consonant itself;

- the vowel closest to the consonant in the alphabet (e.g., if the consonant is d, then the closest vowel is e), with the rule that if the consonant falls exactly between two vowels, then the vowel closer to the start of the alphabet will be chosen (e.g., if the consonant is c, then the closest vowel is a);

- the next consonant in the alphabet following the original consonant (e.g., if the consonant is d, then the next consonant is f) except if the original consonant is z, in which case the next consonant is z as well.

Vowels in the word remain the same. (Vowels are a, e, i, o, u and all other letters are consonants.)

Write a program that translates a word from English into Rovarspraket.

## Input Specification
The input consists of one word entirely composed of lower-case letters. There will be at least one letter and no more than 30 letters in this word.

## Output Specification
Output the word as it would be translated into Rovarspraket on one line.

#### [Solution](./main.py)
#### [Problem PDF](https://cemc.uwaterloo.ca/contests/computing/2015/stage%201/juniorEn.pdf)