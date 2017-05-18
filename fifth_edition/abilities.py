"""This is where abilities will be defined"""

from fifth_edition import input_tools
from fifth_edition import characters

__author__ = "Grant Colasurdo"

ABILITY_LIST = ('Strength', "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma")


def ability_greater_than(character, ability_name, compared_to):
    return character.abilities.ability_map[ability_name] > compared_to


class Ability:
    """Manage the ability score for one ability for one character"""
    def __init__(self, ability_name: str, score: int):
        self.ability_name = ability_name
        self._score = score
        self.description = None

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int):
        self._score = value

    @property
    def modifier(self) -> int:
        return (self.score - 10) // 2


class Strength(Ability):
    def __init__(self, score=None):
        super(Strength, self).__init__("Strength", score)


class Dexterity(Ability):
    def __init__(self, score=None):
        super(Dexterity, self).__init__("Dexterity", score)


class Constitution(Ability):
    def __init__(self, score=None):
        super(Constitution, self).__init__("Constitution", score)


class Intelligence(Ability):
    def __init__(self, score=None):
        super(Intelligence, self).__init__("Intelligence", score)


class Wisdom(Ability):
    def __init__(self, score=None):
        super(Wisdom, self).__init__("Wisdom", score)


class Charisma(Ability):
    def __init__(self, score=None):
        super(Charisma, self).__init__("Charisma", score)


def sum_ability_sources(ability, character: characters.Character) -> int:
    score = 0
    if len(character.initial_abilities) != 0:
        score += sum({item.score for item in character.initial_abilities if isinstance(item, ability)})
    if character.race is not None:
        score += sum({item.score for item in character.race.ability_score_increases if isinstance(item, ability)})
    if character.background is not None:
        score += sum({item.score for item in character.background.ability_score_increases if isinstance(item, ability)})
    if len(character.character_classes) != 0:
        score += sum()
    return score


