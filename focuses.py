"""This is where the logic for focuses lie"""

import csv
import input_tools

__author__ = "Grant Colasurdo"

ALL_FOCUSES = set()


class Focus:
    """Represents the Focus trait in a characters stats
    
    Parameters
    ----------
    focuses: Focuses
        The object that manages meta level information about a character's focuses
    focus_name: str
        The focuses name
    ability: str
        The ability that can be given a bonus when rolling a test
    level: int
        The level of proficiency of the focus, 0 -> unlearned to 2 -> improved foucs
    description: str
        The description of the focus given in the rulebook
        
    """
    def __init__(
        self,
        focuses=None,
        focus_name=None,
        ability=None,
        level=None,
        description=None
    ):
        self._ability = None
        self._name = None
        self.focuses = focuses
        self.focus_name: str = focus_name
        self.ability: str = ability
        self.level = level
        self.description: str = description

    @property
    def ability(self) -> str:
        """str: Return the ability name that the focus improves upon"""
        return self._ability

    @ability.setter
    def ability(self, value: str):
        self._ability = value

    @property
    def focus_name(self) -> str:
        """str: return the focus name"""
        return self._name

    @focus_name.setter
    def focus_name(self, value: str):
        self._name = value

    @property
    def bonus(self):
        """Return the bonus that the character would be due if the focus applies"""
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
        """If the focus is able to be improved, improve the focus"""
        if self.level < 1:
            self.level += 1
        elif self.level > 1:
            print("Focus is already improved")
        elif self.focuses.character.level > 10:
            self.level += 1
        else:
            print("Character is too low a level to improve the focus")


class Focuses:
    """An object that handles the meta-level information about a character's focuses
    
    Parameters
    ----------
    character:  Character
        the character object that this object is representative of
    acquired_focuses: 
    """
    def __init__(
        self, character, acquired_focuses=set()
    ):
        self.character = character
        self.acquired_focuses = acquired_focuses

    @property
    def available_focuses(self):
        """Return a set of focuses that are available to a character in it's current state"""
        improvement_level_met = self.character.level > 10
        focus_pool = {focus_template for focus_template in ALL_FOCUSES}
        #:  First we need to define what focuses we already know
        unleveled_focuses = set()
        [
            unleveled_focuses.add(template_focus) for template_focus in ALL_FOCUSES if
            template_focus.focus_name in self.unleveled_focuses_text
        ]
        unimproved_focuses = set()
        [
            unimproved_focuses.add(template_focus) for template_focus in ALL_FOCUSES if
            template_focus.focus_name in self.unimproved_focuses_text
        ]
        improved_focuses = set()
        [
            improved_focuses.add(template_focus) for template_focus in ALL_FOCUSES if
            template_focus.focus_name in self.improved_focuses_text
        ]

        if improvement_level_met:
            return focus_pool - improved_focuses
        else:
            return focus_pool - improved_focuses - unimproved_focuses

    @property
    def available_focuses_level_up(self) -> set:
        """Return a set of Focuses that are valid choices in a level up process given a character's status"""
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
        """Return a set of str that have the names of each focus not leveled"""
        all_focus_names = {individual_focus.focus_name for individual_focus in ALL_FOCUSES}
        unleveled_focus_names = all_focus_names - self.unimproved_focuses_text - self.improved_focuses_text
        return unleveled_focus_names

    @property
    def unimproved_focuses_text(self):
        """Return a set of str that have the names of each focus known but not improved"""
        return {template_focus.focus_name for template_focus in self.acquired_focuses if focus.level == 1}

    @property
    def improved_focuses_text(self):
        """Return a set of str that have the names of each focus that was improved"""
        return {template_focus.focus_name for template_focus in self.acquired_focuses if focus.level == 2}

    def level_up(self):
        """List the Focuses that are available to be leveled up and select one to level up"""
        option_list = [specific_focus.focus_name for specific_focus in self.available_focuses_level_up]
        focus_selection = input_tools.input_response(
            "These are the focuses that are available, choose one by name", option_list
        )
        self.acquire_focus(focus_selection)

    def acquire_focus(self, focus_name: str, source: str=None):
        """Find the focus from all focuses and append it to the focuses group"""
        if focus_exists(focus_name):
            #  The focus is available, now do we already have it?
            target_focus = self.get_focus(focus_name)
            target_focus.improve_focus()

    def get_focus(self, focus_name: str) -> Focus:
        """Return a focus from the acquired_focuses group with the same name as `focus_name`"""
        try:
            assert focus_exists(focus_name)
            try:
                focus_list = {
                    individual_focus for individual_focus in self.acquired_focuses if
                    individual_focus.focus_name == focus_name
                }
                assert len(focus_list) < 2
                if len(focus_list) == 1:
                    return focus_list.pop()
                else:
                    target_focus = get_focus_from_template(focus_name)
                    target_focus.focuses = self
                    self.acquired_focuses.add(target_focus)
                    return target_focus
            except AssertionError:
                print("There were too many focuses by that name")
            except TypeError:
                target_focus = get_focus_from_template(focus_name)
                target_focus.focuses = self
                self.acquired_focuses.add(target_focus)
                return target_focus
        except AssertionError:
            print("The focus you are trying to get does not exist")

    def is_known(self, focus_name):
        """Return True if there is a Focus with the name `focus_name` in acquired_focuses"""
        return any(
            test_focus.focus_name == focus_name for test_focus in self.acquired_focuses
        )


def choose_focus(character, focus_choices, source=None):
    """List the available choices, and aquire the selected option"""
    focus_selection = input_tools.input_response(
        "These are the focuses you are allowed to chose between", focus_choices
    )
    character.focuses.acquire_focus(focus_selection)


def acquire_focus(character, focus_name: str, source: str = None):
    """Add a focus by the name `focus_name` to the character `character`"""
    character.focuses.acquire_focus(focus_name)


def focus_exists(focus_name) -> bool:
    """Return True if a focus with the name `focus_name` exits in the world"""
    return any(template_focus.focus_name == focus_name for template_focus in ALL_FOCUSES)


def get_focus_from_template(focus_name) -> Focus:
    """Search through all focuses and return the one with a name matching focus_name"""
    qualifying_focuses = [specific_focus for specific_focus in ALL_FOCUSES if specific_focus.focus_name == focus_name]
    try:
        assert len(qualifying_focuses) == 1
        focus_to_copy = qualifying_focuses[0]
        focus_to_return = Focus(
            None,
            focus_name=focus_to_copy.focus_name,
            ability=focus_to_copy.ability,
            level=focus_to_copy.level,
            description=focus_to_copy.description
        )
        print("Found focus " + focus_to_return.focus_name + ". Returning to higher function")
        return focus_to_return
    except AssertionError:
        print("That focus doesnt' exist in memory")

#: Load all the focuses from the csv file into memory as `ALL_FOCUSES`
with open('focuses.csv', 'r') as file:
    focus_file = csv.DictReader(file)
    for row in focus_file:
        focus = Focus(
            focus_name=row['name'],
            ability=row['ability'],
            level=0,
            description=row['description']
        )
        ALL_FOCUSES.add(focus)
