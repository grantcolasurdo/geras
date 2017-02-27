"""
The Idea behind this project is that I'll be able to use it as a tool in
keeping track of all the stats, numbers and calculations that go into an AGE
based roll playing game. The template that I'm building this off of is Titan's
Grave. 
"""

__author__ = "Grant Colasurdo"

import geras.spells
import geras.talents
import geras.items

def InputResponse(caption, options):
    print(caption)
    print(' '.join(options))
    choice = input('')
    while choice not in options:
        choice = input('Try again ')
    return choice


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
        self.abilities = Abilities(self)
        self.abilities.init_abilities()

    def _choose_race(self):
        self.race = Race(self)
        self.race.init_race()

    def _determine_background(self):
        pass

    def _choose_class(self):
        self.character_class = CharacterClass(self)
        self.character_class.init_class()

    def _pick_starting_equipment(self):
        pass

    def _calculate_defense(self):
        pass

    def _pick_name(self):
        self.first_name =InputResponse("What is your character's first name?")
        self.last_name = InputResponse("What is your character's last name?")

    def _choose_goals_and_ties(self):
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

    def init_abilities(self):
        self.accuracy_start = self.determine_ability_table[
            int(InputResponse("Roll for Accuracy", [
                str(x) for x in range(3,19)
            ]))
        ]
        self.communication_start = self.determine_ability_table[
            int(InputResponse("Roll for Communication", [
                str(x) for x in range(3,19)
            ]))
        ]
        self.constitution_start = self.determine_ability_table[
            int(InputResponse("Roll for Constitution", [
                str(x) for x in range(3,19)
            ]))
        ]
        self.dexterity_start = self.determine_ability_table[
            int(InputResponse("Roll for Dexterity", [
                str(x) for x in range(3,19)
            ]))
        ]
        self.fighting_start = self.determine_ability_table[
            int(InputResponse("Roll for Fighting", [
                str(x) for x in range(3,19)
            ]))
        ]
        self.intelligence_start = self.determine_ability_table[
            int(InputResponse("Roll for Intelligence", [
                str(x) for x in range(3,19)
            ]))
        ]
        self.perception_start = self.determine_ability_table[
            int(InputResponse("Roll for Perception", [
                str(x) for x in range(3,19)
            ]))
        ]
        self.willpower_start = self.determine_ability_table[
            int(InputResponse("Roll for Willpower", [
                str(x) for x in range(3,19)
            ]))
        ]
        if InputResponse(
            "Do you want to switch the values for two abilities? ", ["yes", "no"]
        ) == "yes":
            pass



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



