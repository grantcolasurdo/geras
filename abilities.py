"""This is where abilities will be defined"""

import geras.die
import geras.input_tools as input_tools

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
        self._willpower = None
        self.ability_map = {
            "Accuracy": self._accuracy,
            "Communication": self._communication,
            "Constitution": self._constitution,
            "Dexterity": self._dexterity,
            "Fighting": self._fighting,
            "Intelligence": self._intelligence,
            "Perception": self._perception,
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

    determine_ability_table = {
        3:-2, 4:-1, 5:-1, 6:0, 7:0, 8:0, 9:1, 10:1, 11:1, 12:2, 13:2,
        14:2, 15:3, 16:3, 17:3, 18:4
    }

    def init_abilities(self):
        for ability in ABILITY_LIST:
            self.ability_map[ability] = Ability(
                self,
                ability, 
                self.determine_ability_table[
                    int(
                        input_tools.InputResponse(
                            "Roll for " + ability,
                            [str(x) for x in range(3,19)]
                        )
                    )
                ]
            )
            print(ability + " " + str(self.ability_map[ability].value))

        if input_tools.InputResponse(
            "Do you want to switch the values for two abilities? ", ["yes", "no"]
        ) == "yes":
            pass
        print(self._accuracy)
        print(self._communication)
        print(self._constitution)
        print(self._dexterity)
        print(self._fighting)
        print(self._intelligence)
        print(self._strength)
        print(self._willpower)



    @property
    def accuracy(self):
        return self._accuracy.value

    @property
    def communication(self):
        return self._communication.value

    @property
    def constitution(self):
        return self._constitution.value

    @property
    def dexterity(self):
        return self._dexterity.value

    @property
    def fighting(self):
        return self._fighting.value

    @property
    def intelligence(self):
        return self._intelligence.value

    @property
    def perception(self):
        return self._perception.value

    @property
    def strength(self):
        return self._strength.value

    @property
    def willpower(self):
        return self._willpower.value


class Ability:
    """Base class for an individual Ability"""
    def __init__(
        self, abilities=None, ability_name=None, starting_value=0
    ):
        self.abilities = abilities
        self.ability_name = ability_name
        self.ability_log = [(0,0,"Initialization")]
        while self.value > starting_value:
            self.perminent_subtract("Initialization")

        while self.value < starting_value:
            self.perminent_add("Initialization")


    def perminent_add(self, source):
        self.ability_log.append((
            1,
            self.abilities.character.level,
            source
        ))

    def perminent_subtract(self,source):
        self.ability_log.append((
            -1,
            self.abilities.character.level,
            source
        ))

    @property
    def value(self):
        return sum(entry[0] for entry in self.ability_log) 
    

