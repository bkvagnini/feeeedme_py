## Program Name: meal_idea.py
## Author: Brian K. Vagnini
## Started 10/18/18 Revised 1/13/19
##
## Description:
## This program helps me to select from three to five tuples (phase 1) (five JSON files - phase 2), each
## containing a component of a full meal.
## This is to assist me when I get stuck for meal ideas.
## Phase 2 - replace the tuples with standard txt files that the user edits, with one entry per line- done 1/13/19

import random
from tkinter import Tk, Label, Button, W #(used with .grid) #LEFT, #RIGHT(used with .pack)
# The tkinter allows me to run this as a GUI
# At this time, the output is still going to the Python Console window- still pretty cool though
# Parts of this came from https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title ("Feeeedme")

        self.label = Label(master, text ="   This is Feeeedme...an app to suggest meal ideas to me   ")
        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = Button(master, text="Click to suggest a meal...",command=self.greet)
        self.greet_button.grid(row=1)

        self.close_button = Button(master, text = "Quit", command=master.quit)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        main = open ("main_dish.txt", 'r').read()
        main_split= main.split('\n')
        starch = open ("starch.txt", 'r').read()
        starch_split= starch.split('\n')
        vegetable = open ("vegetable.txt", 'r').read()
        vegetable_split= vegetable.split('\n')
        main_dish = random.choice(main_split)
        starch_side = random.choice(starch_split)
        veggie_side = random.choice(vegetable_split)
        print ("\n\n\tHow about {} with {} and {}\n\n".format(main_dish, starch_side,veggie_side))


root = Tk()
my_gui = MyFirstGUI(root) #must match the class name
root.mainloop()




           




