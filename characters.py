"""
The Idea behind this project is that I'll be able to use it as a tool in
keeping track of all the stats, numbers and calculations that go into an AGE
based roll playing game. The template that I'm building this off of is Titan's
Grave. 
"""

__author__ = "Grant Colasurdo"

import spells
import talents
import items

def inputresponse(caption, options):
    print(caption)
    print(options)
    while choice not in options:
        option = input('')
    return option


class Requirement:
    def __init__(self):
        pass

    def test(self, character):
        return False


class Character:
    """This is the character object that holds a character's attributes"""
    def __init__(self):
        self.character_name: str = None
        self.max_health: int = None
        self.current_health: int = None
        self.level: int = None
        self.experience_points = None
        self.abilities: Abilities = None
        self.focuses: Focuses = None
        self.talents: Talents = None
        self.weapon_groups: set = None
        self.talents: set = None
        self.character_class: CharacterClass  = None
        self.specializations: set = None
        self.race: Race = None
        self.magic: Magic = None

        def rest(self):
            self.current_health = self.max_health
            self.current_mana = self.max_mana

        def init_new_character(self):
            """
            The guidebook layes out the character creation process in 9 points
            1. Create a character concept
            2. Determine abilities
            3. Choose a race
            4. determine a social class an background
            5. choose a class
            6. pick a starting equipment
            7. calculate defense
            8. pick a name
            9. choose goals and character ties for your character
            """
            pass
            

class Abilities:
    def __init__(self, character):
        self.character = character
        self.accuracy_start = None
        self.communication_start = None
        self.constitution_start = None
        self.dexterity_start = None
        self.fighting_start = None
        self.intelligence_start = None
        self.perception_start = None
        self.strength_start = None
        self.willpower_start = None
        self._level_log: list = []
        
    determine_ability_table = {
        3:-2, 4:-1, 5:-1, 6:0, 7:0, 8:0, 9:1, 10:1, 11:1, 12:2, 13:2,
        14:2, 15:3, 16:3, 17:3, 18:4
    }

    def init_character(self):
        self.accuracy_start = 

    @property
    def accuracy(self):
        levelups = sum(
            1 if ability == "accuracy" else 0 for ability in self._level_log
        )
        return self.accuracy_start + levelups

    @property
    def communication(self):
        levelups = sum(
            1 if ability == "communication" else 0 for ability in self._level_log
        )
        return self.communication_start + levelups

    @property
    def constitution(self):
        levelups = sum(
            1 if ability == "constitution" else 0 for ability in self._level_log
        )
        return self.constitution_start + levelups


    @property
    def dexterity(self):
        levelups = sum(
            1 if ability == "dexterity" else 0 for ability in self._level_log
        )
        return self.dexteritystart + levelups


    @property
    def fighting(self):
        levelups = sum(
            1 if ability == "fighting" else 0 for ability in self._level_log
        )
        return self.fighting_start + levelups


    @property
    def intelligence(self):
        levelups = sum(
            1 if ability == "intelligence" else 0 for ability in self._level_log
        )
        return self.intelligence_start + levelups


    @property
    def perception(self):
        levelups = sum(
            1 if ability == "perception" else 0 for ability in self._level_log
        )
        return self.perception_start + levelups

    @property
    def strength(self):
        levelups = sum(
            1 if ability == "strength" else 0 for ability in self._level_log
        )
        return self.strength_start + levelups

    @property
    def willpower(self):
        levelups = sum(
            1 if ability == "willpower" else 0 for ability in self._level_log
        )
        return self.willpower_start + levelups


class Focuses:
    def __init__(
        self, character=None, aquired_focuses=None, all_focuses=None
    ):
        self.character = character
        self.aquired_focuses = aquired_focuses
        self.all_focuses = all_focuses

    def available_focuses(self):
        """Return a set of focuses that are available to a character in it's
        current state"""
        pass

    def aquire_focus(self, focus:Focus):
        if focus in self.available_focuses():
            """The focus is available, now do we already have it?"""
            return_focus(focus).level += 1
        else:
            self.aquired_focuses.add(focus(self))
    
    def return_focus(self, focus:Focus):
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
        self, focuses=None, name=None, ability=None, level=None, 
        description=None
    ):
        self.focuses:Focuses = focuses
        self.focus_name: str = name
        self.ability: str = ability
        self._level = level
        self.description: str = None

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



