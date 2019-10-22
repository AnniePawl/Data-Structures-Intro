import sys


def anagram(input1, input2):
    # Check if inputs are same length
    sorted1 = sorted(input1)
    sorted2 = sorted(input2)

    if sorted1 == sorted2:
        return True

    return False


input1 = sys.argv[1]
input2 = sys.argv[2]

print(anagram(input1, input2))
