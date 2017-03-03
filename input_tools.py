"""Handles input from the user"""

__author__ = "Grant Colasurdo"

def InputResponse(caption, options):
    print(caption)
    print(' '.join(options))
    choice = input('')
    while choice not in options:
        choice = input('Try again ')
    return choice



