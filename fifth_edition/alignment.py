"""Categorizing the alignment in D&D"""

__author__ = "Grant Colasurdo"


class Alignment:
    def __init__(self, short_form):
        self._lawful = None
        self._chaotic = None
        self._good = None
        self._evil = None
        self.short_form = short_form

    @property
    def short_form(self) -> str:
        string = []
        if self._lawful:
            string.append("L")
        elif self._chaotic:
            string.append("C")
        else:
            string.append("N")
        if self._good:
            string.append("G")
        elif self._evil:
            string.append("E")
        else:
            string.append("N")
        if "".join(string) == "NN":
            string.pop()
        return "".join(string)

    @short_form.setter
    def short_form(self, value: str):
        self._lawful = False
        self._chaotic = False
        self._evil = False
        self._good = False
        if "L" in value:
            self._lawful = True
            self._chaotic = False
        elif "C" in value:
            self._chaotic = True
            self._lawful = False
        if "E" in value:
            self._evil = True
            self._good = False
        elif "G" in value:
            self._good = True
            self._evil = False

    @property
    def long_form(self):
        string = []
        if self._lawful:
            string.append("Lawful")
        if self._chaotic:
            string.append("Chaotic")
        if self._good:
            string.append("Good")
        if self._evil:
            string.append("Evil")
        if len(string) == 0:
            string.append("True")
            string.append("Neutral")
        elif len(string) == 2:
            pass
        else:
            string.append("Neutral")
        return " ".join(string)

    @long_form.setter
    def long_form(self, value):
        self._lawful = False
        self._chaotic = False
        self._evil = False
        self._good = False
        if "Lawful" in value:
            self._lawful = True
            self._chaotic = False
        elif "Chaotic" in value:
            self._chaotic = True
            self._lawful = False
        if "Evil" in value:
            self._evil = True
            self._good = False
        elif "Good" in value:
            self._good = True
            self._evil = False
