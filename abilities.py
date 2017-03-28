"""This is where abilities will be defined"""

import input_tools

__author__ = "Grant Colasurdo"

ABILITY_LIST = (
    'Accuracy',
    "Communication",
    "Constitution",
    "Dexterity",
    "Fighting",
    "Intelligence",
    "Perception",
    "Strength",
    "Willpower"
)

DETERMINE_ABILITY_TABLE = {
    3: -2,
    4: -1,
    5: -1,
    6: 0,
    7: 0,
    8: 0,
    9: 1,
    10: 1,
    11: 1,
    12: 2,
    13: 2,
    14: 2,
    15: 3,
    16: 3,
    17: 3,
    18: 4
}

def level_up(character, ablity_string, source):
    character.Abilities.level_up(ability_name, source)

class Abilities:

    def __init__(
        self, character, initial_abilities=None
    ):
        self.character = character
        self._accuracy = None
        self._communication = None
        self._constitution = None
        self._dexterity = None
        self._fighting = None
        self._intelligence = None
        self._perception = None
        self._strength = None
        self._willpower = None
        self.ability_map = {
            "Accuracy": self._accuracy,
            "Communication": self._communication,
            "Constitution": self._constitution,
            "Dexterity": self._dexterity,
            "Fighting": self._fighting,
            "Intelligence": self._intelligence,
            "Perception": self._perception,
            "Strength": self._strength,
            "Willpower": self._willpower
        }
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
            self.ability_map[ability_map].permanent_add(source)
        except SetException:
            print(
                "A bad string value was sent to an Abilities object (" +
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
            ability_pool = ABILITY_LIST.copy()
            print("Chose first skill")
            for ability in ability_pool:
                print(ability)
            first_ability = ability_pool.pop(
                input_tools.input_response(
                    "Pick an ability",
                    ability_pool
                )
            )
            second_ability = ability_pool.pop(
                input_tools.input_response(
                    "Pick a second ability",
                    ability_pool
                )
            )

            

        else:
            pass
        print(self.accuracy)
        print(self.communication)
        print(self.constitution)
        print(self.dexterity)
        print(self.fighting)
        print(self.intelligence)
        print(self.strength)
        print(self.willpower)

    @property
    def accuracy(self):
        return self.ability_map["Accuracy"]

    @property
    def communication(self):
        return self.ability_map["Communication"]

    @property
    def constitution(self):
        return self.ability_map["Constitution"]

    @property
    def dexterity(self):
        return self.ability_map["Dexterity"]

    @property
    def fighting(self):
        return self.ability_map["Fighting"]

    @property
    def intelligence(self):
        return self.ability_map["Intelligence"]

    @property
    def perception(self):
        return self.ability_map["Perception"]

    @property
    def strength(self):
        return self.ability_map["Strength"]

    @property
    def willpower(self):
        return self.ability_map["Willpower"]


class Ability:
    """Base class for an individual Ability"""
    def __init__(
        self, abilities=None, ability_name=None, starting_value=0
    ):
        self.abilities = abilities
        self.ability_name = ability_name
        self.ability_log = [(0, 0, "Initialization")]
        while self.value > starting_value:
            self.permanent_subtract("Initialization")

        while self.value < starting_value:
            self.permanent_add("Initialization")

    def permanent_add(self, source):
        self.ability_log.append((
            1,
            self.abilities.character.level,
            source
        ))

    def permanent_subtract(self, source):
        self.ability_log.append((
            -1,
            self.abilities.character.level,
            source
        ))

    @property
    def value(self):
        return sum(entry[0] for entry in self.ability_log) 
    

