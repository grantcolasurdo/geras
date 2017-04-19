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
import weapon_groups
import backgrounds

__author__ = "Grant Colasurdo"


class Character:
    """This is the character object that holds a character's attributes"""
    def __init__(self):
        self.character_name: str = None
        self._first_name: str = None
        self._last_name: str = None
        self.max_health: int = None
        self.current_health: int = None
        self.level: int = None
        self.experience_points = None
        self.abilities: abilities.Abilities = None
        self.focuses: focuses.Focuses = focuses.Focuses(self)
        self.talents: talents.Talents = talents.Talents(self)
        self.languages: languages.Languages = languages.Languages(self)
        self.weapon_groups: set = weapon_groups.WeaponGroups(self)
        self.character_class: classes.CharacterClass = None
        self.wear = items.Wear(self)
        self.specializations: set = None
        self.race: races.Race = None
        self.magic: spells.Magic = None
        self.items: items.Items = None
        self.base_speed: int = None

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

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
        self.level = 1
        self.experience_points = 0

    def _determine_abilities(self):
        self.abilities = abilities.Abilities(self)
        self.abilities.init_abilities()

    def _choose_race(self):
        self.languages = languages.Languages(self)
        race = races.choose_race()
        self.race = race(character=self)
        self.race.init_race()

    def _determine_background(self):
        self.background = backgrounds.init_character(self)

    def _choose_class(self):
        self.character_class = classes.init_class()(self)

    def _pick_starting_equipment(self):
        items.init_items(self)

    def _calculate_defense(self):
        pass

    def _pick_name(self):
        self.first_name = input_tools.prompt_text(
            "What is your character's first name?"
        )
        self.last_name = input_tools.prompt_text(
            "What is your character's last name?"
        )
        print("Hello, " + " ".join((self.first_name, self.last_name)))

    def _choose_goals_and_ties(self):
        pass


def dark_sight(character: Character, value: bool):
    character.dark_sight = value


def base_speed(character: Character, value: int):
    character.base_speed = value
