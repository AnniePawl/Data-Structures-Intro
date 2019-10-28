import sys
import random

# Read from this file
file = open("creatures.txt")

# Select Random Words, Split, and Store in a Data Type
list_of_words = file.read().split(" ")
# Specify number of words you want from sample
random_words = random.choices(list_of_words, k=5)

if __name__ == '__main__':
    # Form Sentence
    random_sentence = ' '.join(random_words)
    print(random_sentence)
