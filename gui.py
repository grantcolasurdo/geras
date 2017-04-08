"""This is the root for the GUI"""

import tkinter as tk
import characters
import abilities

__author__ = "Grant Colasurdo"


class AbilityFrame(tk.LabelFrame):
    """Display the base Ability data for a character"""
    def __init__(self, parent, *args, **kwargs):
        super(AbilityFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.root = parent.root
        self.config(text="Abilities")
        row = 0
        self.ability_variables = {}
        for ability in abilities.ABILITY_LIST:
            tk.Label(
                self,
                text=ability
            ).grid(row=row, column=0)
            self.ability_variables[ability] = tk.StringVar()
            tk.Entry(
                self,
                textvariable=self.ability_variables[ability],
                justify=tk.CENTER,
                state="readonly",
                width=10
            ).grid(row=row, column=1)
            row += 1

    def update_values(self):
        try:
            character = self.parent.character
            for ability in abilities.ABILITY_LIST:
                self.ability_variables[ability].set(character.abilities.ability_map[ability].value)

        except TypeError:
            print("no character is set")


class BackgroundFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(BackgroundFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.root = parent.root
        self.character_variables = {
            "Character Name": tk.StringVar(),
            "Race": tk.StringVar(),
            "Class": tk.StringVar(),
            "Background": tk.StringVar(),
            "Social Class": tk.StringVar()
        }
        row = 0
        for key in self.character_variables:
            tk.Label(self, text=key).grid(row=row, column=0)
            tk.Entry(
                self,
                textvariable=self.character_variables[key],
                justify=tk.CENTER,
                state="readonly"
            ).grid(row=row, column=1)
            row += 1

    def update_values(self):
        try:
            character = self.parent.character
            self.character_variables["Character Name"].set(character.full_name)
            self.character_variables["Race"].set(character.race.race_name)
            self.character_variables["Class"].set(character.character_class.class_name)
            self.character_variables["Social Class"].set(character.background.social_class)
            self.character_variables["Background"].set(character.background.background_name)
        except TypeError:
            print("There was no character selected yet")


class MenuBar(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super(MenuBar, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.root = parent.root
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="New", command=self.parent.init_new_character)
        file_menu.add_command(label="Open", command=self.pass_command)
        file_menu.add_command(label="Save", command=self.pass_command)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=parent.quit)
        self.add_cascade(label="File", menu=file_menu)
        help_menu = tk.Menu(self, tearoff=0)
        help_menu.add_command(label="About", command=self.pass_command)
        self.add_cascade(label="Help", menu=help_menu)

    def pass_command(self):
        pass


class Experience(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Experience, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.root = parent.root
        self.experience_variables = {
            "Level": tk.StringVar(),
            "Experience Points": tk.StringVar(),
        }
        row = 0
        for key in self.experience_variables:
            tk.Label(self, text=key).grid(row=row, column=0)
            tk.Entry(
                self,
                textvariable=self.experience_variables[key],
                justify=tk.CENTER,
                state="readonly",
                width=10
            ).grid(row=row, column=1)
            row += 1

    def update_values(self):
        try:
            character = self.parent.character
            self.experience_variables["Level"].set(character.level)
            self.experience_variables["Experience Points"].set(character.experience_points)
        except TypeError:
            print("There was no character selected yet.")


class HealthAndArmorFrame(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super(HealthAndArmorFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.root = parent.root
        self.config(text="Your ability to get hit in the face")
        self.health_and_armor_variables = {
            "Health": tk.StringVar(),
            "Max Health": tk.StringVar(),
            "Defense": tk.StringVar(),
            "Armor": tk.StringVar(),
            "Effective Armor": tk.StringVar()
        }
        row = 0
        for key in self.health_and_armor_variables:
            tk.Label(self, text=key).grid(row=row, column=0)
            tk.Entry(
                self,
                textvariable=self.health_and_armor_variables[key],
                justify=tk.CENTER,
                state="readonly",
                width=10
            ).grid(row=row, column=1)
            row += 1

    def update_values(self):
        try:
            character = self.parent.character
            self.health_and_armor_variables["Health"].set(character.current_health)
            self.health_and_armor_variables["Max Health"].set(character.max_health)
            defense_value = 10 + character.abilities.dexterity.value + character.equipment.shield_value
            self.health_and_armor_variables["Defense"].set(defense_value)
            armor_value = character.equipment.armor_value
            self.health_and_armor_variables["Armor"].set(armor_value)
        except TypeError:
            print("There was no character bound to the sheet yet")


class MovementFrame(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super(MovementFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.root = parent.root
        self.config(text="Movement")
        self.movement_variables = {
            "Speed": tk.StringVar(),
            "Armor Penalty": tk.StringVar(),
            "Move": tk.StringVar(),
            "Charge": tk.StringVar(),
            "Run": tk.StringVar()
        }
        row = 0
        for key in self.movement_variables:
            tk.Label(self, text=key).grid(row=row, column=0)
            tk.Entry(
                self,
                textvariable=self.movement_variables[key],
                justify=tk.CENTER,
                state="readonly",
                width=10
            ).grid(row=row, column=1)
            row += 1

    def update_values(self):
        try:
            character = self.parent.character
            base_speed = character.base_speed
            dexterity = character.abilities.dexterity
            armor_penalty = character.equipment.armor_penalty
            effective_speed = base_speed + armor_penalty + dexterity
            self.movement_variables["Speed"].set(effective_speed)
            self.movement_variables["Armor Penalty"].set(armor_penalty)
            self.movement_variables["Move"].set(effective_speed)
            self.movement_variables["Charge"].set(effective_speed // 2)
            self.movement_variables["Run"].set(effective_speed * 2)
        except TypeError:
            print("There was no character bound to the sheet yet")


class MagicFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MagicFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.root = parent.root
        self.magic_variables = {
            "Maximum Magic Points": tk.StringVar(),
            "Current Magic Points": tk.StringVar(),
        }

    def update_values(self):
        pass


class CharacterSheet(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(CharacterSheet, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.root = self.parent
        self.character = None

        self.parent.title("Character Sheet")

        self.menu_bar = MenuBar(self)
        self.ability_frame = AbilityFrame(self)
        self.background_frame = BackgroundFrame(self)
        self.experience_frame = Experience(self)
        self.movement_frame = MovementFrame(self)
        self.health_and_armor_frame = HealthAndArmorFrame(self)
        self.magic_frame = MagicFrame(self)

        self.root.config(menu=self.menu_bar)
        self.ability_frame.grid(row=1, column=0)
        self.background_frame.grid(row=0, column=0)
        self.experience_frame.grid(row=0, column=1)
        self.movement_frame.grid(row=0, column=2)
        self.health_and_armor_frame.grid(row=1, column=1)
        self.magic_frame.grid(row=1, column=2)

    def pass_command(self):
        pass

    def init_new_character(self):
        new_character = characters.Character()
        new_character.init_new_character()
        self.character = new_character
        self.updated_values()

    def updated_values(self):
        self.ability_frame.update_values()
        self.background_frame.update_values()
        self.experience_frame.update_values()
        self.movement_frame.update_values()
        self.health_and_armor_frame.update_values()
        self.magic_frame.update_values()


def select_option_prompt(caption: str, options: list):
    """This exits as a way to prompt the user to select from a list of options"""
    def make_selection():
        prompt = tk.Toplevel()
        prompt.title("Make a selection")

        tk.Label(prompt, text=caption).pack()
        listbox = tk.Listbox(prompt, selectmode=tk.SINGLE)
        listbox.pack()

        for option in options:
            listbox.insert(tk.END, option)

        tk.Button(prompt, text="Select", command=prompt.destroy())

    def select(self):
        selected = self.listbox.curselection()


if __name__ == "__main__":
    root = tk.Tk()
    CharacterSheet(root).pack(anchor=tk.CENTER, fill="both", expand=True)
    root.mainloop()

