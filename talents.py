"""Here are all the non-magic talents"""

import classes
import csv
import abilities

__author__ = "Grant Colasurdo"

file = open('talents.csv', 'r')
TALENT_FILE = csv.DictReader(file)


def find_row_by_name(value: str) -> dict:
    for row in TALENT_FILE:
        if row[0] == value:
            return row
    print("Index not found")


class Talent:
    def __init__(
        self,
        talents=None,
        name=None,
        level=None,
    ):
        self.talent_name = name
        db_details = find_row_by_name(self.talent_name)
        self.talents = talents
        self.class_requirements = set()
        if db_details['mage_available']:
            self.class_requirements.add(classes.Mage)
        if db_details['rouge_available']:
            self.class_requirements.add(classes.Rouge)
        if db_details['warrior_available']:
            self.class_requirements.add(classes.Warrior)
        self.description = db_details['description']
        self.novice_description = db_details['novice_description']
        self.journeyman_description = db_details['journeyman_description']
        self.master_description = db_details['master_description']
        if level is None:
            self.level = 0

    def acquire(self, character):
        already_acquired = any(
            isinstance(talent, self.__class__) for talent in character.talents
        )
        eligible = already_acquired and character.character_class in self.class_requirements
        eligible = eligible and self.is_eligible(character)
        if eligible:
            self.talents = character.talents
            character.talents.acquired_talents.add(self)
        else:
            print("Character not eligible to acquire this talent")

    def is_eligible(self, character) -> bool:
        pass

class Talents:
    """The container for aquired talents and manager of talent meta info"""
    def __init__(
        self, character=None, acquired=set()
    ):
        self.character = character
        self.acquired_talents: set = acquired

    @property
    def available_talents(self) -> set:
        """Return a set of talents that are available to a character in it's
        current state"""
        pass

    def list_available_descriptions(self):
        level_index_map = {
            0: 'novice_description',
            1: 'journeyman_description',
            2: 'master_description'
        }
        available_pool = self.available_talents
        unlearned_pool = available_pool - self.acquired_talents
        known_pool = available_pool - unlearned_pool
        print("These are the talents not yet known")
        [print(talent.novice_description) for talent in unlearned_pool]
        print("These are the talents that are upgradeable")
        [
            print(talent.__dict__[level_index_map(talent.level)]) 
            for talent in known_pool
        ]


    def acquire_talent(self, talent):
        """acquire the given talent, or add a level to it"""
        if talent in self.available_talents:
            """The talent is available, now do we already have it?"""
            if talent not in self.acquired_talents:
                self.acquired_talents.add(talent(self))
            self.return_talent(talent).level += 1
        else:
            print("That talent is not available for this character")
    
    def return_talent(self, talent: str) -> Talent:
        """Return a talent form the acquired_talents group"""
        talent_list = {
            individual_talent for individual_talent in self.acquired_talents
            if individual_talent == talent
        }
        if len(talent_list) == 1:
            return talent_list.pop()
        else:
            print("That talent is not acquired yet")



class Alchemy(Talent):
    """You know how to create grenades using alchemical formulas."""
    def __init__(self, talents, level=None):
        super(Alchemy, self).__init__(
            talents,
            "Alchemy",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.intelligence >= 2
        return class_met and other_requirements


class AnimalTraining(Talent):
    """You know how to train animals"""
    def __init__(self, talents, level=None):
        super(AnimalTraining, self).__init__(
            talents,
            "Animal Training",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class ArmorTraining(Talent):
    """Your have learned to fight while wearing armor"""
    def __init__(self, talents, level=None):
        super(ArmorTraining, self).__init__(
            talents,
            "Armor Training",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class ArcheryStyle(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(ArcheryStyle, self).__init__(
            talents,
            "Archery Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.weapon_groups.is_known("Bows")
        return class_met and other_requirements


class Carousing(Talent):
    """You take fun seriously"""
    def __init__(self, talents, level=None):
        super(Carousing, self).__init__(
            talents,
            "Carousing",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = (
            character.abilities.communication >= 1 and
            character.abilities.constitution >= 1
        )
        return class_met and other_requirements


class Chirurgy(Talent):
    """You can treat wounds and illnesses."""
    def __init__(self, talents, level=None):
        super(Chirurgy, self).__init__(
            talents,
            "Chirurgy",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.focuses.is_known("Healing")
        return class_met and other_requirements


class Command(Talent):
    """You are a natural leader"""
    def __init__(self, talents, level=None):
        super(Command, self).__init__(
            talents,
            "Command",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.communication >= 2
        return class_met and other_requirements


class Contacts(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Contacts, self).__init__(
            talents,
            "Contacts",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.communication >= 1
        return class_met and other_requirements


class DualWeaponStyle(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(DualWeaponStyle, self).__init__(
            talents,
            "Dual Weapon Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.dexterity >= 2
        return class_met and other_requirements


class Horsemanship(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Horsemanship, self).__init__(
            talents,
            "Horsemanship",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.focuses.is_known("Riding")
        return class_met and other_requirements


class Intrigue(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Intrigue, self).__init__(
            talents,
            "Intrigue Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.communication >= 2
        return class_met and other_requirements


class Linguistics(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Linguistics, self).__init__(
            talents,
            "Linguistics",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.intelligence >= 1
        return class_met and other_requirements


class Lore(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Lore, self).__init__(
            talents,
            "Lore",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.intelligence >= 2
        return class_met and other_requirements


class MountedCombatStyle(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(MountedCombatStyle, self).__init__(
            talents,
            "Mounted Combat Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.focuses.is_known("Riding")
        return class_met and other_requirements


class Music(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Music, self).__init__(
            talents,
            "Music",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = (
            character.focuses.is_known("Performance") or
            character.focuses.is_known("Musical Lore")
        )
        return class_met and other_requirements


class Observation(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Observation, self).__init__(
            talents,
            "Observation",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.perception >= 2
        return class_met and other_requirements


class Oratory(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Oratory, self).__init__(
            talents,
            "Oratory",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.focuses.is_known("Persuasion")
        return class_met and other_requirements


class PoleWeaponStyle(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(PoleWeaponStyle, self).__init__(
            talents,
            "Pole Weapon Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = (
            character.weapon_groups.is_known("Polearms") or
            character.weapon_groups.is_known("Spears")
        )
        return class_met and other_requirements


class QuickReflexes(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(QuickReflexes, self).__init__(
            talents,
            "Quick Reflexes",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.dexterity >= 2
        return class_met and other_requirements


class Scouting(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Scouting, self).__init__(
            talents,
            "Scouting",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.dexterity >= 2
        return class_met and other_requirements


class SingleWeaponStyle(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(SingleWeaponStyle, self).__init__(
            talents,
            "Single Weapon Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.perception >= 2
        return class_met and other_requirements


class Thievery(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(Thievery, self).__init__(
            talents,
            "Thievery",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.dexterity >= 2
        return class_met and other_requirements


class ThrownWeaponStyle(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(ThrownWeaponStyle, self).__init__(
            talents,
            "Thrown Weapon Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = (
            character.weapon_groups.is_known("Axes") or
            character.weapon_groups.is_known("Light Blades") or
            character.weapon_groups.is_known("Spears")
        )
        return class_met and other_requirements


class TwoHandedStyle(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(TwoHandedStyle, self).__init__(
            talents,
            "Two-Hander Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.strength >= 3 and (
            character.weapon_groups.is_known("Axes") or
            character.weapon_groups.is_known("Bludgeons") or
            character.weapon_groups.is_known("Heavy Blades") or
            character.weapon_groups.is_known("Polearms") or
            character.weapon_groups.is_known("Spears")
        )
        return class_met and other_requirements


class UnarmedStyle(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(UnarmedStyle, self).__init__(
            talents,
            "Unarmed Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.weapon_groups.is_known("Brawling")
        return class_met and other_requirements


class WeaponAndShieldStyle(Talent):
    """You are experienced with bows and crossbows"""
    def __init__(self, talents, level=None):
        super(WeaponAndShieldStyle, self).__init__(
            talents,
            "Weapon and Shield Style",
            level
        )

    def is_eligible(self, character) -> bool:
        class_met = character.character_class in self.class_requirements
        other_requirements = character.abilities.strength >= 2
        return class_met and other_requirements

"""
Here we initialize the "ALL TALENTS" global variable
"""

ALL_TALENTS = {Alchemy, AnimalTraining, ArmorTraining, ArcheryStyle, Carousing,
               Chirurgy, Command, Contacts, DualWeaponStyle, Horsemanship,
               Intrigue, Linguistics, Lore, MountedCombatStyle, Music,
               Observation, Oratory, PoleWeaponStyle, QuickReflexes, Scouting,
               SingleWeaponStyle, Thievery, ThrownWeaponStyle, TwoHandedStyle,
               UnarmedStyle, WeaponAndShieldStyle}
