"""
The Idea behind this project is that I'll be able to use it as a tool in
keeping track of all the stats, numbers and calculations that go into an AGE
based roll playing game. The template that I'm building this off of is Titan's
Grave.
"""

__author__ = "Grant Colasurdo"

import geras.spells as spells
import geras.talents as talents
import geras.items as items
import geras.classes as classes
import geras.races as races
import geras.abilities
import geras.input_tools as input_tools

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
        self._create_character_concept()
        self._determine_abilities()
        self._choose_race()
        self._determine_background()
        self._choose_class()
        self._pick_starting_equipment()
        self._calculate_defense()
        self._pick_name()
        self._choose_goals_and_ties()

    def _create_character_concept(self):
        pass

    def _determine_abilities(self):
        self.abilities = geras.abilities.Abilities(self)
        self.abilities.init_abilities()

    def _choose_race(self):
        self.race = races.Race(self)
        self.race.init_race()

    def _determine_background(self):
        pass

    def _choose_class(self):
        self.character_class = classes.CharacterClass(self)
        self.character_class.init_class()

    def _pick_starting_equipment(self):
        pass

    def _calculate_defense(self):
        pass

    def _pick_name(self):
        self.first_name =InputResponse("What is your character's first name?")
        self.last_name = InputResponse("What is your character's last name?")
        print("Hello, " + " ".join((self.first_name,self.last_name)))

    def _choose_goals_and_ties(self):
        pass


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
        self, focuses=None, name=None, ability=None, level=None, 
        description=None
    ):
        self.focuses = focuses
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



