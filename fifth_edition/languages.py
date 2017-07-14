"""Package for language comprehension"""

__author__ = "Grant Colasurdo"


class Language:
    """A object holding proficiency information in regards to a language"""
    def __init__(self):
        self.language_name: str = None
        self.can_speak: bool = None
        self.can_read: bool = None
        self.can_wright: bool = None
        self.written_script: Language = None


class Common(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Common, self).__init__()
        self.language_name = "Common"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Common


class Dwarvish(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Dwarvish, self).__init__()
        self.language_name = "Dwarvish"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Dwarvish


class Elvish(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Elvish, self).__init__()
        self.language_name = "Elvish"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Elvish


class Giant(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Giant, self).__init__()
        self.language_name = "Giant"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Dwarvish


class Gnomish(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Gnomish, self).__init__()
        self.language_name = "Gnomish"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Dwarvish


class Goblin(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Goblin, self).__init__()
        self.language_name = "Goblin"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Dwarvish


class Halfling(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Halfling, self).__init__()
        self.language_name = "Halfling"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Common


class Orc(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Orc, self).__init__()
        self.language_name = "Orc"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Dwarvish


class Abyssal(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Abyssal, self).__init__()
        self.language_name = "Abyssal"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Infernal


class Celestial(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Celestial, self).__init__()
        self.language_name = "Celestial"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Celestial


class Draconic(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Draconic, self).__init__()
        self.language_name = "Draconic"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Draconic


class DeepSpeech(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(DeepSpeech, self).__init__()
        self.language_name = "Deep Speech"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = None


class Infernal(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Infernal, self).__init__()
        self.language_name = "Infernal"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Infernal


class Primordial(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Primordial, self).__init__()
        self.language_name = "Primordial"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Dwarvish


class Sylvan(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Sylvan, self).__init__()
        self.language_name = "Sylvan"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Elvish


class Undercommon(Language):
    def __init__(self, can_speak: bool, can_read: bool, can_write: bool):
        super(Undercommon, self).__init__()
        self.language_name = "Undercommon"
        self.can_speak = can_speak
        self.can_read = can_read
        self.can_wright = can_write
        self.written_script = Elvish


ALL_LANGUAGES = {
    "Common": Common,
    "Dwarvish": Dwarvish,
    "Elvish": Elvish,
    "Giant": Giant,
    "Gnomish": Gnomish,
    "Goblin": Goblin,
    "Halfling": Halfling,
    "Orc": Orc,
    "Abyssal": Abyssal,
    "Celestial": Celestial,
    "Draconic": Draconic,
    "Deep Speech": DeepSpeech,
    "Infernal": Infernal,
    "Primordial": Primordial,
    "Sylvan": Sylvan,
    "Undercommon": Undercommon
}

LANGUAGE_SET = {
    Common,
    Dwarvish,
    Elvish,
    Giant,
    Gnomish,
    Goblin,
    Halfling,
    Orc,
    Abyssal,
    Celestial,
    Draconic,
    DeepSpeech,
    Infernal,
    Primordial,
    Sylvan,
    Undercommon
}
