"""
The Idea behind this project is that I'll be able to use it as a tool in
keeping track of all the stats, numbers and calculations that go into an AGE
based roll playing game. The template that I'm building this off of is Titan's
Grave. 
"""
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
        self.class_name

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
        if character.character_class.class_name == "Warrior"
            self.
        

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
        self.universe_availability: str = None  # Which expansion can you find this


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
    def __init__(self):
        self.item_name: str = None
        self.weight: float = None
        self.size: float = None
        self.value: float = None
        self.hands_to_weild: int = None


class Weapon(Item):
    def __init__(self):
        super().__init__()
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
