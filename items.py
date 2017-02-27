"""This is a repository for items in AGE"""

__author__ = "Grant Colasurdo"

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
