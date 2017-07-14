"""Test the race library"""

__author__ = "Grant Colasurdo"

from fifth_edition import characters
from fifth_edition import races

for name in races.RACE_DICT:
    char = characters.Character()
    instance: races.Race = races.RACE_DICT[name](char)
    print(instance.BASE_HEIGHT)
    print(instance.BASE_SPEED)
    print(instance.BASE_WEIGHT)
    print(instance.WEIGHT_MODIFIER)
    print(instance.HEIGHT_MODIFIER)
    print(instance.FAMILY_NAMES)
    print(instance.BASE_SPEED)

