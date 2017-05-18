"""Manage the inventory of a character"""

from fifth_edition import items
from fifth_edition import characters


class Armor:
    def __init__(self, character: 'characters.Character'):
        self.character = character
        
        
    @property
    def armor_class(self):

        return

    @property
    def stealth_disadvantage(self):
        return

