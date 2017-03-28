"""This is a repository for items in AGE"""

__author__ = "Grant Colasurdo"


class Items:
    def __init__(self, character):
        self.character = character


class Item:
    def __init__(self, **kwargs):
        self.item_name: str = None
        self.weight: float = None
        self.size: float = None
        self.value: float = None
        self.hands_to_wield: int = None
        for key, value in kwargs.items():
            try:
                assert key in self.__dict__
                self.__dict__[key] = value
            except AssertionError:
                print("There is no key " + key + " in this item")


class Currency(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Container(Item):
    def __init__(self, **kwargs):
        self._weight = None
        self.items = set()
        self.volume_capacity = None
        self.weight_capacity = None
        super(Container, self).__init__(**kwargs)

    @property
    def weight(self) -> float:
        contained_weight = sum([item.weight for item in self.items])
        return contained_weight + self.self_weight

    @weight.setter
    def weight(self, value: float):
        self._weight = value

    @property
    def self_weight(self) -> float:
        return self._weight

    @self_weight.setter
    def self_weight(self, value: float):
        self._weight = value

    @property
    def remaining_weight(self):
        return self.weight_capacity - self.weight

    @property
    def occupied_space(self):
        return sum([item.size for item in self.items])

    @property
    def remaining_space(self):
        return self.volume_capacity - self.occupied_space

    def insert(self, item: Item):
        try:
            assert self.remaining_space >= item.size
            self.items.add(item)
        except AssertionError:
            print("There is not enough space or spare weight in the container to add")

    def remove(self, item: Item):
        try:
            assert item in self.items
            self.items.remove(item)
        except AssertionError:
            print("That item is not in the container")


class Weapon(Item):
    def __init__(self, **kwargs):
        self._damage_rolls = None
        self._weapon_group = None
        self._minimum_strength = None
        self._state = None
        self._max_range = None
        self._min_range = None
        super().__init__(**kwargs)


class MissileWeapon(Weapon):
    def __init__(self, ):
        super().__init__()
        self._missile_used = None


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
        self._burdened = None


class Action:
    def __init__(self):
        self._name = None
        self._type = None
        self._cost = None
        self._required_state = None


class MajorAction(Action):
    def __init__(self):
        super().__init__()
