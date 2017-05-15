"""This is where abilities will be defined"""

from fifth_edition import input_tools
from fifth_edition import characters

__author__ = "Grant Colasurdo"

ABILITY_LIST = ('Strength', "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma")

DETERMINE_ABILITY_TABLE = {
    3: -2, 4: -1, 5: -1, 6: 0, 7: 0, 8: 0, 9: 1, 10: 1,
    11: 1, 12: 2, 13: 2, 14: 2, 15: 3, 16: 3, 17: 3, 18: 4
}


def level_up(character, ability_name, source):
    character.abilities.level_up(ability_name, source)


def ability_greater_than(character, ability_name, compared_to):
    return character.abilities.ability_map[ability_name] > compared_to


class Ability:
    """Manage the ability score for one ability for one character"""
    def __init__(
        self, abilities: Abilities=None, ability_name: str=None, description: str=None
    ):
        self.abilities = abilities
        self.ability_name = ability_name
        self.description = description

    @property
    def score(self) -> int:
        character = self.abilities.character
        background_score = character.background
        classes = set()

        return

    @property
    def modifier(self) -> int:
        return (self.score - 10) // 2


class Abilities:

    ABILITY_SCORE_COST = {"8": 0, "9": 1, "10": 2, "11": 3, "12": 4, "13": 5, "14": 7, "15": 9}

    def __init__(self, character):
        self._character: characters.Character = None
        self._base_communication = None
        self._base_constitution = None
        self._base_dexterity = None
        self._base_intelligence = None
        self._base_strength = None
        self._base_willpower = None
        self.character = character
        if initial_abilities is None:
            initial_abilities = {}
            for ability in ABILITY_LIST:
                initial_abilities[ability] = 0

        for ability in ABILITY_LIST:
            self.ability_map[ability] = Ability(
                self,
                ability, initial_abilities[ability]
            )

    def level_up(self, ability_name, source):
        try:
            assert ability_name in self.ability_map
            self.ability_map[ability_name].permanent_add(source)
        except AssertionError:
            print(
                "A bad value was sent to an Abilities object (" +
                ability_name + ")"
            )

    def init_abilities(self):
        for ability in ABILITY_LIST:
            self.ability_map[ability] = Ability(
                self,
                ability,
                DETERMINE_ABILITY_TABLE[
                    int(
                        input_tools.input_response(
                            "Roll for " + ability,
                            [str(x) for x in range(3, 19)]
                        )
                    )
                ]
            )
            print(ability + " " + str(self.ability_map[ability].value))

        if input_tools.input_response(
            "Do you want to switch the values for two abilities? ",
            ["yes", "no"]
        ) == "yes":
            ability_pool = {ability for ability in ABILITY_LIST}
            print("Chose first skill")
            for ability in ability_pool:
                print(ability)
            first_ability = input_tools.input_response(
                    "Pick an ability",
                    ability_pool
            )

            second_value = self.ability_map[first_ability].value
            ability_pool.remove(first_ability)
            second_ability = input_tools.input_response(
                    "Pick a second ability",
                    ability_pool
            )

            first_value = self.ability_map[second_ability].value
            self.ability_map[first_ability].permanent_set(first_value, "switch abilites")
            self.ability_map[second_ability].permanent_set(second_value, "switch abilities")

        else:
            pass

    @property
    def character(self) -> characters.Character:
        return self._character

    @character.setter
    def character(self, value: characters.Character):
        self._character = value

    @property
    def accuracy(self) -> Ability:
        return self.ability_map["Accuracy"].value

    @property
    def communication(self) -> Ability:
        return self.ability_map["Communication"].value

    @property
    def constitution(self) -> Ability:
        return self.ability_map["Constitution"].value

    @property
    def dexterity(self) -> Ability:
        return self.ability_map["Dexterity"].value

    @property
    def fighting(self) -> Ability:
        return self.ability_map["Fighting"].value

    @property
    def intelligence(self) -> Ability:
        return self.ability_map["Intelligence"].value

    @property
    def perception(self) -> Ability:
        return self.ability_map["Perception"].value

    @property
    def strength(self) -> Ability:
        return self.ability_map["Strength"].value

    @property
    def willpower(self) -> Ability:
        return self.ability_map["Willpower"].value


