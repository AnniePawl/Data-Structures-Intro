import sys
import random


def rearrange_words(input_words):
    """Randomly rearranges words provided as command-line arguments"""

    # Initialize new list to hold rearranged words
    rearranged_words = []

    # Randomly put input_words into 'rearranged_words' list until all input_words are used

    while len(rearranged_words) < len(input_words):
        random_index = random.randint(0, len(input_words)-1)
        random_word = input_words[random_index]

        # Skip words that have already been seen
        if random_word in rearranged_words:
            continue
        rearranged_words.append(random_word)

    # Turn list into a nicely formatted string
    result = ' '.join(rearranged_words)
    return result


if __name__ == '__main__':
    # remember argument one is file name!
    input_words = sys.argv[1:]
    print(rearrange_words(input_words))
