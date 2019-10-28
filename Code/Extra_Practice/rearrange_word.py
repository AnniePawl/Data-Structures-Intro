import random
import sys


def rearrange_word(input_word):
    split_input = input_word.split("")
    rearranged_word = []

    while len(rearranged_word) < len((split_input)):
        random_index = random.randint(0, len(split_input)-1)
        random_letter = split_input[random_index]

        if random_letter not in rearranged_word:
            rearranged_word.append(random_letter)

    return rearranged_word


if __name__ == '__main__':
    input_word = sys.argv[1:]
    print(rearrange_word(input_word))
