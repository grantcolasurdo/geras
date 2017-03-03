"""Character class information"""

__author__ = "Grant Colasurdo"

import geras.input_tools as input_tools

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
        self.class_name = name
        self.primary_abilities = primary_abilities
        self.secondary_abilities = secondary_abilities
        self.level_bonuses = None
        self.base_health = 0

    def calculate_starting_health(self):
        die_roll = input_tools.InputResponse(
            "Roll 1d6 for your starting health calculation",
            [str(x) for x in range(1,7)]
        )
        constitution = self.character.abilities.constitution
        starting_health = die_roll + constitution + self.base_health
        print("Your character now has " + starting_health + " health")
        return die_roll + constitution + self.base_health

    def init_class(self):
        self.character.max_health = self.calculate_starting_health()

class Warrior(CharacterClass):
    def __init__(self, character):
        super().__init__(
            self,
            character,
            "Warrior",
            {
                "Strength",
                "Constitution",
                "Fighting",
                "Dexterity"
            },
            {
                "Accuracy"
                ,"Communication"
                ,"Intelligence"
                ,"Percption"
                ,"Willpower"
            },
            []
        )
        self.base_health = 30

class Mage(CharacterClass):
    def __init__(self, character):
        super().__init__(
            self,
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
            []
        )
        self.base_health = 20

class Rouge(CharacterClass):
    def __init__(self, character):
        super().__init__(
            self,
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
            []
        )
        self.base_health = 25
