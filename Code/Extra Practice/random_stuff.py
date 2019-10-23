# RANDOM FUNCTION PRACTICE

import random

dogs = ("bella", "winnie", "boo", "zola", "pino", "maisy", "emilio")

fruits = ("apple", "banana", "orange", "lemon")

veggies = ("carrot", "eggplant", "mushroom", "pepper")

robots = ("R2D2", "C3PO", "Wall-E", "Eve")

nuts = ("cashew", "peanut", "almond", "walnut")

dairy = ("milk", "butter", "cream", "cheese")


def random_dog():
    random_index = random.randint(0, len(dogs)-1)
    return dogs[random_index]


def random_fruit():
    random_index = random.randint(0, len(fruits)-1)
    return fruits[random_index]


def random_veggie():
    random_index = random.randint(0, len(veggies)-1)
    return veggies[random_index]


def random_robot():
    random_index = random.randint(0, len(robots)-1)
    return robots[random_index]


def random_nut():
    random_index = random.randint(0, len(nuts)-1)
    return nuts[random_index]


def random_dairy():
    random_index = random.randint(0, len(dairy)-1)
    return dairy[random_index]


if __name__ == '__main__':
    fruit = random_fruit()
    print(fruit)
    quote = random_dog()
    print(quote)
    veggie = random_veggie()
    print(veggie)
    robot = random_robot()
    print(robot)
    nut = random_nut()
    print(nut)
    dairy = random_dairy()
    print(dairy)
