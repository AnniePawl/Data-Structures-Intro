import sys
import random

# Program accepts one argument (# of words)
number = input("Enter a number: ")


def get_words(text):
    """ reads file, strips leading and trailer characters, returns list of stings (#TODO?) """
    words = []
    with open("/usr/share/dict/words", "r") as file:  # closes file when done
        text = file.read().strip().split(" ")
        return text


def random_sentence(words):
    """ randomly selects words from list and returns them as a properly formatted sentence """
    random_words = random.choice(words)
    random_sentence = ' '.join(random_words)
    # format sentence
    return random_sentence


if __name__ == '__main__':
    source = get_words("/usr/share/dict/words")
    print(random_sentence(source))
