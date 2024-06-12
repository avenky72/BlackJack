import tkinter as tk
from tkinter import ttk

def show_rules():
    # More efficient way to clear widgets
    for widget in root.winfo_children():
        widget.destroy()
    rules_label = tk.Label(root, text="Blackjack 2.0 Rules:\n\n1. The goal is to get as close to 21 without going over.\n2. Face cards are worth 10, and Aces are worth 1 or 11.\n3. There are also special cards that have special abilities like delete an opponents card or force to draw another card.\n4. Players are dealt two cards and can choose to 'hit' to take another card or 'stand' to keep their current hand.", wraplength=400)
    rules_label.pack(padx=10, pady=10)
    start_game_button = tk.Button(root, text="Start Game", font=('arial', 15, 'bold'), bg="magenta4", fg="red", command=start_game)
    start_game_button.pack(padx=10, pady=10)


def start_game():
    for widget in root.winfo_children():
        widget.destroy()
    # The actual game here
    game_label = tk.Label(root, text="Blackjack Game Screen")
    game_label.pack(padx=10, pady=10)


def save_name():
    name = name_entry.get()
    name_field.delete(0, tk.END)
    greeting = f"Hello {name}"
    name_field.insert(0, greeting)



root = tk.Tk()
root.title("Black Jack 2.0")
root.configure(background='wheat3')



name_label = tk.Label(root, fg="navy", text="Enter your name")
name_entry = tk.Entry(root, bg="MistyRose2")
name_button = tk.Button(root, font=('arial', 15, 'bold'), text="Enter", bg="magenta4", fg="magenta4", command=save_name)
name_field = tk.Entry(root, bg="SeaGreen1")
start_button = tk.Button(root, font=('arial', 15, 'bold'), text="Start", bg="magenta4", fg="red", command=show_rules)



name_label.pack(padx=5, pady=5)
name_entry.pack(padx=5, pady=5)
name_button.pack(padx=5, pady=5)
name_field.pack(padx=5, pady=5)
start_button.pack(padx=5, pady=5)




root.mainloop()
