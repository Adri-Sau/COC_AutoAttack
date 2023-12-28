from . import utility as Utility
import pyautogui
import keyboard
import time

class search:
    def __init__(self, target_gold=800_000, target_elixar=800_000, target_darkelixar=8_000, time_since_skip=5):
        self.target_gold = target_gold
        self.target_elixar = target_elixar
        self.target_darkelixar = target_darkelixar
        self.target_mean_resources = (target_gold + target_elixar + target_darkelixar*100) / 3

        self.time_since_skip = time_since_skip

        self.find_good_opponent() # Find a good opponent

    def enough_resources(self) -> bool:
        name= Utility.get_text_at_position(80, 20, 200, 30) or "NoName"
        print(f"Opponent name: {name}")

        gold = Utility.get_number_at_position(75, 120, 150, 40, name)
        gold = gold if gold < 2_000_000 else -2 # If the opponent has more than 2M gold, the reading is wrong
        print(f"Opponent gold: {gold}")

        elixar = Utility.get_number_at_position(75, 170, 150, 40, name)
        elixar = elixar if elixar < 2_000_000 else -2 # If the opponent has more than 2M elixar, the reading is wrong
        print(f"Opponent elixar: {elixar}")

        darkelixar = Utility.get_number_at_position(75, 220, 100, 40, name)
        darkelixar = darkelixar if darkelixar < 20_000 else -2 # If the opponent has more than 20k dark elixar, the reading is wrong
        print(f"Opponent dark elixar: {darkelixar}")

        mean_resources = (gold + elixar + darkelixar*100) / 3

        if (gold > self.target_gold and elixar > self.target_elixar and darkelixar > self.target_darkelixar) or mean_resources > self.target_mean_resources:
            return True
        else:
            return False
        
    def find_good_opponent(self) -> None:
        time.sleep(3) # Allow user to change desktop
        pyautogui.click(101, 970) # Click the attack button
        pyautogui.click(1350, 625) # Click the search opponent button
        Utility.wait() # Wait for first oponent to be found

        while True:
            # Check if the user wants to quit the application
            if keyboard.is_pressed('esc'):
                break

            # Check if the opponent is good
            if self.enough_resources():
                print("Found good opponent!")
                break
            else: 
                print("Opponent not good enough, searching for new opponent...\n")
                pyautogui.click(1780, 650) # Click the search opponent button
                Utility.wait() # Wait for opponent to be found
