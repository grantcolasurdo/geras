"""Traits of races"""

__author__ = "Grant Colasurdo"

import characters

class Race:
    def __init__(
        self, character=None, name=None, min_height=None, max_height = None 
    ):
        self.character = character 
        self.race_name = name 
        self.min_height = min_height
        self.max_height = max_height
        
