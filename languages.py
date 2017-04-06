"""Package for language comprehension"""

__author__ = "Grant Colasurdo"


class Language:
    """A object holding proficiency information in regards to a language
    
    Parameters
    ----------
    languages: Languages
        The object holding the meta-level information of a characters language knowledge
    language_name:  str
        The name of the language, used as an identifier
    level: int
        The level of proficiency starting at 0 - no knowledge to 3 - indistinguishable from native
        
    Attributes
    ----------
    languages: Languages
        The object holding the meta-level information of a characters language knowledge
    language_name:  str
        The name of the language, used as an identifier
    level: int
        The level of proficiency starting at 0 - no knowledge to 3 - indistinguishable from native
    
    """
    def __init__(
        self,
        languages: Languages,
        language_name: str,
        level: int = 0
    ):
        self.languages = languages
        self.name = language_name
        self.level = level

    def level_up(self):
        """Increment the language proficiency by 1 level."""
        if self.level < 3:
            self.level += 1

    @property
    def can_speak(self) -> bool:
        """Return a boolean that represents weather or not the character can speak the language."""
        if self.level >= 1:
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
        """Return a boolean that represents weather or not the character can read in the language"""
        if self.level >= 2:
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
        """Return a boolean that represents weather or not the character can pass as a native while communicating"""
        if self.level >= 3:
            return True
        else:
            return False

    @can_pass_as_native.setter
    def can_pass_as_native(self, value: bool):
        if value:
            while self.level < 3:
                self.level += -1
        else:
            while self.level >= 3:
                self.level += -1


class Languages:
    """The meta-info management layer of languages known by a character
    
    Note
    ----
    
    Parameters
    ----------
    character: Character
        The character object that the languages object is attached to.
        
    Attributes
    ----------
    character:  Character
        The character object that the languages object is attached to.
    language_pool:  set
        The set object that holds all the Language objects
        
    """
    def __init__(self, character):
        self.character = character
        self.language_pool = set()

    def is_language_known(self, language_name: str) -> bool:
        """Check language_pool for elements with the name language_name and return true if found
        
        Parameters
        ----------
        language_name: str
            The name of the language you are checking for
            
        Return
        ------
        bool
            True if there is a Language in language_pool with the name language_name
            
        """
        return any(
            language.name == language_name for language in
            self.language_pool
        )

    def get_language(self, language_name: str) -> Language:
        """Find a Language object with the name language_name and return it.
        
        Note
        ----
        If there is no Language of the name `language_name`, a Language object is created with the name language_name,
        it has an initial level of 0, and then it is added to language_pool and returned.
        
        Parameters
        ----------
        language_name: str
            The name of the language you are checking for
            
        Return
        ------
        Language
            A Language object with the name `language_name`
            
        """
        if not self.is_language_known(language_name):
            self.add_language(language_name, 0)
        matching_languages = {language for language in self.language_pool if language.name == language_name}
        if len(matching_languages) == 1:
            return matching_languages.pop()
        else:
            print("There were more than 2 languages of that name")

    def add_language(self, language_name, level):
        """Add a new Language to the Languages object at the proficiency level `level`
        
        Parameters
        ----------
        language_name: str
            The name of the language you are adding
        level: int
            The initial proficiency level the Language should be at
            
        """
        if not self.is_language_known(language_name):

            new_language = Language(
                self,
                language_name,
                level
            )
            self.language_pool.add(new_language)
        else:
            print(
                "Language already known. " + 
                language_name + 
                "No changes were made"
            )


def add_language(character, language_name: str):
    try:
        character.languages.add_language(language_name)
    except Exception:
        print("something went wrong when adding a language")
