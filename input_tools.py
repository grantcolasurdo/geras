"""Handles input from the user"""

__author__ = "Grant Colasurdo"


def input_response(caption, options=None) -> str:
    print(caption)
    if options is not None:
        print(' '.join(options))
    choice = input('')
    if options is not None:
        while choice not in options:
            choice = input('Try again ')
    return choice
