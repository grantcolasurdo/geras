"""This is the root for the GUI"""

from tkinter import *
import characters

__author__ = "Grant Colasurdo"


class CharacterSheet:
    def __init__(self):
        self.root = Tk()
        self.root.title("Character Sheet")
        menu_button = Menubutton(self.root, height=1)
        menu_button.pack()
        menu = Menu(menu_button)
        menu.pack()
        ability_frame = Frame(self.root, bd='1m', relief=GROOVE)  # For the ability stats
        new_char = characters.Character()
        new_char.init_new_character()
        label_text = "Accuracy: " + str(new_char.abilities.accuracy)
        label = Label(ability_frame, text=label_text)
        label.pack()
        ability_frame.pack()
        basic_frame = Frame(self.root, bd='1m', relief=GROOVE)  # For name, description, background etc...
        basic_frame.pack()
        calculated_frame = Frame(self.root, bd='1m', relief=GROOVE)  # Speed, defense,
        calculated_frame.pack()
        magic_frame = Frame(self.root, bd='1m', relief=GROOVE)
        magic_frame.pack()
        self.root.mainloop()


a = CharacterSheet()
