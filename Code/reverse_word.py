import sys
import random


def reverse_word(input_word):
    reversed_word = input_word[::-1]

    return reversed_word


input_word = sys.argv[1:]
print(reverse_word(' '.join(input_word)))
