"""
The Idea behind this project is that I'll be able to use it as a tool in
keeping track of all the stats, numbers and calculations that go into an AGE
based roll playing game. The template that I'm building this off of is Titan's
Grave. 
"""
def inputresponse(caption, options)
    print(caption)
    print(options)
    while choice not in options:
        option = input('')
    return option


class Character:
    """This is the character object that holds a character's attributes"""
    def __init__(self):
        self.character_name = None
        self.max_health = None
        self.current_health = None
        self.max_mana = None
        self.current_mana = None
        self.level = None
        self.experience_points = None
        self.abilities: Abilities = Abilities(self)
        self.focuses: set = None
        self.weapon_groups: set = None
        self.talents: set = None
        self.character_class: CharacterClass  = CharacterClass(self)
        self.specializations: set = None
        self.race = None

        def rest(self):
            self.current_health = self.max_health
            self.current_mana = self.max_mana

        def init_new_character(self):
            pass

class CharacterClass:
    def __init__(self, character):
        self.character = character
        self.class_name = None
        self.primary_abilities = None
        self.secondary_abilities = None
        self.level_bonuses = None


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
        
    def level_up(self):
        if self.character.level % 2 == 0:
            available_abilities =\
                self.character.character_class.primary_abilities
        else:
            available_abilities =\
                    self.character.character_class.secondary_abilities
        print("Choose an ability to level up")
        print(available_abilities)
        good_input = False
        while good_input is False:
            try:    
                choice = good_input("Chose a number ")
                ability == available_abilities[choice + 1]
                good_input = True
            except Exception:
                print("Bad input")
        self._level_log.append(ability)

    @property
    def accuracy(self):
        levelups = sum(
            1 if ability == "accuracy" else 0 for ability in self._level_log
        )
        reutrn self.accuracy_start + levelups

    @property
    def communication(self):
        levelups = sum(
            1 if ability == "communication" else 0 for ability in self._level_log
        )
        reutrn self.communication_start + levelups

    @property
    def constitution(self):
        levelups = sum(
            1 if ability == "constitution" else 0 for ability in self._level_log
        )
        reutrn self.constitution_start + levelups


    @property
    def dexterity(self):
        levelups = sum(
            1 if ability == "dexterity" else 0 for ability in self._level_log
        )
        reutrn self.dexteritystart + levelups


    @property
    def fighting(self):
        levelups = sum(
            1 if ability == "fighting" else 0 for ability in self._level_log
        )
        reutrn self.fighting_start + levelups


    @property
    def intelligence(self):
        levelups = sum(
            1 if ability == "intelligence" else 0 for ability in self._level_log
        )
        reutrn self.intelligence_start + levelups


    @property
    def perception(self):
        levelups = sum(
            1 if ability == "perception" else 0 for ability in self._level_log
        )
        reutrn self.perception_start + levelups

    @property
    def strength(self):
        levelups = sum(
            1 if ability == "strength" else 0 for ability in self._level_log
        )
        reutrn self.strength_start + levelups

    @property
    def willpower(self):
        levelups = sum(
            1 if ability == "willpower" else 0 for ability in self._level_log
        )
        reutrn self.willpower_start + levelups


class Spell:
    def __init__(self):
        self._arcana = None
        self._target_number = 0
        self._requirement = None
        self._description = None
        self._mp_cost = None
        self._casting_time = None
        self._test = None
        self._effect = []


class Focus:
    def __init__(self):
        self.focus_name = None
        self.ability: str = None
        self.upgrade = None
        self.description: str = None


class Talent:
    def __init__(self):
        self.talent_name: str = None
        self.class_requirement: set = None
        self.other_requirements: set = None
        self.description: str = None
        self.novice_description: str = None
        self.journeyman_description: str = None
        self.master_description: str = None


class Item:
    def __init__(self, name, weight, size, value):
        self.item_name: str = name
        self.weight: float = weight
        self.size: float = size
        self.value: float = value
        self.hands_to_weild: int = None


class Currency(Item):
    def __init__(self, name, weight, size, value):
        super().__init__(name, weight, size, value)
        

class Weapon(Item):
    def __init__(
        self, name, weight, size, value, weapon_group, minimum_strength,
        min_range, max_range
    ):
        super().__init__(name, weight, size, value)
        self._damage_rolls = None
        self._weapon_group = None
        self._minimum_strength = None
        self._state = None
        self._max_range = None
        self._min_range = None


class MissleWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self._missle_used = None


class Armor(Item):
    def __init__(self):
        super().__init__()
        self._rating = None
        self._weight_class = None
        self._penalty = None


class Shield(Item):
    def __init__(self):
        super().__init__()
        self._weight_class = None
        self._defense_modifier = None


class State:
    def __init__(self):
        self._name = None
        self._emburdened = None


class Action:
    def __init__(self):
        self._name = None
        self._type = None
        self._cost = None
        self._required_state = None



class MajorAction(Action):
    def __init__(self):
        super().__init__()
        self._
