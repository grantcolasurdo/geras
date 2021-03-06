"""
The Idea behind this project is that I'll be able to use it as a tool in
keeping track of all the stats, numbers and calculations that go into an AGE
based roll playing game. The template that I'm building this off of is Titan's
Grave.
"""

from fifth_edition import abilities, races, languages, backgrounds, classes, input_tools, inventory, magic
from fifth_edition import items

__author__ = "Grant Colasurdo"

EXPERIENCE_TABLE = {
    "0": 1,
    "300": 2,
    "900": 3,
    "2700": 4,
    "6500": 5,
    "14000": 6,
    "23000": 7,
    "34000": 8,
    "48000": 9,
    "64000": 10,
    "85000": 11,
    "100000": 12,
    "120000": 13,
    "140000": 14,
    "165000": 15,
    "195000": 16,
    "225000": 17,
    "265000": 18,
    "305000": 19,
    "355000": 20
}


class Character:
    """This is the character object that holds a character's attributes"""
    def __init__(self):
        self._first_name: str = None
        self._last_name: str = None
        self._sex: str = None
        self._hit_die: set = None
        self.max_health: int = None
        self.current_health: int = None
        self.experience_points = None
        self.initial_abilities: set() = None
        self.character_classes: set() = None
        self._class_level_list = [None] * 20
        self.specializations: set = None
        self.race: races.Race = None
        #  self.inventory = inventory.Inventory
        self.magic: magic = None
        self.base_speed: int = None

    @property
    def full_name(self) -> str:
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

    @property
    def sex(self) -> str:
        return self._sex

    @sex.setter
    def sex(self, value: str):
        self._sex = value

    @property
    def level(self) -> int:
        level_return = 0
        for level in range(1, len(EXPERIENCE_TABLE) + 1):
            if self.experience_points > EXPERIENCE_TABLE[level]:
                level_return += 1
        return level_return

    @property
    def hit_die(self) -> set:
        return_set = set()
        for character_class in self._class_level_list:
            if isinstance(character_class, classes.CharacterClass):
                return_set.add(character_class.hit_die)
        return return_set

    @property
    def strength(self) -> abilities.Strength:
        temp_score = 0
        temp_score += abilities.sum_ability_sources(abilities.Strength, self.race.ability_score_increases)
        temp_score += abilities.sum_ability_sources(abilities.Strength, self.ability_score_increases)
        return abilities.Strength(temp_score)

    @property
    def dexterity(self) -> abilities.Ability:
        temp_score = 0
        temp_score += abilities.sum_ability_sources(abilities.Dexterity, self.race.ability_score_increases)
        return abilities.Dexterity(temp_score)

    @property
    def constitution(self) -> abilities.Ability:
        temp_score = 0
        temp_score += abilities.sum_ability_sources(abilities.Constitution, self.race.ability_score_increases)
        return abilities.Constitution(temp_score)

    @property
    def intelligence(self) -> abilities.Ability:
        temp_score = 0
        temp_score += abilities.sum_ability_sources(abilities.Intelligence, self.race.ability_score_increases)
        return abilities.Intelligence(temp_score)

    @property
    def wisdom(self) -> abilities.Ability:
        temp_score = 0
        temp_score += abilities.sum_ability_sources(abilities.Wisdom, self.race.ability_score_increases)
        return abilities.Wisdom(temp_score)

    @property
    def charisma(self) -> abilities.Ability:
        temp_score = 0
        temp_score += abilities.sum_ability_sources(abilities.Charisma, self.race.ability_score_increases)
        return abilities.Charisma(temp_score)

    @property
    def proficiency_bonus(self) -> int:
        return (self.level - 1) // 4 + 2

    def rest(self):
        self.current_health = self.max_health
        if self.magic is not None:
            self.magic.current_mana = self.magic.max_mana

    def init_new_character(self):
        """
        The guidebook shows the character creation process in 9 points
        1. Choose a race
        2. Choose a class
        3. Determine ability scores
        4. Choose a background
        5. Choose equipment
        """
        self.experience_points = 0
        self._choose_race()
        self._choose_class()
        self._determine_abilities()
        self._determine_background()
        self._pick_starting_equipment()

    def _choose_race(self):
        self.languages = set()
        race = races.choose_race()
        race.character = self
        self.race = race
        self.race.init_race()

    def _choose_class(self):
        self.character_class = classes.init_class()(self)

    def _determine_background(self):
        self.background = backgrounds.init_character(self)

    def _determine_abilities(self):

        ability_options = {
            "Standard D&D": self._d_and_d_init_abilities,
            "Purchase with Points": self._purchase_abilities,
            "I'm feeling lucky": self._roll_abilities
        }
        ability_function = ability_options[
            input_tools.input_response(
                "How would you like to determine your starting abilities?",
                ability_options
            )
        ]
        ability_function()

#    def _d_and_d_init_abilities(self):
#        ability_list = {ability for ability in abilities.ABILITY_LIST}
#        score_list = [15, 14, 13, 12, 10, 8]
#        choice_list = set()
#        while len(score_list) > 0:
#            iterator

    def _purchase_abilities(self):
        pass

    def _roll_abilities(self):
        pass

    def _pick_starting_equipment(self):
        items.init_items(self)

    def _pick_name(self):
        self.first_name = input_tools.prompt_text(
            "What is your character's first name?"
        )
        self.last_name = input_tools.prompt_text(
            "What is your character's last name?"
        )
        print("Hello, " + " ".join((self.first_name, self.last_name)))


def dark_sight(character: Character, value: bool):
    character.dark_sight = value


def base_speed(character: Character, value: int):
    character.base_speed = value
