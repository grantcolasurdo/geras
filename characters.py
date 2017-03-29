"""
The Idea behind this project is that I'll be able to use it as a tool in
keeping track of all the stats, numbers and calculations that go into an AGE
based roll playing game. The template that I'm building this off of is Titan's
Grave.
"""

import spells
import talents
import items
import focuses
import classes
import races
import abilities
import input_tools
import languages

__author__ = "Grant Colasurdo"


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
        self.abilities: abilities.Abilities = None
        self.focuses: focuses.Focuses = None
        self.talents: talents.Talents = None
        self.languages: languages.Languages = None
        self.weapon_groups: set = None
        self.talents: set = None
        self.character_class: classes.CharacterClass = None
        self.specializations: set = None
        self.race: races.Race = None
        self.magic: spells.Magic = None
        self.items: items.Items = None

    def rest(self):
        self.current_health = self.max_health
        if self.magic is not None:
            self.magic.current_mana = self.magic.max_mana

    def init_new_character(self):
        """
        The guidebook shows the character creation process in 9 points
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
        self.abilities = abilities.Abilities(self)
        self.abilities.init_abilities()

    def _choose_race(self):
        self.languages = languages.Languages(self)
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
        self.first_name = input_tools.input_response(
            "What is your character's first name?"
        )
        self.last_name = input_tools.input_response(
            "What is your character's last name?"
        )
        print("Hello, " + " ".join((self.first_name, self.last_name)))

    def _choose_goals_and_ties(self):
        pass
