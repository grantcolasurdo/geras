"""Traits of races"""

import abilities
import focuses

__author__ = "Grant Colasurdo"


class Race:
    def __init__(
        self, character=None, name=None, description=None,
        min_height=None, max_height=None, given_stats=None,
        female_names=None, male_names=None, family_names=None,
        benefit_schedule=None
    ):
        self.character = character 
        self.race_name = name 
        self.description = description
        self.min_height = min_height
        self.max_height = max_height
        self.given_stats = given_stats
        self.female_names = female_names
        self.male_names = male_names
        self.family_names = family_names
        self.benefit_schedule = benefit_schedule

    def init_race(self):
        pass



class Dwarf(Race):
    def __init__(self):
        super().__init__(
            character=character,
            name="Dwarf",
            description="Short harry people",
            min_height=4,
            max_height=5,
            given_stats = [],
            female_names = {
                "Ailine", "Dara", "Kalin", "Klara", "Mora", 
                "Telka", "Ulma"
            },
            male_names = {
                "Bodag", "Crag", "Doffin", "Hador", "Gurt", "Throrik",
                "Warrik"
            },
            family_names = {
                "Bronzeblade", "Highcliff", "Ironshield", "Rockhammer",
                "Steelhelm", "Stonebones"
            },
            benefit_schedule = {
                2: (abilities.level_up, "Willpower"),
                3: (focuses.aquire_focus, "Historacal Lore"),
                4: (focuses.aquire_focus, "Historacal Lore"),
                5: (focuses.aquire_focus, "Stamina"),
                6: (weapon_groups.learn_group, "Axes"),
                7: (abilities.level_up, "Fighting"),
                8: (abilities.level_up, "Fighting"),
                9: (focuses.aquire_focus, "Smithing"),
                10: (focuses.aquire_focus, "Engineering"),
                11: (focuses.aquire_focus, "Engineering"),
                12: (abilities.level_up, "Strength")
            }

        )

class Elf(Race):
    def __init__(self):
        super().__init__(
            character = character,
            name = "Elf",
            description="Dirt worshiper",
            min_height = 5,
            max_height = 6,
        )

