"""This is a repository for items in AGE"""

import csv

__author__ = "Grant Colasurdo"


class Items:
    """This class manages the meta-info of """
    def __init__(self, character):
        self.character = character


class Item:
    def __init__(self, csv_row):
        self.item_name: str = csv_row['item_name']
        self.weight: float = csv_row['weight']
        self.size: float = csv_row['size']
        self.value: float = csv_row['value']
        self.hands_to_wield: int = csv_row['hands_to_wield']


class Dress:
    """Handle the meta data for clothing worn by a character
    
    Notes
    -----
    Attributes link to places that clothes can be worn. Some positions have 3 layers represented by placement on a list.
    [Under, Normal, Over]
    """
    def __init__(self, character):
        self.character = character
        self.feet = [None]*3
        self.legs = [None]*3
        self.waist = [None]*3
        self.torso = [None]*3
        self.over_wear = [None]*3
        self.head = [None]*3
        self.face = [None]*3
        self.hands = [None]*3
        self.back = [None]*3


class WearPosition:
    """Each wear slot can hold 1 clothing or armor item"""
    def __init__(self, dress: Dress):
        self.dress = dress
        self._item = None  # The normal spot for most clothing





class Currency(Item):
    def __init__(self, csv_row):
        super().__init__(csv_row)


class Container(Item):
    def __init__(self, csv_row):
        super(Container, self).__init__(csv_row)
        self._weight = None
        self.items = set()
        self.volume_capacity = csv_row['volume_capacity']
        self.weight_capacity = csv_row['weight_capacity']
        self.lock = None

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
    def __init__(self, csv_row):
        super().__init__(csv_row)
        self.damage_rolls = csv_row['weapon_damage']
        self.weapon_group = csv_row['weapon_group']
        self.minimum_strength = csv_row['minimum_strength']
        self.state = None
        self.long_range = csv_row['short_range']
        self.short_range = csv_row['maximum_range']
        self.minimum_range = csv_row['minimum_range']


class Missile(Weapon):
    def __init__(self, csv_row):
        self.missile_used = None
        super().__init__(csv_row)


class Armor(Item):
    def __init__(self, csv_row):
        self.rating = csv_row['armor_rating']
        self.weight_class = csv_row['armor_weight_class']
        self.penalty = csv_row['armor_penalty']
        self.strain = csv_row['armor_strain']
        super().__init__(csv_row)


class Shield(Item):
    def __init__(self, csv_row):
        self.weight_class = csv_row['armor_weight_class']
        self.defense_modifier = csv_row['shield_bonus']
        super().__init__(csv_row)


class Lock(Item):
    def __init__(self, csv_row):
        self.is_locked = None
        super().__init__(csv_row)


class Tool(Item):
    def __init__(self, csv_row):
        super(Tool, self).__init__(csv_row)


class Traveling(Item):
    def __init__(self, csv_row):
        super(Traveling, self).__init__(csv_row)


class Clothing(Item):
    def __init__(self, csv_row):
        super(Clothing, self).__init__(csv_row)


class TradeGoods(Item):
    def __init__(self, csv_row):
        super(TradeGoods, self).__init__(csv_row)


class ProfessionalGear(Item):
    def __init__(self, csv_row):
        super(ProfessionalGear, self).__init__(csv_row)


class HomeAndHearth(Item):
    def __init__(self, csv_row):
        super(HomeAndHearth, self).__init__(csv_row)


class FoodAndLodging(Item):
    def __init__(self, csv_row):
        super(FoodAndLodging, self).__init__(csv_row)


class State:
    def __init__(self):
        self._name = None
        self._burdened = None


class Equipment:
    """This will manage the meta level information for the items worn by a character"""
    def __init__(self, character):
        self.character = character
        self.all_items = set()  # All the items being worn, not all the item held by the character
        self.primary_hand = None  # Link to an item that the primary hand is holding
        self.secondary_hand = None  # Link to an item that the secondary hand is holding
        self._backpack = None  # Link to an item that is worn on the character's back

    @property
    def armor_value(self) -> int:
        """The amount of protection your armor affords you"""
        return self.armor.rating

    @property
    def armor_penalty(self) -> int:
        """The penalty applied to speed and Dexterity if untrained in the armor class"""
        return self.armor.penalty

    @property
    def armor_strain(self):
        """The penalty applied to magic rolls"""
        return self.armor.strain

    @property
    def armor(self) -> Armor:
        """Return the armor object being worn by the character"""
        return self.character.wear.armor

    @armor.setter
    def armor(self, value: Armor):
        self.character.wear.armor = value

    @property
    def shield_bonus(self):
        """Return the bonus to defense gained from having a shield"""
        bonus_value = 0
        try:
            bonus_value = max(self.primary_hand.defense_modifier, bonus_value)
        except AttributeError:
            pass
        try:
            bonus_value = max(self.secondary_hand.defense_modifer, bonus_value)
        except AttributeError:
            pass
        return bonus_value

    @property
    def backpack(self):
        return

    @backpack.setter
    def backpack(self, value: Container):
        self.character

ITEM_CLASS_DICT = {
    "Currency": Currency,
    "Container": Container,
    "Item": Item,
    "Lock": Lock,
    "Tool": Tool,
    "Missile": Missile,
    "Traveling": Traveling,
    "Clothing": Clothing,
    "Trade Goods": TradeGoods,
    "Professional Gear": ProfessionalGear,
    "Home and Hearth": HomeAndHearth,
    "Food and Lodging": FoodAndLodging,
    "Weapon": Weapon,
    "Armor": Armor,
    "Shield": Shield
}


def new_item(item_name) -> Item:
    item = None
    with open('items.csv', 'r') as file:
        item_db = csv.DictReader(file)
        for row in item_db:
            if row['item_name'] == item_name:
                item_class = row['item_class']
                class_to_call = ITEM_CLASS_DICT[item_class]
                item = class_to_call(row)

    return item


def init_items(character):
    character = character
    character.equipment = Equipment(character)
    character.items = Items(character)
    starting_items = set()
    starting_items.add(new_item("Backpack"))


