"""Alignment object class"""

__author__ = "Grant Colasurdo"


class Alignment:
    SHORT_TO_LONG = {
        'N': 'Neutral',
        'G': 'Good',
        'E': 'Evil',
        'C': 'Chaotic',
        'L': 'Lawful',
        '': ''
    }

    def __init__(self, short_string: str=""):

        if "L" in short_string:
            self._LawChaos = "L"
        if "C" in short_string:
            self._LawChaos = "C"
        if "G" in short_string:
            self._GoodEvil = "G"
        if "E" in short_string:
            self._GoodEvil = "E"
        if "N" in short_string:
            if "NG" in short_string or "NE" in short_string:
                self._LawChaos = "N"
            if "LN" in short_string or "CN" in short_string:
                self._GoodEvil = "N"
            if short_string == "N":
                self._LawChaos = "N"
                self._GoodEvil = "N"

    @property
    def short_string(self):
        string = self._LawChaos + self._GoodEvil
        if string == "NN":
            string = "N"
        return string

    @property
    def long_string(self):
        law_chaos = self.short_to_long[self._LawChaos]
        good_evil = self.short_to_long[self._GoodEvil]
        string = (law_chaos + " " + good_evil).strip()
        if string == "Neutral Neutral":
            string = "True Neutral"
        return string

    @property
    def is_lawful(self):
        return self._LawChaos == "L"

    @is_lawful.setter
    def is_lawful(self, value: bool):
        if value:
            self._LawChaos = "L"
        elif self.is_lawful:
            self._LawChaos = ""
        else:
            pass

    @property
    def is_good(self):
        return self._GoodEvil == "G"

    @is_good.setter
    def is_good(self, value: bool):
        if value:
            self._GoodEvil = "G"
        elif self.is_good:
            self._GoodEvil = ""
        else:
            pass

    @property
    def is_chaotic(self):
        return self._LawChaos == "C"

    @is_chaotic.setter
    def is_chaotic(self, value: bool):
        if value:
            self._LawChaos = "C"
        elif self.is_chaotic:
            self._LawChaos = ""
        else:
            pass

    @property
    def is_evil(self):
        return self._GoodEvil == "E"

    @is_evil.setter
    def is_evil(self, value: bool):
        if value:
            self._GoodEvil = "E"
        elif self.is_evil:
            self._GoodEvil = ""
        else:
            pass

    @property
    def is_neutral_law_chaos(self):
        return self._LawChaos == "N"

    @is_neutral_law_chaos.setter
    def is_neutral_law_chaos(self, value: bool):
        if value:
            self._LawChaos = "N"
        elif self.is_neutral_law_chaos:
            self._LawChaos = ""
        else:
            pass

    @property
    def is_neutral_good_evil(self):
        return self._GoodEvil == "N"

    @is_neutral_good_evil.setter
    def is_neutral_good_evil(self, value: bool):
        if value:
            self._GoodEvil = "N"
        elif self.is_neutral_good_evil:
            self._GoodEvil = ""
        else:
            pass
