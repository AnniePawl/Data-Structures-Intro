import sys


def reverse_sentence(input_sentence):
    reversed_sentence = input_sentence[::-1]
    final_sentence = ' '.join(reversed_sentence)

    return final_sentence


if __name__ == '__main__':
    input_sentence = sys.argv[1:]
    print(reverse_sentence(input_sentence))
