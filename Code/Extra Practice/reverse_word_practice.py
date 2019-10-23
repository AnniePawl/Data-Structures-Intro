import sys


def reverse_word(input_word):
    reversed_word = input_word[::-1]

    return reversed_word


if __name__ == '__main__':
    input_word = sys.argv[1:]
    print(reverse_word(' '.join(input_word)))
