import sys
import random


def rearrange_sentence(input_sentence):
    rearranged_sentence = []

    while len(rearranged_sentence) < len(input_sentence):
        random_index = random.randint(0, len(input_sentence)-1)
        random_word = input_sentence[random_index]

        # Is word already in rearranged sentence list?
        if random_word not in rearranged_sentence:
            rearranged_sentence.append(random_word)

    return ' '.join(rearranged_sentence)


input_sentence = sys.argv[1:]
print(rearrange_sentence(input_sentence))
