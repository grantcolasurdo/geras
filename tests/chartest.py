#! /usr/bin/python
import sys
sys.path.append("/home/grant/Projects/")
import geras.characters

print('geras imported')

a = geras.characters.Character()
print('character created')
a.init_new_character()
print('characer initialized')
