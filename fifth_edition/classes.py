"""Character class information"""

from fifth_edition import input_tools
from fifth_edition import characters

__author__ = "Grant Colasurdo"


class CharacterClass:
    """The base character class"""
    def __init__(self, character: characters.Character, class_name: str):
        self.character = character
        self.class_name = class_name
        self.description = None
        self.ability_score_increases: set = set()
        self.hit_die: str = None
        self.starting_equipment: set = set()

    def calculate_starting_health(self):
        die_roll = int(input_tools.input_response(
            "Roll 1d6 for your starting health calculation",
            [str(x) for x in range(1, 7)]
        ))
        constitution = self.character.abilities.constitution.value
        starting_health = die_roll + constitution + self.base_health
        print("Your character now has a maximum health of " + str(starting_health))
        return die_roll + constitution + self.base_health

    def init_class(self):
        self.character.max_health = self.calculate_starting_health()


class Subclass:
    def __init__(self, subclass_name: str, parent: CharacterClass):
        self.parent_class = parent
        self.subclass_name = subclass_name
        self.description = None


class Barbarian(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Barbarian")
        self.description = "A fierce warrior of primitive background who can enter a battle rage"
        self.hit_die = "d12"


class Bard(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Bard")
        self.description = "An inspiring magician whose power echoes the music of creation"
        self.hit_die = "d8"


class Cleric(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Cleric")
        self.description = "A priestly champion who wields divine magic in service of a higher power"
        self.hit_die = "d8"


class Druid(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Druid")
        self.description = "A priest of the Old Faith, wielding the powers of nature - moonlight and plant " +\
            "growth, fire and lightning - and adoption animal forms"
        self.hit_die = "d8"


class Fighter(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Fighter")
        self.description = "A master of martial combat, skilled with a variety of weapons and armor"
        self.hit_die = "d10"


class Monk(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Monk")
        self.description = "A master of martial arts, harnessing the power of the body in pursuit of " +\
            "physical and spiritual perfection"
        self.hit_die = "d8"


class Paladin(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Paladin")
        self.description = "A holy warrior bound to a sacred oath"
        self.hit_die = "d10"


class Ranger(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Ranger")
        self.description = "A warrior who uses martial prowess and nature magic to combat threats on " +\
            "the edge of civilization"
        self.hit_die = "d10"


class Rouge(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Rouge")
        self.description = "A scoundrel who uses stealth and trickery to overcome obstacles and enemies"
        self.hit_die = "d8"


class Sorcerer(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Sorcerer")
        self.description = "A spellcaster who draws on inherent magic from a gift or a bloodline"
        self.hit_die = "d6"


class Warlock(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Warlock")
        self.description = "A wielder of magic that is derived from a bargain with an extra-planar entity"
        self.hit_die = "d8"


class Wizard(CharacterClass):
    def __init__(self, character):
        super().__init__(character, "Wizard")
        self.description = "A scholarly magic-user capable of manipulating the structures of reality"
        self.hit_die = "d8"


CLASS_DICT = {
    "Barbarian": Barbarian,
    "Bard": Bard,
    "Cleric": Cleric,
    "Druid": Druid,
    "Fighter": Fighter,
    "Monk": Monk,
    "Paladin": Paladin,
    "Ranger": Ranger,
    "Rogue": Rouge,
    "Sorcerer": Sorcerer,
    "Warlock": Warlock,
    "Wizard": Wizard
}


def init_class():
    chosen_class = input_tools.input_response(
        "Choose your Character Class",
        CLASS_DICT.keys()
    )
    return CLASS_DICT[chosen_class]
