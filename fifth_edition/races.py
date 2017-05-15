"""Traits of races"""

from fifth_edition import characters
from fifth_edition import input_tools
from fifth_edition import languages
from fifth_edition import abilities
from fifth_edition import weapon_groups

__author__ = "Grant Colasurdo"


class Race:
    def __init__(self, character: characters.Character):
        self.character = character
        self.race_name = None
        self.female_names = None
        self.male_names = None
        self.family_names = None
        self.description = None
        self.ability_score_increases = None
        self.age_of_majority = None
        self.lifespan = None
        self.traditional_alignment = None
        self.size_class = None
        self.low_height = None
        self.high_height = None
        self.low_weight = None
        self.high_weight = None
        self.base_speed = None
        self.languages = None
        self.additional_traits = None


class Dwarf(Race):
    def __init__(self, character):
        super().__init__(
            character=character,
            name="Dwarf",
            description="Short harry people",
            min_height=4,
            max_height=5,
            base_speed=8,
            dark_sight=True,
            given_stats=[
                (abilities.level_up, "Constitution"),
                (focuses.choose_focus, ["Evaluation", "Drinking"]),
                (languages.add_language, "Dwarven", 3),
                (languages.add_language, "Common Tongue", 2)
            ],
            female_names={
                "Ailine", "Dara", "Kalin", "Klara", "Mora",
                "Telka", "Ulma"
            },
            male_names={
                "Bodag", "Crag", "Doffin", "Hador", "Gurt", "Throrik",
                "Warrik"
            },
            family_names={
                "Bronzeblade", "Highcliff", "Ironshield", "Rockhammer",
                "Steelhelm", "Stonebones"
            },
            benefit_schedule={
                2: (abilities.level_up, "Willpower"),
                3: (focuses.acquire_focus, "Historacal Lore"),
                4: (focuses.acquire_focus, "Historacal Lore"),
                5: (focuses.acquire_focus, "Stamina"),
                6: (weapon_groups.learn_group, "Axes"),
                7: (abilities.level_up, "Fighting"),
                8: (abilities.level_up, "Fighting"),
                9: (focuses.acquire_focus, "Smithing"),
                10: (focuses.acquire_focus, "Engineering"),
                11: (focuses.acquire_focus, "Engineering"),
                12: (abilities.level_up, "Strength")
            }

        )


class Elf(Race):
    def __init__(self, character):
        super().__init__(
            character=character,
            name="Elf",
            description="Dirt worshiper",
            min_height=5,
            max_height=6,
            base_speed=12,
            dark_sight=True,
            given_stats=[
                (abilities.level_up, "Dexterity"),
                (focuses.choose_focus, ["Natural Lore", "Seeing"]),
                (languages.add_language, "Elven", 3),
                (languages.add_language, "Common Tongue", 2)
            ],
            benefit_schedule={
                2: (abilities.level_up, "Communication"),
                3: (focuses.acquire_focus, "Cultural Lore"),
                4: (focuses.acquire_focus, "Cultural Lore"),
                5: (focuses.acquire_focus, "Hearing"),
                6: (weapon_groups.learn_group, "Bows"),
                7: (abilities.level_up, "Accuracy"),
                8: (abilities.level_up, "Accuracy"),
                9: (focuses.acquire_focus, "Initiative"),
                10: (focuses.acquire_focus, "Persuasion"),
                11: (focuses.acquire_focus, "Persuasion"),
                12: (abilities.level_up, "Perception"),
            },
            female_names={
                "Alowar", "Celemor", "Elowen", "Faerenel", "Hereal",
                "Lanathiel"
            },
            male_names={
                "Alagolin", "Effolond", "Kyriel", "Larrendir", "Melloran",
                "Serren"
            },
            family_names={
                "Andurad", "Arvanor", "Derendil", "Ellendi", "Kellovan",
                "Talloran"
            }
        )


class Gnome(Race):
    def __init__(self, character):
        super().__init__(
            character=character,
            name="Gnome",
            description="The gimps",
            min_height=3,
            max_height=4,
            base_speed=8,
            dark_sight=True,
            given_stats=[
                (abilities.level_up, "Dexterity"),
                (focuses.choose_focus, ["Stamina", "Legerdemain"]),
                (languages.add_language, "Gnomish", 3),
                (languages.add_language, "Common Tongue", 2)
            ],
            benefit_schedule={
                2: (abilities.level_up, "Constitution"),
                3: (focuses.acquire_focus, "Traps"),
                4: (focuses.acquire_focus, "Traps"),
                5: (focuses.acquire_focus, "Evaluation"),
                6: (focuses.acquire_focus, "Hearing"),
                7: (abilities.level_up, "Willpower"),
                8: (abilities.level_up, "Willpower"),
                9: (focuses.acquire_focus, "Arcane Lore"),
                10: (focuses.acquire_focus, "Bargaining"),
                11: (focuses.acquire_focus, "Bargaining"),
                12: (abilities.level_up, "Intelligence"),
            },
            female_names={
            },
            male_names={
            },
            family_names={
            }
        )


class Halfling(Race):
    def __init__(self, character):
        super().__init__(
            character=character,
            name="Halfling",
            description="The super gimps",
            min_height=2,
            max_height=3,
            base_speed=8,
            dark_sight=False,
            given_stats=[
                (abilities.level_up, "Dexterity"),
                (focuses.choose_focus, ["Bargaining", "Stealth"]),
                (languages.add_language, "Halfling", 3),
                (languages.add_language, "Common Tongue", 2)
            ],
            benefit_schedule={
                2: (abilities.level_up, "Perception"),
                3: (focuses.acquire_focus, "Persuasion"),
                4: (focuses.acquire_focus, "Persuasion"),
                5: (focuses.acquire_focus, "Initiative"),
                6: (focuses.acquire_focus, "Courage"),
                7: (abilities.level_up, "Communication"),
                8: (abilities.level_up, "Communication"),
                9: (focuses.acquire_focus, "Hearing"),
                10: (focuses.acquire_focus, "Climbing"),
                11: (focuses.acquire_focus, "Climbing"),
                12: (abilities.level_up, "Accuracy"),
            },
            female_names={
                "Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia",
                "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani",
                "Verna"
            },
            male_names={
                "Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal",
                "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"
            },
            family_names={
                "Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Leagallow",
                "Tealeaf", "Thorngage", "Tosscobble", "Underbough"
            }
        )


class Human(Race):
    def __init__(self, character):
        super().__init__(
            character=character,
            name="Human",
            description="Master race",
            min_height=4,
            max_height=7,
            base_speed=10,
            dark_sight=False,
            given_stats=[
                (abilities.level_up, "Fighting"),
                (focuses.choose_focus, ["Riding", "Swimming"]),
                (languages.add_language, "Common Tongue", 3)
            ],
            benefit_schedule={
                2: (abilities.level_up, "Intelligence"),
                3: (focuses.acquire_focus, "Stamina"),
                4: (focuses.acquire_focus, "Searching"),
                5: (focuses.acquire_focus, "Searching"),
                6: (focuses.acquire_focus, "Persuasion"),
                7: (abilities.level_up, "Constitution"),
                8: (abilities.level_up, "Constitution"),
                9: (focuses.acquire_focus, "Deception"),
                10: (focuses.acquire_focus, "Brawling"),
                11: (focuses.acquire_focus, "Brawling"),
                12: (abilities.level_up, "Strength"),
            },
            female_names={
                "Catrin", "Iona", "Lyn", "Nikki", "Sienna", "Zara"
            },
            male_names={
                "Aarin", "Donal", "Jorm", "Kellan", "Marric", "Thom"
            },
            family_names={
                "Baker", "Cooper", "Smith", "Ward", "Highgate", "Lakeside",
                "Silverton"
            }
        )


class Orc(Race):
    def __init__(self, character):
        super().__init__(
            character=character,
            name="Orc",
            description="Shitskin",
            min_height=5,
            max_height=7,
            base_speed=10,
            dark_sight=True,
            given_stats=[
                (abilities.level_up, "Strength"),
                (focuses.choose_focus, ["Stamina", "Might"]),
                (languages.add_language, "Orcish", 3),
                (languages.add_language, "Common Tongue", 2)
            ],
            benefit_schedule={
                2: (abilities.level_up, "Constitution"),
                3: (focuses.acquire_focus, "Smelling"),
                4: (focuses.acquire_focus, "Smelling"),
                5: (focuses.acquire_focus, "Stealth"),
                6: (focuses.acquire_focus, "Intimidation"),
                7: (abilities.level_up, "Fighting"),
                8: (abilities.level_up, "Fighting"),
                9: (weapon_groups.learn_group, "Bludgeons"),
                10: (focuses.acquire_focus, "Brawling"),
                11: (focuses.acquire_focus, "Brawling"),
                12: (abilities.level_up, "Willpower"),
            },
            female_names={
                "Beska", "Eldra", "Grisha", "Mag", "Oota", "Vol"
            },
            male_names={
                "Feld", "Gar", "Harsk", "Kurg", "Skag", "Tor"
            },
            family_names={
                "Blackfire", "Heartblood", "Irontusk", "Redaxe", "Sunder"
            }
        )


class Saurian(Race):
    def __init__(self, character):
        super().__init__(
            character=character,
            name="Saurian",
            description="Polititian",
            min_height=5,
            max_height=7,
            base_speed=10,
            dark_sight=False,
            given_stats=[
                (abilities.level_up, "Strength"),
                (focuses.choose_focus, ["Scientific Lore", "Self-Discipline"]),
                (languages.add_language, "Saurian", 3),
                (languages.add_language, "Common Tongue", 2)
            ],
            benefit_schedule={
                2: (abilities.level_up, "Willpower"),
                3: (focuses.acquire_focus, "Stamina"),
                4: (focuses.acquire_focus, "Stamina"),
                5: (focuses.acquire_focus, "Historical Lore"),
                6: (focuses.acquire_focus, "Engineering"),
                7: (abilities.level_up, "Intelligence"),
                8: (abilities.level_up, "Intelligence"),
                9: (focuses.acquire_focus, "Computers"),
                10: (focuses.acquire_focus, "Intimidation"),
                11: (focuses.acquire_focus, "Intimidation"),
                12: (abilities.level_up, "Constitution"),
            },
            female_names={
            },
            male_names={
            },
            family_names={
            }
        )

RACE_DICT = {
    "Dwarf": Dwarf,
    "ElF": Elf,
    "Gnome": Gnome,
    "Halfling": Halfling,
    "Human": Human,
    "Orc": Orc,
    "Saurian": Saurian
}


def choose_race() -> Race:
    possible_races = {key for key in RACE_DICT}
    selected_race = input_tools.input_response("Choose your race", possible_races)
    character_race = RACE_DICT[selected_race]
    return character_race
