"""Traits of races"""

from fifth_edition import characters
from fifth_edition import input_tools
from fifth_edition import alignment
from fifth_edition import languages
from fifth_edition import abilities

__author__ = "Grant Colasurdo"


class Race:
    RACE_NAME = None
    DESCRIPTION = None
    FEMALE_NAMES = None
    MALE_NAMES = None
    FAMILY_NAMES = None
    AGE_OF_MAJORITY = None
    LIFESPAN = None
    TRADITIONAL_ALIGNMENT = None
    SIZE_CLASS = None
    BASE_HEIGHT = None
    HEIGHT_MODIFIER = None
    BASE_WEIGHT = None
    WEIGHT_MODIFIER = None
    BASE_SPEED = None

    def __init__(self, character: 'characters.Character'):
        self.character = character
        self.ability_score_increases = set()
        self.languages = set()
        self.additional_traits = set()
        self.proficiencies = set()
        self.damage_resistances = set()
        self.hit_point_bonus = 0

    def init_race(self):
        self._define_gender()
        self._define_name()
        self._define_height()
        self._define_weight()
        self._define_allignment()

    def _define_gender(self):
        self.character.sex = input_tools.input_response("Choose a gender", ["Male", "Female", "Triggered"])
        if self.character.sex == "Triggered":
            self.character.sex = input_tools.input_response("Try Again", ["Male", "Female"])

    def _define_name(self):
        if self.character.sex == "Male":
            print("These are the common male names for this race")
        else:
            print("These are the common female names for this race")

        self.character.first_name = input_tools.input_response("First Name")
        input_tools.input_response("First Name")

    def _define_height(self):
        pass

    def _define_weight(self):
        pass

    def _define_alignment(self):
        pass


class Dwarf(Race):
    RACE_NAME = "Dwarf"
    DESCRIPTION = "Short harry people"
    AGE_OF_MAJORITY = 50
    LIFESPAN = 350
    TRADITIONAL_ALIGNMENT = alignment.Alignment("LG")
    HEIGHT_MODIFIER = "2d4"
    WEIGHT_MODIFIER = "2d6"
    SIZE_CLASS = "Medium"
    BASE_SPEED = 25
    FEMALE_NAMES = {
        "Ailine", "Dara", "Kalin", "Klara", "Mora",
        "Telka", "Ulma"
    }
    MALE_NAMES = {
        "Bodag", "Crag", "Doffin", "Hador", "Gurt", "Throrik",
        "Warrik"
    }
    FAMILY_NAMES = {
        "Bronzeblade", "Highcliff", "Ironshield", "Rockhammer",
        "Steelhelm", "Stonebones"
    }

    def __init__(self, character: 'characters.Character'):
        super().__init__(character=character)
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Dwarvish(True, True, True))
        self.ability_score_increases.add(abilities.Constitution(2))


class HillDwarf(Dwarf):
    BASE_WEIGHT = 115
    BASE_HEIGHT = 3.667

    def __init__(self, character: 'characters.Character'):
        super(HillDwarf, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Wisdom(1))


class MountainDwarf(Dwarf):
    BASE_WEIGHT = 130
    BASE_HEIGHT = 4

    def __init__(self, character: 'characters.Character'):
        super(MountainDwarf, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Strength(2))


class Elf(Race):
    RACE_NAME = "Elf"
    TRADITIONAL_ALIGNMENT = alignment.Alignment("CG")
    DESCRIPTION = ""
    AGE_OF_MAJORITY = 100
    LIFESPAN = 750
    SIZE_CLASS = "Medium"
    BASE_SPEED = 30

    FEMALE_NAMES = {
        "Alowar", "Celemor", "Elowen", "Faerenel", "Hereal",
        "Lanathiel"
    }
    MALE_NAMES = {
        "Alagolin", "Effolond", "Kyriel", "Larrendir", "Melloran",
        "Serren"
    }
    FAMILY_NAMES = {
        "Andurad", "Arvanor", "Derendil", "Ellendi", "Kellovan",
        "Talloran"
    }

    def __init__(self, character: 'characters.Character'):
        super().__init__(character=character),
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Elvish(True, True, True))
        self.ability_score_increases.add(abilities.Dexterity(2))


class HighElf(Elf):
    RACE_NAME = "Hight elf"
    BASE_HEIGHT = 4.5
    HEIGHT_MODIFIER = "2d10"
    BASE_WEIGHT = 90
    WEIGHT_MODIFIER = "1d4"

    def __init__(self, character: 'characters.Character'):
        super(HighElf, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Intelligence(1))


class WoodElf(Elf):
    RACE_NAME = "Wood elf"
    BASE_HEIGHT = 4.5
    HEIGHT_MODIFIER = "2d10"
    BASE_WEIGHT = 100
    WEIGHT_MODIFIER = "1d4"
    BASE_SPEED = 35

    def __init__(self, character: 'characters.Character'):
        super(WoodElf, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Wisdom(1))


class DrowElf(Elf):
    RACE_NAME = "Drow elf"
    BASE_HEIGHT = 4.417
    HEIGHT_MODIFIER = "2d6"
    BASE_WEIGHT = 75
    WEIGHT_MODIFIER = "1d6"
    TRADITIONAL_ALIGNMENT = alignment.Alignment("CE")

    def __init__(self, character: 'characters.Character'):
        super(DrowElf, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Charisma(1))


class Gnome(Race):
    RACE_NAME = "Gnome"
    AGE_OF_MAJORITY = 40
    LIFESPAN = 500
    TRADITIONAL_ALIGNMENT = alignment.Alignment("NG")
    BASE_HEIGHT = 2.917
    HEIGHT_MODIFIER = "2d4"
    BASE_WEIGHT = 35
    WEIGHT_MODIFIER = "1"
    SIZE_CLASS = "Medium"
    BASE_SPEED = 25
    FEMALE_NAMES = {
    }
    MALE_NAMES = {
    }
    FAMILY_NAMES = {
    }

    def __init__(self, character: 'characters.Character'):
        super().__init__(character=character)
        self.ability_score_increases.add(abilities.Intelligence(2))
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Gnomish(True, True, True))


class ForestGnome(Gnome):
    def __init__(self, character: 'characters.Character'):
        super(ForestGnome, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Dexterity(1))


class RockGnome(Gnome):
    def __init__(self, character: 'characters.Character'):
        super(RockGnome, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Constitution(1))


class Halfling(Race):
    RACE_NAME = "Halfling"
    AGE_OF_MAJORITY = 20
    LIFESPAN = 150
    TRADITIONAL_ALIGNMENT = alignment.Alignment("LG")
    BASE_HEIGHT = 2.583
    HEIGHT_MODIFIER = "2d4"
    BASE_WEIGHT = 35
    WEIGHT_MODIFIER = "1"
    SIZE_CLASS = "Medium"
    BASE_SPEED = 25
    FEMALE_NAMES = {
        "Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia",
        "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani",
        "Verna"
    }
    MALE_NAMES = {
        "Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal",
        "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"
    }
    FAMILY_NAMES = {
        "Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Leagallow",
        "Tealeaf", "Thorngage", "Tosscobble", "Underbough"
    }

    def __init__(self, character: 'characters.Character'):
        super().__init__(character=character)
        self.ability_score_increases.add(abilities.Dexterity(2))
        self.languages.add(languages.Halfling(True, True, True))
        self.languages.add(languages.Common(True, True, True))


class LightFootHalfling(Halfling):
    def __init__(self, character: 'characters.Character'):
        super(LightFootHalfling, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Charisma(1))


class StoutHalfling(Halfling):
    def __init__(self, character: 'characters.Character'):
        super(StoutHalfling, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Constitution(1))


class Human(Race):
    RACE_NAME = "Human"
    AGE_OF_MAJORITY = 17
    LIFESPAN = 90
    TRADITIONAL_ALIGNMENT = alignment.Alignment("N")
    BASE_HEIGHT = 4.667
    HEIGHT_MODIFIER = "2d10"
    BASE_WEIGHT = 110
    WEIGHT_MODIFIER = "2d4"
    SIZE_CLASS = "Medium"
    BASE_SPEED = 30
    FEMALE_NAMES = {
        "Catrin", "Iona", "Lyn", "Nikki", "Sienna", "Zara"
    }
    MALE_NAMES = {
        "Aarin", "Donal", "Jorm", "Kellan", "Marric", "Thom"
    }
    FAMILY_NAMES = {
        "Baker", "Cooper", "Smith", "Ward", "Highgate", "Lakeside",
        "Silverton"
    }

    def __init__(self, character: 'characters.Character'):
        super().__init__(character=character)

        self.ability_score_increases.add(abilities.Strength(1))
        self.ability_score_increases.add(abilities.Dexterity(1))
        self.ability_score_increases.add(abilities.Constitution(1))
        self.ability_score_increases.add(abilities.Intelligence(1))
        self.ability_score_increases.add(abilities.Wisdom(1))
        self.ability_score_increases.add(abilities.Charisma(1))
        self.languages.add(languages.Common(True, True, True))


class HalfOrc(Race):
    RACE_NAME = "Half-orc"
    AGE_OF_MAJORITY = 14
    LIFESPAN = 75
    TRADITIONAL_ALIGNMENT = alignment.Alignment("CE")
    BASE_WEIGHT = 140
    WEIGHT_MODIFIER = "2d10"
    BASE_HEIGHT = 4.833
    HEIGHT_MODIFIER = "2d6"
    BASE_SPEED = 30
    SIZE_CLASS = "Medium"
    FEMALE_NAMES = {
        "Beska", "Eldra", "Grisha", "Mag", "Oota", "Vol"
    }
    MALE_NAMES = {
        "Feld", "Gar", "Harsk", "Kurg", "Skag", "Tor"
    }
    FAMILY_NAMES = {
        "Blackfire", "Heartblood", "Irontusk", "Redaxe", "Sunder"
    }

    def __init__(self, character: 'characters.Character'):
        super().__init__(character=character)
        self.ability_score_increases.add(abilities.Strength(2))
        self.ability_score_increases.add(abilities.Constitution(1))
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Orc(True, True, True))


class Dragonborn(Race):
    RACE_NAME = "Dragonborn"
    TRADITIONAL_ALIGNMENT = alignment.Alignment("LG")
    AGE_OF_MAJORITY = 15
    LIFESPAN = 80
    SIZE_CLASS = "Medium"
    BASE_HEIGHT = 5.5
    HEIGHT_MODIFIER = "2d8"
    BASE_WEIGHT = 175
    WEIGHT_MODIFIER = "2d6"
    BASE_SPEED = 30
    FEMALE_NAMES = {
        "Akra", "Biri", "Daar", "Farideh", "Harann", "Flavilar", "Jheri", "Kava", "Korinn", "Mishann",
        "Nala", "Perra", "Raiann", "Sora", "Surina", "Thava", "Uadjit"
    }
    MALE_NAMES = {
        "Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadarr",
        "Pandjed", "Patrin", "Rhogar", "Shamash", "Shedinn", "Tarhun", "Torinn"
    }
    FAMILY_NAMES = {
    }

    def __init__(self, character: 'characters.Character'):
        super().__init__(character=character)
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
    RACE_NAME = "Half-elf"
    DESCRIPTION = "Walking in two worlds but truly belonging to neither, half-elves combine what " + \
                  "some say are the best qualities of their elf and human parents: human curiosity, " +\
                  "inventiveness, and ambition tempered by the refined senses, love of nature, and " +\
                  "artistic tastes of the elves."
    AGE_OF_MAJORITY = 20
    LIFESPAN = 180
    TRADITIONAL_ALIGNMENT = alignment.Alignment("CN")
    BASE_HEIGHT = 4.75
    HEIGHT_MODIFIER = "2d8"
    BASE_WEIGHT = 110
    WEIGHT_MODIFIER = "2d4"
    SIZE_CLASS = "Medium"
    BASE_SPEED = 30
    FEMALE_NAMES = {
    }
    MALE_NAMES = {
    }
    FAMILY_NAMES = {
    }

    def __init__(self, character: 'characters.Character'):
        super(HalfElf, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Charisma(2))
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Elvish(True, True, True))


class Tiefling(Race):
    MALE_NAMES = {
        "Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Karion", "Leucis", "Melech",
        "Mordai", "Pelaios", "Skamos", "Therai"
    }
    FEMALE_NAMES = {
        "Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia",
        "Orianna", "Phelaia", "Rieta"
    }
    RACE_NAME = "Tiefling"
    DESCRIPTION = ""
    AGE_OF_MAJORITY = 17
    LIFESPAN = 100
    TRADITIONAL_ALIGNMENT = alignment.Alignment("CN")
    BASE_HEIGHT = 4.75
    HEIGHT_MODIFIER = "2d8"
    BASE_WEIGHT = 110
    WEIGHT_MODIFIER = "2d4"
    SIZE_CLASS = "Medium"
    BASE_SPEED = 30

    def __init__(self, character: 'characters.Character'):
        super(Tiefling, self).__init__(character=character)
        self.ability_score_increases.add(abilities.Intelligence(1))
        self.ability_score_increases.add(abilities.Charisma(2))
        self.damage_resistances.add("Fire")
        self.languages.add(languages.Common(True, True, True))
        self.languages.add(languages.Infernal(True, True, True))


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
