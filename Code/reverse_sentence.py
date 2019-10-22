import sys
import random


def reverse_sentence(input_sentence):
    reversed_sentence = input_sentence[::-1]

    return ' '.join(reversed_sentence)


input_sentence = sys.argv[1:]
print(reverse_sentence(input_sentence))
