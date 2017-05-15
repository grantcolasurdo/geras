#! /usr/bin/python
import sys

from age import characters

sys.path.append("~/home/grant/Projects/")

print('geras imported')

a = characters.Character()
print('character created')
a.init_new_character()
print('character initialized')
