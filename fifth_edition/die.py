"""The die rolls are what makes the world go round"""

import random

__author__ = "Grant Colasurdo"


class DieString:
    def __init__(self, string: str):
        self.string = string
        self.die_list = []
        number_of_die = string[:string.find('d')]
        sides_on_die = int(string[string.find('d')+1:])
        self.die_list = int(number_of_die) * [Die(sides_on_die)]

    def roll(self) -> int:
        return sum(die.roll() for die in self.die_list)


class Die:
    def __init__(self, sides: int):
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)


def make_roll():
    pass
