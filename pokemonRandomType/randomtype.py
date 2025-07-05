import tkinter as tk
from tkinter import *
import random 
import json
from datetime import datetime
import os

SAVE_FILE = "last_pick.json"
POKEMON_TYPES = [
    "Fire", "Water", "Grass", "Electric", "Ice", "Fighting",
    "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock",
    "Ghost", "Dragon", "Dark", "Steel", "Fairy", "Normal"
]
result_label = None

def load_last_pick():
    if not os.path.exists(SAVE_FILE):
        return None, None
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)
        return data.get("date"), data.get("type")

def save_pick(pick):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(SAVE_FILE, "w") as f:
        json.dump({"date": today, "type": pick}, f)

def pickType():
    today = datetime.now().strftime("%Y-%m-%d")
    last_date, last_pick = load_last_pick()

    if last_date == today:
        result_label.config(text=f"Today's type is: {last_pick}")
    else:
        new_pick = random.choice(POKEMON_TYPES)
        save_pick(new_pick)
        result_label.config(text=f"Today's type is: {new_pick}")
root = tk.Tk()
root.title("PokeRogue Challenge Type Randomizer for Addicts")
root.geometry("300x200")

label = tk.Label(root, text="Pick today's Pokémon type", font=("Arial", 14))
label.pack(pady=20,fill="x", expand=True)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10,fill="x", expand=True)

button = tk.Button(root, text="Pick Type",width=25, command=pickType)
button.pack(pady=10,fill="x", expand=True)

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)

root.mainloop()