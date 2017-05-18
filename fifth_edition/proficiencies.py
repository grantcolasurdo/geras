"""This is the module that organizes the different proficiencis that a character can have"""

from fifth_edition import abilities
import csv

__author__ = "Grant Colasurdo"


class Proficiency:
    def __init__(self):
        self.proficiency_name: str = None
        self.description: str = None


class ToolProficiency(Proficiency):
    def __init__(self, proficiency_name: str):
        super(ToolProficiency, self).__init__()
        self.proficiency_name = proficiency_name


class WeaponProficiency(Proficiency):
    def __init__(self, proficiency_name: str):
        super(WeaponProficiency, self).__init__()
        self.proficiency_name = proficiency_name


class ArmorProficiency(Proficiency):
    def __init__(self, proficiency_name: str):
        super(ArmorProficiency, self).__init__()
        self.proficiency_name = proficiency_name


class SavingThrowProficiency(Proficiency):
    def __init__(self, proficiency_name: str):
        super(SavingThrowProficiency, self).__init__()
        self.proficiency_name = proficiency_name
        self.ability = abilities.ABILITY_LIST[self.proficiency_name]()


class SkillProficiency(Proficiency):
    def __init__(self, proficiency_name: str):
        super(SkillProficiency, self).__init__()
        self.proficiency_name = proficiency_name

        with open("skills.csv") as file:
            skill_file = csv.DictReader(file)
            for row in skill_file:
                if row['skill_name'] == self.proficiency_name:
                    self.description = row['description']
                    self.ability = abilities.ABILITY_LIST[row['ability_name']]()

