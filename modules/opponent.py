from . import utility as Utility
import pyautogui
import keyboard

class search:
    def __init__(self, target_gold=800_000, target_elixar=800_000, target_darkelixar=8_000, time_since_skip=5):
        self.target_gold = target_gold
        self.target_elixar = target_elixar
        self.target_darkelixar = target_darkelixar
        self.target_mean_resources = (target_gold + target_elixar + target_darkelixar*100) / 3

        self.time_since_skip = time_since_skip

        self.find_good_opponent() # Find a good opponent

    def enough_resources(self) -> bool:
        name= Utility.get_text_at_position(80, 20, 200, 30) or "-"
        print(f"{name.capitalize()}:")

        gold = Utility.get_number_at_position(75, 120, 150, 40)
        gold = gold if gold < 2_000_000 else -2 # If the opponent has more than 2M gold, the reading is wrong
        print(f"Gold: {gold}")

        elixar = Utility.get_number_at_position(75, 170, 150, 40)
        elixar = elixar if elixar < 2_000_000 else -2 # If the opponent has more than 2M elixar, the reading is wrong
        print(f"Elixar: {elixar}")

        darkelixar = Utility.get_number_at_position(75, 220, 100, 40)
        darkelixar = darkelixar if darkelixar < 20_000 else -2 # If the opponent has more than 20k dark elixar, the reading is wrong
        print(f"Dark Elixar {darkelixar}")

        mean_resources = (gold + elixar + darkelixar*100) / 3

        if (gold > self.target_gold and elixar > self.target_elixar and darkelixar > self.target_darkelixar) or mean_resources > self.target_mean_resources:
            return True
        else:
            return False
        
    def find_good_opponent(self) -> None:
        pyautogui.click(101, 970) # Click the attack button
        pyautogui.click(1350, 625) # Click the search opponent button
        Utility.wait() # Wait for first oponent to be found

        while True:
            # Check if the user wants to quit the application
            if keyboard.is_pressed('esc'):
                print("Application closed. With esc key")
                break

            # Check if the opponent is good
            if self.enough_resources():
                print("Found good opponent!")
                break
            else: 
                print("Opponent not good enough, searching for new opponent...\n")
                pyautogui.click(1780, 650) # Click the search opponent button
                Utility.wait() # Wait for opponent to be found

class attack:
    def __init__(self, troops: int, potions: int, siege: True, heroes: list) -> None:
        self.potions = potions
        self.troops = troops
        self.heroes = heroes # (king, queen, warden, royal champion)
        self.siege = siege

        self.attack_opponent() # Attack the opponent

    def attack_opponent(self) -> None:
        # Todo: Finish this function

        if self.siege:
            pyautogui.press("z") # Select the siege machine
            pyautogui.click(1780, 650) # deploy the siege machine
        
        if self.heroes[0]:
            pyautogui.press("q") # Select the king
            pyautogui.click(1780, 650) # deploy the king

        if self.heroes[1]:
            pyautogui.press("w") # Select the queen
            pyautogui.click(1780, 650) # deploy the queen
            pyautogui.press("w") # deploy the queen ability

        if self.heroes[3]:
            pyautogui.press("r") # Select the royal champion
            pyautogui.click(1780, 650) # deploy the royal champion

        pyautogui.press("1") # Select the troops
        pyautogui.moveTo(1780, 650) # Go to the top of the deployment area
        pyautogui.dragTo(1780, 650, duration=3) # Deploy the troops

        if self.heroes[2]:
            pyautogui.press("e") # Select the warden
            pyautogui.click(1780, 650) # deploy the warden

        pyautogui.press("a") # Select fury potions
        Utility.wait(20)
        pyautogui.click(1780, 650) if self.potions >= 1 else None # Deploy first potion
        pyautogui.click(1780, 650) if self.potions >= 2 else None # Deploy second potion
        Utility.wait(10)

        pyautogui.click(1780, 650) if self.potions >= 3 else None # Deploy third potion
        pyautogui.click(1780, 650) if self.potions >= 4 else None # Deploy fourth potion
        pyautogui.click(1780, 650) if self.potions >= 5 else None # Deploy fifth potion

        Utility.wait(2*60) # Wait for the attack to finish
        pyautogui.click(1780, 650) # Click the return home button


        
