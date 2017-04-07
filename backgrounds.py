#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Manage character's backgrounds here"""

import input_tools
import csv

__author__ = "Grant Colasurdo"
__copyright__ = "Copyright (C) 2017 Grant Colasurdo"
__licence__ = "GPLv2"

SOCIAL_CLASS_ROLLS = {
    1: "Outsider",
    2: "Lower",
    3: "Lower",
    4: "Middle",
    5: "Middle",
    6: "Upper",
}

BACKGROUND_DICTIONARY = {
    "Outsider": {
        1: "Criminal",
        2: "Exile",
        3: "Hermit",
        4: "Pirate",
        5: "Radical",
        6: "Wanderer"
    },
    "Lower": {
        1: "Artist",
        2: "Laborer",
        3: "Performer",
        4: "Sailor",
        5: "Solder",
        6: "Tradesperson"
    },
    "Middle": {
        1: "Guilder",
        2: "Initiate",
        3: "Innkeeper",
        4: "Merchant",
        5: "Scribe",
        6: "Student"
    },
    "Upper": {
        1: "Apprentice",
        2: "Dilettante",
        3: "Noble",
        4: "Official",
        5: "Scholar",
        6: "Squire"
    }
}

SOCIAL_CLASS_BASE_MONEY = {
    "Outsider": 15,
    "Lower": 25,
    "Middle": 50,
    "Upper": 100
}


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
    social_class: str
        The name of the parent social class
    description: str
        The description given in the rulebook
    starting_focus_options: list of str
        The focus options available to a character of this class
    """
    def __init__(
            self,
            background_name,
    ):
        self.character = None
        self.background_name = background_name
        self.social_class = None
        self.description = None
        self.starting_focus_options = set()
        self.chosen_starting_focus = None
        with open('backgrounds.csv', 'r') as csv_file:
            background_db = csv.DictReader(csv_file)
            for row in background_db:
                if row['name'] == self.background_name:
                    self.social_class = row['social_class']
                    self.description = row['description']
                    self.starting_focus_options.add(row['focus_option_1'])
                    self.starting_focus_options.add(row['focus_option_2'])


def init_character(character=None) -> Background:
    class_roll = int(input_tools.input_response(
        "Roll for social class",
        [str(x) for x in range(1, 7)]
    ))
    rolled_class = SOCIAL_CLASS_ROLLS[class_roll]
    background_dict = BACKGROUND_DICTIONARY[rolled_class]
    print("In your past you were a member of the " + rolled_class + " class.")
    background_roll = int(input_tools.input_response(
        "Roll for specific background",
        [str(x) for x in range(1, 7)]
    ))
    rolled_background = background_dict[background_roll]
    background = Background(rolled_background)
    background.chosen_starting_focus = input_tools.input_response(
        "Choose a focus that fit's your background",
        background.starting_focus_options
    )
    if character is not None:
        background.character = character
    return background


def get_background(background_name: str, chosen_focus: str) -> Background:
    background = Background(background_name)
    background.chosen_starting_focus = chosen_focus
    return background


