"""The spells in an AGE fantasy RPG"""

__author__ = "Grant Colasurdo"

class Magic:
    """This class manages the spells available to a character"""
    def __init__(self, character):
        self.character = character
        self.max_mana = None
        self.mana = None
        self.known



class Arcana:
    """This is a group of spells that are related to eachother"""
    def __init__(self, magic, name, level):
        self.arcana_name: str = name
        self.level: int = level
        self.magic: Magic = magic


class BaseSpell:
    def __init__(
        self, arcana, target_number, requirements, description, mp_cost, 
        casting_time, test, effect
    ):
        self.arcana = arcana
        self.target_number = target_number
        self.requirement = requirements
        self.description = description
        self.mp_cost = mp_cost
        self.casting_time = casting_time
        self.test = test
        self.effect = []
    
    def spell_power(self):
        base = 10
        willpower = self.arcana.magic.character.abilities.willpower
        if arcana_name in self.arcana.magic.focuses:
            focus = self.arcana.magic.character.focuses[arcana.arcana_name]

class AirArcana(BaseArcana):
    def __init__(self, level):
        super().__init__("Air Arcana", level)

