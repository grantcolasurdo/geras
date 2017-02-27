"""The die rolls are what makes the world go round"""

__author__ = "Grant Colasurdo"

import random

class DieString:
    def __init__(self, string: str):
        self.string = string
        self.die_list = []
        number_of_die = string[:string.find('d')]
        sides_on_die = string[string.find('d')+1:]
        self.die_list = int(number_of_die) * [Die(sides_on_die)]

    def roll(self) -> int:
        return sum(die.roll for die in self.die_list)

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self) -> int:
        try:
            return  random.randint(1,sides)
        except:
            print("number of sides was bad")

