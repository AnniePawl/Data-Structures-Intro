import sys


def reverse_sentence(input_sentence):
    """Returns sentence in reverse order"""
    reversed_sentence = input_sentence[::-1]
    return(reversed_sentence)
    # return ' '.join(reversed_sentence)


def reverse_word(input_word):
    """Returns word in reverse order"""
    input_word = ' '.join(input_word)
    reversed_word = input_word[::-1]
    return reversed_word


def reverse_reverse(reverse_reverse_input):
    """"Returns words And Sentences in reverse order"""
    # Reverse sentence first(type list)
    reversed1 = reverse_sentence(reverse_reverse_input)

    reversed2 = []
    for letter in reversed1:
        backwards_letter = reverse_word(letter)
        reversed2.append(backwards_letter)

    return ' '.join(reversed2)


if __name__ == '__main__':
    # input_sentence = sys.argv[1:]
    # print(reverse_sentence(input_sentence))

    # input_word = sys.argv[1:]
    # print(reverse_word(input_word))

    reverse_reverse_input = sys.argv[1:]
    print(reverse_reverse(reverse_reverse_input))
