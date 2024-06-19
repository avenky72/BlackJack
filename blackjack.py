import tkinter as tk
from tkinter import ttk
import random

def show_rules():
    # More efficient way to clear widgets
    for widget in root.winfo_children():
        widget.destroy()
    rules_label = tk.Label(root, text="Blackjack 2.0 Rules:\n\n1. The goal is to get as close to 21 without going over.\n2. Face cards are worth 10, and Aces are worth 1 or 11.\n3. There are also special cards that have special abilities like delete an opponents card or force to draw another card.\n4. Players are dealt two cards and can choose to 'hit' to take another card or 'stand' to keep their current hand.", wraplength=400)
    rules_label.pack(padx=10, pady=10)
    start_game_button = tk.Button(root, text="Start Game", font=('arial', 15, 'bold'), bg="magenta4", fg="red", command=start_game)
    start_game_button.pack(padx=10, pady=10)



def cards():
    # Showing the cards as value, suit instead of using images
    # Change to add the special cards after everything works
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(value, suit) for suit in suits for value in values]
    return deck


def save_name():
    global name
    name = name_entry.get()
    name_field.delete(0, tk.END)
    greeting = f"Hello {name}"
    name_field.insert(0, greeting)


def start_game():
    for widget in root.winfo_children():
        widget.destroy()
        
        
    global deck, player_hand, dealer_hand, player_frame, dealer_frame
    deck = cards()
    random.shuffle(deck)
    player_hand = []
    dealer_hand = []


    player_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())



    player_frame = tk.Frame(root, bg='green')
    player_frame.pack(side=tk.LEFT, padx=10, pady=10)
    tk.Label(player_frame, text=f"{name}'s Hand", font=('arial', 15, 'bold'), bg='green', fg='white').pack(padx=10, pady=10)    
    for card in player_hand:
        tk.Label(player_frame, text=f"{card[0]} of {card[1]}", font=('arial', 15, 'bold'), bg='white', fg='black').pack(padx=5, pady=5)
    print(current_points(player_hand))
    #player_points_label = tk.Label(player_frame, text=f"Points: {current_points(player_hand)}", font=('arial', 15, 'bold'), bg='green', fg='white')
    #player_points_label.pack(padx=5, pady=5)


    dealer_frame = tk.Frame(root, bg='green')
    dealer_frame.pack(side=tk.RIGHT, padx=10, pady=10)
    tk.Label(dealer_frame, text="Dealer's Hand", font=('arial', 15, 'bold'), bg='green', fg='white').pack(padx=10, pady=10)
    for card in dealer_hand:
        tk.Label(dealer_frame, text=f"{card[0]} of {card[1]}", font=('arial', 15, 'bold'), bg='white', fg='black').pack(padx=5, pady=5)



    control_frame = tk.Frame(root, bg='green')
    control_frame.pack(pady=10)
    hit_button = tk.Button(control_frame, text="Hit", font=('arial', 15, 'bold'), bg="magenta4", fg="red", command=hit)
    hit_button.pack(side=tk.LEFT, padx=10)
    stand_button = tk.Button(control_frame, text="Stand", font=('arial', 15, 'bold'), bg="magenta4", fg="red", command=stand)
    stand_button.pack(side=tk.LEFT, padx=10)





def hit():
    player_hand.append(deck.pop())
    tk.Label(player_frame, text=f"{player_hand[-1][0]} of {player_hand[-1][1]}", font=('arial', 15, 'bold'), bg='white', fg='black').pack(padx=5, pady=5)
    global points
    points = current_points(player_hand)
    print(points)
    if points > 21:
        end_game("Game Over, Your Hand is a Bust")
    if points == 21:
        end_game("You Win")
        
        
def end_game(message):
    for widget in root.winfo_children():
        widget.destroy()
    result_label = tk.Label(root, text=message, font=('arial', 20, 'bold'), bg='wheat3', fg='navy')
    result_label.pack(padx=20, pady=20)


def stand():
    global d_points
    d_points = current_points(dealer_hand)
    print("dealer: ", d_points)
    if d_points > current_points(player_hand):
        end_game("You Lose, Dealer Had ", d_points)
    else:
        while d_points <= current_points(player_hand):
        # While the dealer total is less than 18, auto hit
            dealer_hand.append(deck.pop())
            tk.Label(dealer_frame, text=f"{dealer_hand[-1][0]} of {dealer_hand[-1][1]}", font=('arial', 15, 'bold'), bg='white', fg='black').pack(padx=5, pady=5)
            d_points = current_points(dealer_hand)
            print("dealer: ", d_points)
            if d_points > 21:
                end_game("You Win, Dealer's Hand is a Bust")
            elif d_points > current_points(player_hand):
                end_game("You Lose, Dealer Had ", d_points)



def current_points(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
    points = sum(values[card[0]] for card in hand)
    return points




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
