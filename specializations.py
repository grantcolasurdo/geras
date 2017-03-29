"""Similar to the Talents, this are super talents"""

import csv

__author__ = "Grant Colasurdo"

file = open('specializations.csv', 'r')
specialization_file = csv.DictReader(file)

def find_row_by_name(specialization_name: str) -> dict:
    for row in specialization_file:
        if row['name'] == specialization_name:
            return row
    print("there was no specialization by that name")

ALL_SPECIALIZATIONS = set()

class Specializations:
    """A collection class that handles specialization meta data"""
    def __init__(self, character, specializations=set()):
        self.character = character
        self.acquired_specializations = specializations

    def available_specializations(self):
        pass


class Specializaton:
    """Essentially, a more restrictive talent"""
    def __init__(
        self,
        specializations,
        specialization_name=None,
        level=None
    ):
        self.specialization_name = specialization_name
        db_details = find_row_by_name(self.specialization_name)
        self.specializations = specializations
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
    
    def is_eligible(self, character):
        pass


class ArcaneScholar(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(ArcaneScholar, self).__init__(
            specializations,
            "Arcane Scholar",
            level
        )

    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = (
            character.abilities.intelligence >= 3 and
            character.focuses.is_known("Arcane Lore")
        )
        return class_met and other_requirements


class Assassin(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(Assassin, self).__init__(
            specializations,
            "Assassin",
            level
        )

    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class Berzerker(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(Berzerker, self).__init__(
            specializations,
            "Berzerker",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class Dualist(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(Dualist, self).__init__(
            specializations,
            "Dualist",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class Elementalist(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(Elementalist, self).__init__(
            specializations,
            "Elementalist",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class Guardian(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(Guardian, self).__init__(
            specializations,
            "Guardian",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class Knight(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(Knight, self).__init__(
            specializations,
            "Knight",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class MageHunter(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(MageHunter, self).__init__(
            specializations,
            "MageHunter",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class MiracleWorker(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(MiracleWorker, self).__init__(
            specializations,
            "MiracleWorker",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class SharpShooter(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(SharpShooter, self).__init__(
            specializations,
            "Sharpshooter",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class Swashbuckler(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(Swashbuckler, self).__init__(
            specializations,
            "Swashbuckler",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements


class SwordMage(Specializaton):
    def __init__(
        self,
        specializations=None,
        level=None
    ):
        super(SwordMage, self).__init__(
            specializations,
            "Sword Mage",
            level
        )
    def is_eligible(self, character):
        class_met = character.character_class in self.class_requirements
        other_requirements = True
        return class_met and other_requirements

"""
Here is where we put everyting into the ALL_SPECIALIZATIONS
"""

ALL_SPECIALIZATIONS = {
    ArcaneScholar, Assassin, Berzerker, Dualist, Elementalist, Guardian,
    Knight, MageHunter, MiracleWorker, SharpShooter, Swashbuckler, SwordMage
}
