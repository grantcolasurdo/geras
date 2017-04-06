"""This is the root for the GUI"""

from tkinter import *
import characters
import abilities

__author__ = "Grant Colasurdo"


class CharacterSheet:
    def pass_command(self):
        pass

    def init_new_character(self):
        new_character = characters.Character()
        new_character.init_new_character()
        self.character = new_character

    def __init__(self):
        self.root = Tk()
        self.root.title("Character Sheet")
        menu_bar = Menu(self.root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=characters.Character())
        file_menu.add_command(label="Open", command=self.pass_command)
        file_menu.add_command(label="Save", command=self.pass_command)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.pass_command)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

        #: All the abilities should show up here
        ability_frame = Frame(self.root, bd='1m', relief=GROOVE)  # For the ability stats
        ability_frame.pack()
        ability_row = 0
        ability_vars = {}
        for ability in abilities.ABILITY_LIST:
            Label(
                ability_frame,
                text=ability
            ).grid(row=ability_row, column=0)
            ability_vars[ability] = StringVar()
            Entry(
                ability_frame,
                textvariable=ability_vars[ability],
                justify=CENTER,
                state="readonly",
                width=10
            ).grid(row=ability_row, column=1)
            ability_vars[ability].set("0")
            ability_row += 1

        ability_vars["Intelligence"].set(2)
        basic_frame = Frame(self.root, bd='1m', relief=GROOVE)  # For name, description, background etc...
        basic_frame.pack()
        calculated_frame = Frame(self.root, bd='1m', relief=GROOVE)  # Speed, defense,
        calculated_frame.pack()
        magic_frame = Frame(self.root, bd='1m', relief=GROOVE)
        magic_frame.pack()
        self.root.mainloop()


a = CharacterSheet()
