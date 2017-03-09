"""Weapon Group information"""

__author__ = "Grant Colasurdo"


def learn_group(character, weapon_group: str): 
    character.weapon_groups.learn_group(weapon_group)

class WeaponGroups:
    def __init__(
        self,
        character,
        known_groups = set(),

    ):
        self.character = character
        self.known_groups = known_groups

    def learn_group(self, group_name):
        is_known = any(
            [
                True for group in self.known_groups 
                if group.group_name == group_name
            ]
        )
        if is_known:
            print("Skill already known")
            return False
        else:
            self.known_groups.add(WeaponGroup(self,group_name))
            return True

class WeaponGroup:
    def __init__(
        self,
        weapon_groups,
        name=None,

    ):
        self.weapon_groups = weapon_groups
        self.group_name = name
