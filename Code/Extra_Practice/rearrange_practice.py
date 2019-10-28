import random
import sys


def rearrange_sentence(input_sentence):
    """Rearranges the word order of an input sentence"""

    rearranged_sentence = []

    while len(rearranged_sentence) < len(input_sentence):
        random_index = random.randint(0, len(input_sentence)-1)
        random_word = input_sentence[random_index]

        if random_word not in rearranged_sentence:
            rearranged_sentence.append(random_word)

    result = ' '.join(rearranged_sentence)
    return result


if __name__ == '__main__':
    input_sentence = sys.argv[1:]
    print(rearrange_sentence(input_sentence))
