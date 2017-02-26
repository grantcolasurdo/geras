"""Here are all the non-magic talents"""

__author__ = "Grant Colasurdo"

class Talents:
    def __init__(
        self, character=None, aquired=None, available=None, all_talents=None
    ):
        self.character = character
        self.aquired = aquired
        self.available = available
        self.all_talents = all_talents

    def available_talents(self):
        """Return a set of talents that are available to a character in it's
        current state"""
        pass

    def aquire_talent(self, talent:Talent):
        """aquire the given talent, or add a level to it"""
        if talent in self.available_talents():
            """The talent is available, now do we already have it?"""
            return_talent(talent).level += 1
        else:
            self.aquired_talents.add(talent(self))
    
    def return_talent(self, talent:Talent):
        """Return a talent formthe aquired_talents group"""
        talent_list = [
            individual_talent for individual_talent in self.available_talents 
            if isinstance(individual_talent, talent)
        ]
        if len(talent_list) == 1:
            return return_talent[0]
        else:
            return None


class Talent:
    def __init__(
        self, talents=None, name=None, classes=None, requirements=None,
        description=None, level=None, novice_description=None,
        journeyman_description=None, master_description=None
    ):
        self.talents = talents
        self.talent_name = name
        self.classes = classes
        self.requirements = requirements
        self.description = description
        self.level = level

    def aquire(self, character):
        already_aquired = any(
            isinstance(talent, self.__class__) for talent in character.talents
        )
        eligible = already_aquired and character.character_class in self.classes
        eligible = eligible and all(
            requirement.test(character) for requirement in self.requirements
        )
        if eligible:
            self.talents.add

class AnimalTraining(Talent):
    def __init__(self, talents, level):
        super().__init__(
            talents, 
            "Animal Training", 
            {classes.Mage, classes.Rouge, classes.Warrior},
            set(),
            "You know how to train animals",
            level
        )

class ArmorTraining(Talent):
    def __init__(self, talents, level):
        super().__init__(
            talents,
            "Armor Training",
            {classes.Warrior},
            set(),
            "You You have learned to fight while wearing armor. You only take "\
            "the armor’s penalty to your Speed, while those without this "\
            "talent suffer the penalty to all Dexterity-based tests and "\
            "calculations (including Speed).",
            level
        )

