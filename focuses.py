"""This is where the logic for focuses lie"""

import csv
import input_tools

__author__ = "Grant Colasurdo"

ALL_FOCUSES = set()

class Focus:
    def __init__(
        self,
        focuses=None,
        name=None,
        ability=None,
        level=None,
        description=None
    ):
        self.focuses = focuses
        self.focus_name: str = name
        self.ability: str = ability
        self.level = level
        self.description: str = description

    def bonus(self):
        if self.level == 0:
            return 0
        elif self.level == 1:
            return 2
        elif self.level == 2:
            return 3
        else:
            print("Focus level is too damn high")
            raise Exception

    def improve_focus(self):
        if self.focuses.character.level > 10 and self.level < 2:
            self.level += 1
        elif self.level > 1:
            print("Focus is already improved")
        else:
            print("Character is too low a level to improve the focus")


class Focuses:
    def __init__(
        self, character, acquired_focuses=None, all_focuses=None
    ):
        self.character = character
        self.acquired_focuses = acquired_focuses
        self.all_focuses = all_focuses

    @property
    def available_focuses(self):
        """Return a set of focuses that are available to a character in it's
        current state"""
        improvement_level_met = self.character.level > 10
        focus_pool = {focus_template for focus_template in ALL_FOCUSES}
        #  First we need to define what focuses we already know
        unleveled_focuses = set()
        [
            unleveled_focuses.add(template_focus) for template_focus in ALL_FOCUSES if
            template_focus.name in self.unleveled_focuses_text
        ]
        unimproved_focuses = set()
        [
            unimproved_focuses.add(template_focus) for template_focus in ALL_FOCUSES if
            template_focus.name in self.unimproved_focuses_text
        ]
        improved_focuses = set()
        [
            improved_focuses.add(template_focus) for template_focus in ALL_FOCUSES if
            template_focus.name in self.improved_focuses_text
        ]

        if improvement_level_met:
            return focus_pool - improved_focuses
        else:
            return focus_pool - improved_focuses - unimproved_focuses

    @property
    def available_focuses_level_up(self):
        focus_pool = self.available_focuses
        primary_abilities = self.character.character_class.primary_abilities
        secondary_abilities = self.character.character_class.secondary_abilities
        level_uses_primary = self.character.level % 2 == 0
        if level_uses_primary:
            return {template_focus for template_focus in focus_pool if focus.ability in primary_abilities}
        else:
            return {template_focus for template_focus in focus_pool if focus.ability in secondary_abilities}

    @property
    def unleveled_focuses_text(self):
        return {template_focus.name for template_focus in self.acquired_focuses if focus.level == 0}

    @property
    def unimproved_focuses_text(self):
        return {template_focus.name for template_focus in self.acquired_focuses if focus.level == 1}

    @property
    def improved_focuses_text(self):
        return {template_focus.name for template_focus in self.acquired_focuses if focus.level == 2}

    def level_up(self):
        option_list = [focus.name for focus in self.available_focuses_level_up]
        focus_selection = input_tools.input_response(
            "These are the focuses that are available, choose one by name", option_list
        )
        self.acquire_focus(focus_selection)

    def acquire_focus(self, focus_name):
        """Find the focus from all focuses and append it to the focuses group"""
        if focus_exits(focus_name):
            #  The focus is available, now do we already have it?
            target_focus = self.get_focus(focus_name)
            if target_focus is None:
                target_focus = get_focus_from_template(focus_name)
                target_focus.focuses = self
                self.acquired_focuses.add(target_focus)
            target_focus.improve_focus()

    def get_focus(self, focus_name) -> Focus:
        focus_list = [
            individual_focus for individual_focus in self.available_focuses if
            individual_focus.name == focus_name
        ]
        if len(focus_list) == 1:
            return focus_list[0]
        else:
            return None

    def is_known(self, focus_name):
        return any(
            test_focus.focus_name == focus_name and test_focus.level > 0
            for test_focus in self.acquired_focuses
        )



def acquire_focus(character, focus_name: str):
    character.focuses.acquire_focus(focus_name)


def focus_exits(focus_name):
    return any(template_focus.name == focus_name for template_focus in ALL_FOCUSES)


def get_focus_from_template(focus_name) -> Focus:
    """Search through all focuses and return the one with a name matching focus_name"""
    qualifying_focuses = [focus for focus in ALL_FOCUSES if focus.name == focus_name]
    try:
        assert len(qualifying_focuses) == 1
        focus_to_copy = qualifying_focuses[0]
        focus_to_return = Focus(
            None,
            name=focus_to_copy.name,
            ability=focus_to_copy.ability,
            level=focus_to_copy.level,
            description=focus_to_copy.description
        )
        return focus_to_return
    except AssertionError:
        print("That focus doesnt' exist in memory")


with open('focuses.csv', 'r') as file:
    focus_file = csv.DictReader(file)
    for row in focus_file:
        focus = Focus(
            name=row['name'],
            ability=row['ability'],
            level=0,
            description=row['description']
        )
        ALL_FOCUSES.add(focus)
