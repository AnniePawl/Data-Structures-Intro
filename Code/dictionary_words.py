# DICTIONARY WORDS
# All hardcoded parameters
# Program accepts one arrgument (num of words)
# Returns random sentence(not grammatical)

import sys
import random

word_count = int(' '.join(sys.argv[1:]))
word_list = []

with open("/usr/share/dict/words", "r") as file:
    # Select Random Words, Split, and Store in a Data Type
    list_of_words = file.read().splitlines()
    # print(list_of_words)
    # print(len(list_of_words))
    # while word_count < len(word_list):

    random_index = random.randint(0, len(list_of_words))
    # print(random_index)

    random_word = random.choices(list_of_words, k=word_count)

    word_list.append(' '.join(random_word))


if __name__ == '__main__':
    # fist value in array
    print(word_list[0])
