"""Traits of races"""

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
            max_height=5
        )

