#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Manage character's backgrounds here"""

import csv
from fifth_edition import characters
from fifth_edition import abilities
from fifth_edition import proficiencies
from fifth_edition import input_tools

__author__ = "Grant Colasurdo"
__copyright__ = "Copyright (C) 2017 Grant Colasurdo"
__licence__ = "GPLv2"


class Background:
    """The background information for a character
    
    Parameters
    ----------
    background_name: str
        The name of the background
        
    Attributes
    ----------
    character: Character
        The character that the background describes
    background_name: str
        this is the name of the background
    description: str
        The description given in the rulebook
    """
    def __init__(self, character: characters.Character, background_name: str):
        self.character = character
        self.background_name = background_name
        self.description = None
        self.ability_score_increases = set()
        self.proficiencies = set()
        self.languages = set()
        self.personality_trait:str = None
        self.personality_trait_options: dict = None
        self.ideal: str = None
        self.ideal_options: dict = None
        self.bond: str = None
        self.bond_options: dict = None
        self.flaw: str = None
        self.flaw_options: dict = None


class Acolyte(Background):
    def __init__(self, character: characters.Character):
        super(Acolyte, self).__init__(character, "Acolyte")
        self.proficiencies.add(proficiencies.SkillProficiency("Insight"))
        self.proficiencies.add(proficiencies.SkillProficiency("Religion"))

        self.personality_trait_options = {
            "1": "I idolize a particular hero of my faith, and constantly refer to that person's deeds and example",
            "2": "I can find common ground between the fiercest enemies, empathizing with them and always working "
                 "towards peace",
            "3": "I see omens in every event and action. The gods try to speak to us, we just need to listen",
            "4": "Nothing can shake my optimistic attitude",
            "5": "I quote (or misquote) sacred texts and proverbs in almost every situation",
            "6": "I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods",
            "7": "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me",
            "8": "I've spent so long in the temple that I have little practical experience dealing with people in "
                 "the outside world"
        }
        self.ideal_options = {
            "1": "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld (Lawful)",
            "2": "Charity. I always try to help those in need, no matter what the personal cost. (Good)",
            "3": "Change. We must help bring about the changes the gods are constantly working in the world",
            "4": "Power. I hope to one day rise to the top of my faith's religious hierarchy. (Lawful)",
            "5": "Faith, I trust that my deity will guide my actions. I have faith that if I work hard, things will go "
                 "well (Lawful)",
            "6": "Aspiration. I seek to prove myself worthy of my god's favor by matching my actions against his her "
                 "her teachings. (Any)"
        }
        self.bond_options = {
            "1": "I would die to recover an ancient relic of my faith that wsa lost long ago",
            "2": "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic",
            "3": "I owe my life to the priest who took me in when my parents died",
            "4": "Everything I do is for the common people",
            "5": "I will do anything to protect the temple where I served",
            "6": "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy"
        }
        self.flaw_options = {
            "1": "I judge others harshly, and myself even more severely",
            "2": "I put too much trust in those who wield power within my temple's hierarchy",
            "3": "My piety sometimes leads me to blindly trust those that profess faith in my god",
            "4": "I am inflexible in my thinking",
            "5": "I am suspicious of strangers and expect the worst of them",
            "6": "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life"
        }


class Charlatan(Background):
    def __init__(self, character: characters.Character):
        super(Charlatan, self).__init__(character, "Charlatan")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "I fall in and out of love easily, and am always pursuing someone.",
            "2": "I have a joke for every occasion, especially occasions where humor is inappropriate",
            "3": "Flattery is my preferred trick for getting what I want.",
            "4": "I'm a born gambler who can't resist taking a risk for a potential payoff",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class Criminal(Background):
    def __init__(self, character: characters.Character):
        super(Criminal, self).__init__(character, "Criminal")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class Entertainer(Background):
    def __init__(self, character: characters.Character):
        super(Entertainer, self).__init__(character, "Entertainer")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class FolkHero(Background):
    def __init__(self, character: characters.Character):
        super(FolkHero, self).__init__(character, "FolkHero")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class GuildArtisan(Background):
    def __init__(self, character: characters.Character):
        super(GuildArtisan, self).__init__(character, "GuildArtisan")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class Hermit(Background):
    def __init__(self, character: characters.Character):
        super(Hermit, self).__init__(character, "Hermit")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class Noble(Background):
    def __init__(self, character: characters.Character):
        super(Noble, self).__init__(character, "Noble")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class Outlander(Background):
    def __init__(self, character: characters.Character):
        super(Outlander, self).__init__(character, "Outlander")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class Sage(Background):
    def __init__(self, character: characters.Character):
        super(Sage, self).__init__(character, "Sage")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class Sailor(Background):
    def __init__(self, character: characters.Character):
        super(Sailor, self).__init__(character, "Sailor")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class Soldier(Background):
    def __init__(self, character: characters.Character):
        super(Soldier, self).__init__(character, "Soldier")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }


class Urchin(Background):
    def __init__(self, character: characters.Character):
        super(Urchin, self).__init__(character, "Urchin")
        self.proficiencies.add(proficiencies.SkillProficiency)

        self.personality_trait_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": ""
        }
        self.ideal_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.bond_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }
        self.flaw_options = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": ""
        }

















def init_character(character: characters.Character) -> Background:
    pass


def get_background(background_name: str, chosen_focus: str) -> Background:
    background = Background(background_name)
    background.chosen_starting_focus = chosen_focus
    return background


