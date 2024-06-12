import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Black Jack 2.0")
root.configure(background='wheat3')


def save_name():
    name = name_entry.get()
    name_field.delete(0, tk.END)
    greeting = f"Hello {name}"
    name_field.insert(0, greeting)
    # initialize the play_game() function here to clear the screen and start the game


name_label = tk.Label(root, fg="navy", text="Enter your name")
name_entry = tk.Entry(root, bg="MistyRose2")
name_button = tk.Button(root, font=('arial', 15, 'bold'), text="Enter",  bg="magenta4", fg="magenta4", command= save_name)
name_field = tk.Entry(root, bg="SeaGreen1")




name_label.pack(padx=5, pady=5, side=tk.LEFT)
name_entry.pack(padx=5, pady=5, side=tk.LEFT)
name_button.pack(padx=5, pady=5, side=tk.LEFT)
name_field.pack(padx=5, pady=5, side=tk.LEFT)


root.mainloop()