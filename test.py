import tkinter as tk
from tkinter import ttk
from random import randrange


def get_from_entry():
    element = entry.get()
    print(element)
    lable['text'] = element



def lotto():
    global NUMBER
    NUMBER = randrange(1, 50)
    print(NUMBER)


root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
lable = ttk.Label(frm, text="LOTTO")
lable.grid(column=0, row=0, padx=10, pady=10)

button_1 = ttk.Button(frm, text="Kliknij mnie", command=get_from_entry)
button_1.grid(column=0, row=1,  padx=10, pady=10)


button_2 = ttk.Button(frm, text="Losowanie", command=lotto)
button_2.grid(column=1, row=2,  padx=10, pady=10)

entry = ttk.Entry(frm, text="wpisz coś")
entry.grid(column=0, row=2,  padx=10, pady=10)

quit_button = ttk.Button(frm, text="Quit", command=root.destroy)
quit_button.grid(column=0, row=6, padx=10, pady=10)


root.mainloop()
