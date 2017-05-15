"""Weapon Group information"""

import csv

__author__ = "Grant Colasurdo"


ALL_WEAPON_GROUPS = set()


def learn_group(character, weapon_group: str, source: str = None):
    character.weapon_groups.learn_group(weapon_group, source)


def weapon_group_known(character, weapon_group: str, comparison_dummy):
    return character.weapon_groups.is_known(weapon_group)


class WeaponGroups:
    def __init__(
        self,
        character,
        known_groups=set(),

    ):
        self.character = character
        self.known_groups = known_groups

    def learn_group(self, group_name, source: str = None):
        if self.is_known(group_name):
            print("Skill already known")
        else:
            try:
                assert any(group.group_name == group_name for group in ALL_WEAPON_GROUPS)
                matching_groups = {group for group in ALL_WEAPON_GROUPS if group.group_name == group_name}
                group_to_copy = None
                if len(matching_groups) == 1:
                    group_to_copy = matching_groups.pop()
                else:
                    print("Too many matching groups, check the source csv's for duplicates")
                group_to_add = WeaponGroup(
                    self,
                    group_to_copy.group_name,
                    group_to_copy.success_ability,
                    group_to_copy.damage_ability
                )
                self.known_groups.add(group_to_add)
            except AssertionError:
                print("That weapon group don't exist")

    def is_known(self, weapon_group: str):
        return any(group.group_name == weapon_group for group in self.known_groups)


class WeaponGroup:
    def __init__(
        self,
        weapon_groups=None,
        name=None,
        success_ability=None,
        damage_ability=None
    ):
        self.weapon_groups = weapon_groups
        self.group_name = name
        self.success_ability = success_ability
        self.damage_ability = damage_ability

with open('weapon_groups.csv', 'r') as file:
    group_file = csv.DictReader(file)
    for row in group_file:
        new_group_name = row['name']
        new_group_success_ability = row['success_ability']
        new_group_damage_ability = row['damage_ability']
        new_group = WeaponGroup(None, new_group_name, new_group_success_ability, new_group_success_ability)
        ALL_WEAPON_GROUPS.add(new_group)
