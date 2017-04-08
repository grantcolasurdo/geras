"""Handles input from the user"""

import tkinter as tk

__author__ = "Grant Colasurdo"


class InputObject:
    def __init__(self):
        self.value = None


def input_response(caption, options=None) -> str:
    return_object = InputObject()

    def select(event=None):
        value = list_box.get(tk.ACTIVE)
        io_root.destroy()
        io_root.quit()
        return_object.value = value
    io_root = tk.Toplevel()
    io_root.bind('<Return>', select)
    io_root.title("Make a choice")
    label = tk.Label(io_root, text=caption)
    label.pack()
    list_box = tk.Listbox(io_root, selectmode=tk.SINGLE)
    io_root.data = [option for option in options]
    for option in options:
        list_box.insert(tk.END, option)
    list_box.pack(fill=tk.BOTH, expand=1)
    list_box.see(tk.END)
    button = tk.Button(io_root, text="Select", command=select)
    button.pack()
    list_box.focus_set()
    io_root.mainloop()
    return return_object.value


def prompt_text(caption) -> str:
    return_object = InputObject()

    def ok(event=None):
        value = entry_variable.get()
        root.destroy()
        root.quit()
        return_object.value = value

    root = tk.Toplevel()
    root.bind('<Return>', ok)
    root.title("Enter some text")
    label = tk.Label(root, text=caption)
    label.pack()
    entry_variable = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_variable)
    entry.pack()
    entry.focus_set()
    button = tk.Button(root, text="OK", command=ok)
    button.pack()
    root.mainloop()

    return return_object.value

