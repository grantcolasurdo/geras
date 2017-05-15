"""Skills that allow for bonuses to be applied on rolls"""

from fifth_edition import abilities
import csv


class Skill:
    def __init__(self, name: str, ability: str, description: str = None):
        self.name = name
        self.description = description


ALL_SKILLS = set()

with open("skills.csv") as file:
    skill_file = csv.DictReader(file)
    for row in skill_file:
        skill = Skill(
            name=row['skill_name'],
            ability=row['ability_name'],
            description=row['description']
        )
        ALL_SKILLS.add(skill)

