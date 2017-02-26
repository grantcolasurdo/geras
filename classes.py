"""Character class information"""

__author__ = "Grant Colasurdo"

import characters

class CharacterClass:
    """The base character class"""
    def __init__(
        self, character=None, name=None, primary_abilities=None, 
        secondary_abilities=None, 
    ):
        self.character = character
        self.class_name = name
        self.primary_abilities = primary_abilities
        self.secondary_abilities = secondary_abilities
        self.level_bonuses = None
        self.



