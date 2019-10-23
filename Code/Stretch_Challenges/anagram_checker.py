import sys


def anagram_checker(input1, input2):
    input1 = sorted(input1)
    input2 = sorted(input2)

    if input1 == input2:
        return True
    return False


if __name__ == '__main__':
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    print(anagram_checker(input1, input2))
