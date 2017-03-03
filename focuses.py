"""This is where the logic for focuses lie"""

import character

__author__ = "Grant Colasurdo"

def aquire_focus(character: character.Character, focus_name: Focus):
    character.focuses.aquire_focus(focus_name)


class Focuses:
    def __init__(
        self, character, aquired_focuses=None, all_focuses=None
    ):
        self.character = character
        self.aquired_focuses = aquired_focuses
        self.all_focuses = all_focuses

    def available_focuses(self):
        """Return a set of focuses that are available to a character in it's
        current state"""
        pass

    def aquire_focus(self, focus):
        if focus in self.available_focuses():
            """The focus is available, now do we already have it?"""
            return_focus(focus).level += 1
        else:
            self.aquired_focuses.add(focus(self))

    def return_focus(self, focus):
        focus_list = [
            individual_focus for individual_focus in self.available_focuses
            if isinstance(individual_focus, focus)
        ]
        if len(focus_list) == 1:
            return return_focus[0]
        else:
            return None


class Focus:
    def __init__(
        self,
        focuses=None,
        name=None,
        ability=None,
        level=None,
        description=None
    ):
        self.focuses = focuses
        self.focus_name: str = name
        self.ability: str = ability
        self.level = level
        self.description: str = description

    def bonus(self):
        if self.level == 0:
            return 0
        elif self.level == 1:
            return 2
        elif self.level == 2:
            return 3
        else:
            print("Focus level is too damn high")
            raise Exception

