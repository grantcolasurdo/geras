"""Package for language comprehension"""

import input_tools

__author__ = "Grant Colasurdo"

def add_language(character, language_name: Language):
    try:
        character.languages.add_language(language_name)
    except:
        print("something went wrong when adding a language")

class Languages:
    def __init__(self, character):
        self.character = character
        self.language_pool = set()

    def is_language_known(self, language_name: str) -> bool:
        return any(
            language.name == language_name for language in
            self.language_pool
        )

    def get_language(self, language_name: str) -> Language:
        if is_language_known(language_name):
            pass
        else:
            self.add_language(Language(self, language_name, 0))
        return self.language_pool[language_name]

    def add_language(self, language_name, level):
        """Add the language to the Languages group at the level level"""
        if is_language_known == False:
            self.language_pool[language_name] = Language(
                language_name,
                level
            )
        else:
            print(
                "Language already known. " + 
                language_name + 
                "No changes were made"
            )


class Language:
    def __init__(
        self,
        languages: Languages,
        language_name: str,
        level: int = 0
    ):
        self.languages = languages
        self.name  = language_name
        self.level = level

    def level_up(self):
        if self.level < 3:
            self.level += 1

    @property
    def can_speak(self) -> bool:
        if level >= 1:
            return True
        else:
            return False

    @can_speak.setter
    def can_speak(self, value: bool):
        if value:
            while self.level < 1:
                self.level += 1
        else:
            while self.level >= 1:
                self.level += -1

    @property
    def can_read(self) -> bool:
        if level >= 2:
            return True
        else:
            return False

    @can_read.setter
    def can_read(self, value: bool):
        if value:
            while self.level < 2:
                self.level += 1
        else:
            while self.level >= 2:
                self.level += -1

    @property
    def can_pass_as_native(self) -> bool:
        if self.level >= 3:
            return True
        else:
            return False

    @can_pass_as_native.setter
    def can_pass_as_native(self, value: bool):
        if value:
            while self.value < 3:
                self.level += -1
        else:
            while self.level >=3:
                self.level += -1

