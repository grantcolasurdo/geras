"""Character class information"""

from age import input_tools as input_tools

__author__ = "Grant Colasurdo"


class CharacterClass:
    """The base character class"""
    def __init__(
        self,
        character,
        name=None,
        primary_abilities=None,
        secondary_abilities=None,
    ):
        self.character = character
        self.class_name: str = name
        self.primary_abilities: set = primary_abilities
        self.secondary_abilities: set = secondary_abilities
        self.level_bonuses = {}
        self.base_health: int = 0

    def calculate_starting_health(self):
        die_roll = int(input_tools.input_response(
            "Roll 1d6 for your starting health calculation",
            [str(x) for x in range(1, 7)]
        ))
        constitution = self.character.abilities.constitution.value
        starting_health = die_roll + constitution + self.base_health
        print("Your character now has a maximum health of " + str(starting_health))
        return die_roll + constitution + self.base_health

    def init_class(self):
        self.character.max_health = self.calculate_starting_health()


class Warrior(CharacterClass):
    def __init__(self, character):
        super().__init__(
            character,
            "Warrior",
            {
                "Strength",
                "Constitution",
                "Fighting",
                "Dexterity"
            },
            {
                "Accuracy",
                "Communication",
                "Intelligence",
                "Perception",
                "Willpower"
            },
        )
        self.base_health = 30
        self.level_bonuses ={
        }


class Mage(CharacterClass):
    def __init__(self, character):
        super().__init__(
            character,
            "Mage",
            {
                "Accuracy",
                "Intelligence",
                "Perception",
                "Willpower"
            },
            {
                 "Communication",
                 "Constitution",
                 "Dexterity",
                 "Fighting",
                 "Strength"
            },
        )
        self.base_health = 20
        self.level_bonuses = {
        }


class Rouge(CharacterClass):
    def __init__(self, character):
        super().__init__(
            character,
            "Rouge",
            {
                "Accuracy",
                "Communication",
                "Dexterity",
                "Perception"
            },
            {
                "Constitution",
                "Fighting",
                "Intelligence",
                "Strength",
                "Willpower"
            },
        )
        self.base_health = 25


CLASS_DICT = {
    "Warrior": Warrior,
    "Mage": Mage,
    "Rouge": Rouge
}


def init_class():
    chosen_class = input_tools.input_response(
        "Choose your Character Class",
        {"Warrior", "Mage", "Rouge"}
    )
    return CLASS_DICT[chosen_class]
