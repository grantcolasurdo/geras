"""Traits of races"""

import abilities
import focuses
import languages
import input_tools

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
        for entry in self.given_stats:
            function = entry[0]
            arguments = entry[1:]
            function(self.character, arguments)
        self.roll_benefit()


    def roll_benefit(self):
        roll_1 = input_tools.input_response(
            "Roll 2d6 for your benefit",
            range(2, 13)
        )
        benefit_1 = self.benefit_schedule[roll_1]
        function_1 = benefit_1[0]
        args_1 = benefit[1:]
        function_1(self.character, args_1)
        roll_2_same = True
        while roll_2_same:
            roll_2 = input_tools.input_response(
                "Roll another 2d6 for your other race benefit",
                range(2, 13)
            )
            benefit_2 = self.benefit_schedule[roll_2]
            roll_2_same =  benefit_2 == benefit_1
        function_2 = benefit_2[0]
        args_2 = benefit_2[1:]
        function_2(self.character, args_2)


class Dwarf(Race):
    def __init__(self):
        super().__init__(
            character=character,
            name="Dwarf",
            description="Short harry people",
            min_height=4,
            max_height=5,
            given_stats = [
                (abilities.level_up, ("Constitution", "Race")),
                (focuses.aquire_focus, ("Evaluation or Drinking")),
                (dark_sight, True),
                (languages.add_language, "Dwarven"), 
                (languages.add_language, "Common Tongue")
            ],
            female_names = {
                "Ailine", "Dara", "Kalin", "Klara", "Mora",
                "Telka", "Ulma"
            },
            male_names = {
                "Bodag", "Crag", "Doffin", "Hador", "Gurt", "Throrik",
                "Warrik"
            },
            family_names = {
                "Bronzeblade", "Highcliff", "Ironshield", "Rockhammer",
                "Steelhelm", "Stonebones"
            },
            benefit_schedule = {
                2: (abilities.level_up, "Willpower"),
                3: (focuses.aquire_focus, "Historacal Lore"),
                4: (focuses.aquire_focus, "Historacal Lore"),
                5: (focuses.aquire_focus, "Stamina"),
                6: (weapon_groups.learn_group, "Axes"),
                7: (abilities.level_up, "Fighting"),
                8: (abilities.level_up, "Fighting"),
                9: (focuses.aquire_focus, "Smithing"),
                10: (focuses.aquire_focus, "Engineering"),
                11: (focuses.aquire_focus, "Engineering"),
                12: (abilities.level_up, "Strength")
            }

        )

class Elf(Race):
    def __init__(self):
        super().__init__(
            character = character,
            name = "Elf",
            description="Dirt worshiper",
            min_height = 5,
            max_height = 6,
            given_stats = [
                (ability.level_up, "Dexterity"),
                (
                    focuses.choose_focus,
                    (
                        focuses.Focus("Natural Lore"),
                        focuses.Focus("Seeing")
                    )
                )
                (characer.dark_sight, True),
                (character.base_speed, 12),
                (languages.add_language, "Elven")
                (languages.add_language, "Common Tongue")
            ],
            benefit_schedule = {
                2: (abilities.level_up, "Communication"),
                3: (focuses.aquire_focus, "Culteral Lore"),
                4: (focuses.aquire_focus, "Culteral Lore"),
                5: (focuses.aquire_focus, "Hearing"),
                6: (weapon_groups.learn_group, "Bows"),
                7: (abilities.level_up, "Acuuracy"),
                8: (abilities.level_up, "Acuuracy"),
                9: (focuses.aquire_focus, "Initiative"),
                10: (focuses.aquire_focus, "Persuasion"),
                11: (focuses.aquire_focus, "Persuasion"),
                12: (abilities.level_up, "Perception"),
            },
            female_names = {
                "Alowar", "Celemor", "Elowen", "Faerenel", "Hereal",
                "Lanathiel"
            },
            male_names = {
                "Alagolin", "Effolond", "Kyriel", "Larrendir", "Melloran",
                "Serren"
            },
            family_names = {
                "Andurad", "Arvanor", "Derendil", "Ellendi", "Kellovan",
                "Talloran"
            }
        )

class Gnome(Race):
    def __init__(self):
        super().__init__(
            character = character,
            name = "Gnome",
            description="The gimps",
            min_height = 3,
            max_height = 4,
            given_stats = [
                (ability.level_up, "Dexterity"),
                (
                    focuses.choose_focus,
                    (
                        focuses.Focus("Stamina"),
                        focuses.Focus("Legerdemain")
                    )
                )
                (characer.dark_sight, True),
                (character.base_speed, 8),
                (languages.add_language, "Gnomish")
                (languages.add_language, "Common Tongue")
            ],
            benefit_schedule = {
                2: (abilities.level_up, "Constitution"),
                3: (focuses.aquire_focus, "Traps"),
                4: (focuses.aquire_focus, "Traps"),
                5: (focuses.aquire_focus, "Evaluatoin"),
                6: (focuses.aquire_focus, "Hearing"),
                7: (abilities.level_up, "Willpower"),
                8: (abilities.level_up, "Willpower"),
                9: (focuses.aquire_focus, "Arcane Lore"),
                10: (focuses.aquire_focus, "Bargaining"),
                11: (focuses.aquire_focus, "Bargaining"),
                12: (abilities.level_up, "Intelligence"),
            },
            female_names = {
            },
            male_names = {
            },
            family_names = {
            }
        )


class Halfling(Race):
    def __init__(self):
        super().__init__(
            character = character,
            name = "Halfling",
            description="The super gimps",
            min_height = 2,
            max_height = 3,
            given_stats = [
                (ability.level_up, "Dexterity"),
                (
                    focuses.choose_focus,
                    (
                        focuses.Focus("Bargaining"),
                        focuses.Focus("Stealth")
                    )
                )
                (characer.dark_sight, False),
                (character.base_speed, 8),
                (languages.add_language, "Halfling")
                (languages.add_language, "Common Tongue")
            ],
            benefit_schedule = {
                2: (abilities.level_up, "Perception"),
                3: (focuses.aquire_focus, "Persuasion"),
                4: (focuses.aquire_focus, "Persuasion"),
                5: (focuses.aquire_focus, "Initiative"),
                6: (focuses.aquire_focus, "Courage"),
                7: (abilities.level_up, "Communication"),
                8: (abilities.level_up, "Communication"),
                9: (focuses.aquire_focus, "Hearing"),
                10: (focuses.aquire_focus, "Climbing"),
                11: (focuses.aquire_focus, "Climbing"),
                12: (abilities.level_up, "Accuracy"),
            },
            female_names = {
            },
            male_names = {
            },
            family_names = {
            }
        )

class Human(Race):
    def __init__(self):
        super().__init__(
            character = character,
            name = "Human",
            description="Master race",
            min_height = 4,
            max_height = 7,
            given_stats = [
                (ability.level_up, "Fighting"),
                (
                    focuses.choose_focus,
                    (
                        focuses.Focus("Riding"),
                        focuses.Focus("Swimming")
                    )
                )
                (characer.dark_sight, False),
                (character.base_speed, 10)
                (languages.add_language, "Common Tongue")
            ],
            benefit_schedule = {
                2: (abilities.level_up, "Intelligence"),
                3: (focuses.aquire_focus, "Stamina"),
                4: (focuses.aquire_focus, "Searching"),
                5: (focuses.aquire_focus, "Searching"),
                6: (focuses.aquire_focus, "Persuasion"),
                7: (abilities.level_up, "Constitution"),
                8: (abilities.level_up, "Constitution"),
                9: (focuses.aquire_focus, "Deception"),
                10: (focuses.aquire_focus, "Brawling"),
                11: (focuses.aquire_focus, "Brawling"),
                12: (abilities.level_up, "Strength"),
            },
            female_names = {
                "Catrin", "Iona", "Lyn", "Nikki", "Sienna", "Zara"
            },
            male_names = {
                "Aarin", "Donal", "Jorm", "Kellan", "Marric", "Thom"
            },
            family_names = {
                "Baker", "Cooper", "Smith", "Ward", "Highgate", "Lakeside",
                "Silverton"
            }
        )


class Orc(Race):
    def __init__(self):
        super().__init__(
            character = character,
            name = "Orc",
            description="Shitskin",
            min_height = 5,
            max_height = 7,
            given_stats = [
                (ability.level_up, "Strength"),
                (
                    focuses.choose_focus,
                    (
                        focuses.Focus("Stamina"),
                        focuses.Focus("Might")
                    )
                )
                (characer.dark_sight, True),
                (character.base_speed, 10),
                (languages.add_language, "Orcish")
                (languages.add_language, "Common Tongue")
            ],
            benefit_schedule = {
                2: (abilities.level_up, "Constitution"),
                3: (focuses.aquire_focus, "Smelling"),
                4: (focuses.aquire_focus, "Smelling"),
                5: (focuses.aquire_focus, "Stealth"),
                6: (focuses.aquire_focus, "Intimidation"),
                7: (abilities.level_up, "Fighting"),
                8: (abilities.level_up, "Fighting"),
                9: (weapon_groups.learn_group, "Bludgeons"),
                10: (focuses.aquire_focus, "Brawling"),
                11: (focuses.aquire_focus, "Brawling"),
                12: (abilities.level_up, "Willpower"),
            },
            female_names = {
                "Beska", "Eldra", "Grisha", "Mag", "Oota", "Vol"
            },
            male_names = {
                "Feld", "Gar", "Harsk", "Kurg", "Skag", "Tor"
            },
            family_names = {
                "Blackfire", "Heartblood", "Irontusk", "Redaxe", "Sunder"
            }
        )

class Saurian(Race):
    def __init__(self):
        super().__init__(
            character = character,
            name = "Saurian",
            description="Polititian",
            min_height = 5,
            max_height = 7,
            given_stats = [
                (ability.level_up, "Strength"),
                (
                    focuses.choose_focus,
                    (
                        focuses.Focus("Scientific Lore"),
                        focuses.Focus("Self-Discipline")
                    )
                )
                (characer.dark_sight, False),
                (character.base_speed, 10),
                (languages.add_language, "Saurian")
                (languages.add_language, "Common Tongue")
            ],
            benefit_schedule = {
                2: (abilities.level_up, "Willpower"),
                3: (focuses.aquire_focus, "Stamina"),
                4: (focuses.aquire_focus, "Stamina"),
                5: (focuses.aquire_focus, "Historical Lore"),
                6: (focuses.aquire_focus, "Engineering"),
                7: (abilities.level_up, "Intelligence"),
                8: (abilities.level_up, "Intelligence"),
                9: (focuses.aquire_focus, "Computers"),
                10: (focuses.aquire_focus, "Intimidation"),
                11: (focuses.aquire_focus, "Intimidation"),
                12: (abilities.level_up, "Constitution"),
            },
            female_names = {
            },
            male_names = {
            },
            family_names = {
            }
        )
