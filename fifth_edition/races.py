"""Traits of races"""

from fifth_edition import characters
from fifth_edition import input_tools
from fifth_edition import alignment
from fifth_edition import languages
from fifth_edition import abilities

__author__ = "Grant Colasurdo"


class Race:
    def __init__(self, character: characters.Character):
        self.character = character
        self.race_name = None
        self.description = None
        self.female_names = None
        self.male_names = None
        self.family_names = None
        self.ability_score_increases = set()
        self.age_of_majority = None
        self.lifespan = None
        self.traditional_alignment = None
        self.size_class = None
        self.base_height = None
        self.height_modifier = None
        self.base_weight = None
        self.weight_modifier = None
        self.base_speed = None
        self.languages = set()
        self.additional_traits = set()
        self.proficiencies = set()
        self.damage_resistances = set()
        self.hit_point_bonus = 0


class Dwarf(Race):
    def __init__(self, character: characters.Character):
        super().__init__(character=character)
        self.race_name = "Dwarf",
        self.description = "Short harry people",
        self.age_of_majority = 50
        self.lifespan = 350
        self.traditional_alignment = alignment.Alignment("LG")
        self.height_modifier = "2d4"
        self.weight_modifier = "2d6"
        self.size_class = "Medium"
        self.base_speed = 25,
        self.female_names = {
            "Ailine", "Dara", "Kalin", "Klara", "Mora",
            "Telka", "Ulma"
        },
        self.male_names = {
            "Bodag", "Crag", "Doffin", "Hador", "Gurt", "Throrik",
            "Warrik"
        },
        self.family_names = {
            "Bronzeblade", "Highcliff", "Ironshield", "Rockhammer",
            "Steelhelm", "Stonebones"
        }
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Dwarvish(True, True, True))
        self.ability_score_increases.add(abilities.Constitution(2))


class HillDwarf(Dwarf):
    def __init__(self, character: characters.Character):
        super(HillDwarf, self).__init__(character=character)
        self.base_height = 3.667
        self.base_weight = 115
        self.ability_score_increases.add(abilities.Wisdom(1))


class MountainDwarf(Dwarf):
    def __init__(self, character: characters.Character):
        super(MountainDwarf, self).__init__(character=character)
        self.base_height = 4
        self.base_weight = 130
        self.ability_score_increases.add(abilities.Strength(2))


class Elf(Race):
    def __init__(self, character: characters.Character):
        super().__init__(character=character),
        self.race_name = "Elf",
        self.traditional_alignment = alignment.Alignment("CG")
        self.description = "Dirt worshiper",
        self.age_of_majority = 100
        self.lifespan = 750
        self.size_class = "Medium"
        self.base_speed = 30,
        self.female_names = {
            "Alowar", "Celemor", "Elowen", "Faerenel", "Hereal",
            "Lanathiel"
        },
        self.male_names = {
            "Alagolin", "Effolond", "Kyriel", "Larrendir", "Melloran",
            "Serren"
        },
        self.family_names = {
            "Andurad", "Arvanor", "Derendil", "Ellendi", "Kellovan",
            "Talloran"
        }
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Elvish(True, True, True))
        self.ability_score_increases.add(abilities.Dexterity(2))


class HighElf(Elf):
    def __init__(self, character: characters.Character):
        super(HighElf, self).__init__(character=character)
        self.race_name = "High elf"
        self.base_height = 4.5
        self.height_modifier = "2d10"
        self.base_weight = 90
        self.weight_modifier = "1d4"
        self.ability_score_increases.add(abilities.Intelligence(1))


class WoodElf(Elf):
    def __init__(self, character: characters.Character):
        super(WoodElf, self).__init__(character=character)
        self.race_name = "Wood elf"
        self.base_height = 4.5
        self.height_modifier = "2d10"
        self.base_weight = 100
        self.weight_modifier = "1d4"
        self.ability_score_increases.add(abilities.Wisdom(1))
        self.base_speed = 35


class DrowElf(Elf):
    def __init__(self, character: characters.Character):
        super(DrowElf, self).__init__(character=character)
        self.race_name = "Drow elf"
        self.base_height = 4.417
        self.height_modifier = "2d6"
        self.base_weight = 75
        self.weight_modifier = "1d6"
        self.traditional_alignment = alignment.Alignment("CE")
        self.ability_score_increases.add(abilities.Charisma(1))


class Gnome(Race):
    def __init__(self, character: characters.Character):
        super().__init__(character=character)
        self.race_name = "Gnome",
        self.age_of_majority = 40
        self.lifespan = 500
        self.traditional_alignment = alignment.Alignment("NG")
        self.base_height = 2.917
        self.height_modifier = "2d4"
        self.base_weight = 35
        self.height_modifier = "1"
        self.size_class = "Medium"
        self.base_speed = 25
        self.description = "The gimps",
        self.female_names = {
        },
        self.male_names = {
        },
        self.family_names = {
        }
        self.ability_score_increases.add(abilities.Intelligence(2))
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Gnomish(True, True, True))


class ForestGnome(Gnome):
    def __init__(self, character: characters.Character):
        super(ForestGnome, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Dexterity(1))


class RockGnome(Gnome):
    def __init__(self, character: characters.Character):
        super(RockGnome, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Constitution(1))


class Halfling(Race):
    def __init__(self, character: characters.Character):
        super().__init__(character=character)
        self.race_name = "Halfling",
        self.description = "The super gimps",
        self.age_of_majority = 20
        self.lifespan = 150
        self.traditional_alignment = alignment.Alignment("LG")
        self.base_height = 2.583,
        self.height_modifier = "2d4"
        self.base_weight = 35
        self.weight_modifier = "1"
        self.size_class = "Medium"
        self.base_speed = 25
        self.female_names = {
            "Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia",
            "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani",
            "Verna"
        },
        self.male_names = {
            "Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal",
            "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"
        },
        self.family_names = {
            "Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Leagallow",
            "Tealeaf", "Thorngage", "Tosscobble", "Underbough"
        }
        self.ability_score_increases.add(abilities.Dexterity(2))
        self.languages.add(languages.Halfling(True, True, True))
        self.languages.add(languages.Common(True, True, True))


class LightFootHalfling(Halfling):
    def __init__(self, character: characters.Character):
        super(LightFootHalfling, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Charisma(1))


class StoutHalfling(Halfling):
    def __init__(self, character: characters.Character):
        super(StoutHalfling, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Constitution(1))


class Human(Race):
    def __init__(self, character: characters.Character):
        super().__init__(character=character)
        self.race_name = "Human",
        self.description = "Master race",
        self.age_of_majority = 17
        self.lifespan = 90
        self.traditional_alignment = alignment.Alignment("N")
        self.base_height = 4.667
        self.height_modifier = "2d10"
        self.base_weight = 110
        self.weight_modifier = "2d4"
        self.size_class = "Medium"
        self.base_speed = 30,
        self.female_names = {
            "Catrin", "Iona", "Lyn", "Nikki", "Sienna", "Zara"
        },
        self.male_names = {
            "Aarin", "Donal", "Jorm", "Kellan", "Marric", "Thom"
        },
        self.family_names = {
            "Baker", "Cooper", "Smith", "Ward", "Highgate", "Lakeside",
            "Silverton"
        }
        self.ability_score_increases.add(abilities.Strength(1))
        self.ability_score_increases.add(abilities.Dexterity(1))
        self.ability_score_increases.add(abilities.Constitution(1))
        self.ability_score_increases.add(abilities.Intelligence(1))
        self.ability_score_increases.add(abilities.Wisdom(1))
        self.ability_score_increases.add(abilities.Charisma(1))
        self.languages.add(languages.Common(True, True, True))


class HalfOrc(Race):
    def __init__(self, character: characters.Character):
        super().__init__(character=character)
        self.race_name = "Half-orc"
        self.age_of_majority = 14
        self.lifespan = 75
        self.traditional_alignment = alignment.Alignment("CE")
        self.base_weight = 140
        self.weight_modifier = "2d10"
        self.base_height = 4.833
        self.height_modifier = "2d6"
        self.base_speed = 30,
        self.size_class = "Medium"
        self.female_names = {
            "Beska", "Eldra", "Grisha", "Mag", "Oota", "Vol"
        },
        self.male_names = {
            "Feld", "Gar", "Harsk", "Kurg", "Skag", "Tor"
        },
        self.family_names = {
            "Blackfire", "Heartblood", "Irontusk", "Redaxe", "Sunder"
        }
        self.ability_score_increases.add(abilities.Strength(2))
        self.ability_score_increases.add(abilities.Constitution(1))
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Orc(True, True, True))


class Dragonborn(Race):
    def __init__(self, character: characters.Character):
        super().__init__(character=character)
        self.race_name = "Dragonborn",
        self.description = "",
        self.traditional_alignment = alignment.Alignment("LG")
        self.age_of_majority = 15
        self.lifespan = 80
        self.size_class = "Medium"
        self.base_height = 5.5
        self.height_modifier = "2d8"
        self.base_weight = 175
        self.weight_modifier = "2d6"
        self.base_speed = 30,
        self.female_names = {
            "Akra", "Biri", "Daar", "Farideh", "Harann", "Flavilar", "Jheri", "Kava", "Korinn", "Mishann",
            "Nala", "Perra", "Raiann", "Sora", "Surina", "Thava", "Uadjit"
        },
        self.male_names = {
            "Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadarr",
            "Pandjed", "Patrin", "Rhogar", "Shamash", "Shedinn", "Tarhun", "Torinn"
        },
        self.family_names = {
        }
        self.ability_score_increases.add(abilities.Strength(2))
        self.ability_score_increases.add(abilities.Charisma(1))
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Draconic(True, True, True))
        self._choose_ancestor()

    def _choose_ancestor(self):
        damage_type = {
            "Black": "Acid",
            "Blue": "Lightning",
            "Brass": "Fire",
            "Bronze": "Lightning",
            "Copper": "Acid",
            "Gold": "Fire",
            "Green": "Poison",
            "Red": "Fire",
            "Silver": "Cold",
            "White": "Cold"
        }
        ancestry_damage_type = input_tools.input_response("Chose a draconic ancestry", damage_type)
        self.damage_resistances.add(ancestry_damage_type)


class HalfElf(Race):
    def __init__(self, character: characters.Character):
        super(HalfElf, self).__init__(character=character)
        self.race_name = "Half-elf"
        self.description = "Walking in two worlds but truly belonging to neither, half-elves combine what " + \
                           "some say are the best qualities of their elf and human parents: human curiosity, " +\
                           "inventiveness, and ambition tempered by the refined senses, love of nature, and " +\
                           "artistic tastes of the elves."
        self.age_of_majority = 20
        self.lifespan = 180
        self.traditional_alignment = alignment.Alignment("CN")
        self.base_height = 4.75
        self.height_modifier = "2d8"
        self.base_weight = 110
        self.weight_modifier = "2d4"
        self.size_class = "Medium"
        self.base_speed = 30
        self.female_names = {
        },
        self.male_names = {
        },
        self.family_names = {
        }
        self.ability_score_increases.add(abilities.Charisma(2))
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Elvish(True, True, True))


class Tiefling(Race):
    def __init__(self, character: characters.Character):
        super(Tiefling, self).__init__(character=character)
        self.race_name = "Tiefling"
        self.description = ""
        self.age_of_majority = 17
        self.lifespan = 100
        self.traditional_alignment = alignment.Alignment("CN")
        self.base_height = 4.75
        self.height_modifier = "2d8"
        self.base_weight = 110
        self.weight_modifier = "2d4"
        self.size_class = "Medium"
        self.base_speed = 30
        self.ability_score_increases.add(abilities.Intelligence(1))
        self.ability_score_increases.add(abilities.Charisma(2))
        self.damage_resistances.add("Fire")
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Infernal(True, True, True))
        self.male_names = {
            "Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Karion", "Leucis", "Melech",
            "Mordai", "Pelaios", "Skamos", "Therai"
        }
        self.female_names = {
            "Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia",
            "Orianna", "Phelaia", "Rieta"
        }

RACE_DICT = {
    "Mountain Dwarf": MountainDwarf,
    "Hill Dwarf": HillDwarf,
    "High ElF": HighElf,
    "Wood ElF": WoodElf,
    "Drow ElF": DrowElf,
    "ForestGnome": ForestGnome,
    "RockGnome": RockGnome,
    "Halfling": Halfling,
    "Human": Human,
    "Half-orc": HalfOrc,
    "Half-elf": HalfElf,
    "Tiefling": Tiefling,
    "Dragonborn": Dragonborn
}


def choose_race() -> Race:
    possible_races = {key for key in RACE_DICT}
    selected_race = input_tools.input_response("Choose your race", possible_races)
    character_race = RACE_DICT[selected_race]
    return character_race
