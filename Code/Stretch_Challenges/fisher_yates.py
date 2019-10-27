# Shuffle an array using Fisher Yates Shuffle Algorithm
# Every permutation of array should be equally likely
# 0(n) Complexity

import random


def fisher_yates_shuffle(array):
    for index in range(len(array)-1):  # access all nums in array
        # random num between 0 and current index
        random_index = random.randint(0, index + 1)
        # swap index w/ num at random index
        array[index], array[random_index] = array[random_index], array[index]
    return array


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':
    print(fisher_yates_shuffle(array))
