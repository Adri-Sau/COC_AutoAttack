from . import utility as Utility
import pyautogui
import keyboard

# Constants for the troops deployement bar 
BAR_POSITION = (0, 747)

CARD_SIZE = (111, 147)
CARD_SPACE_SIZE = (9, 22)
CARDS_OFFSET = (155, 10)
CARDS_PACKS_SPACE = 23

class search:
    def __init__(self, target_gold=700_000, target_elixar=700_000, target_darkelixar=7_000, time_since_skip=5):
        self.target_gold = target_gold
        self.target_elixar = target_elixar
        self.target_darkelixar = target_darkelixar
        self.target_mean_resources = (target_gold + target_elixar + target_darkelixar*100) / 3

        self.time_since_skip = time_since_skip

        self.good_opponent() # Find a good opponent

    def enough_resources(self) -> bool:
        name = Utility.get_text_at_position(80, 20, 200, 30)

        gold = Utility.get_number_at_position(75, 120, 150, 40)
        gold = gold if gold < 1_500_000 else -2 # If the opponent has more than 2M gold, the reading is wrong

        elixar = Utility.get_number_at_position(75, 170, 150, 40)
        elixar = elixar if elixar < 1_500_000 else -2 # If the opponent has more than 2M elixar, the reading is wrong

        darkelixar = Utility.get_number_at_position(75, 220, 100, 40)
        darkelixar = darkelixar if darkelixar < 15_000 else -2 # If the opponent has more than 20k dark elixar, the reading is wrong

        mean_resources = (gold + elixar + darkelixar*100) / 3

        if (gold > self.target_gold and elixar > self.target_elixar and darkelixar > self.target_darkelixar) or mean_resources > self.target_mean_resources:
            print("Found good opponent.\n")
            print(f"{name.capitalize()}:")
            print(f"Gold: {gold}")
            print(f"Elixar: {elixar}")
            print(f"Dark Elixar {darkelixar}\n")
            return True
        else:
            return False
        
    def good_opponent(self) -> None:
        pyautogui.click(101, 970) # Click the attack button
        pyautogui.click(1350, 625) # Click the search opponent button
        Utility.wait() # Wait for first oponent to be found

        while True:
            # Check if the user wants to quit the application
            if keyboard.is_pressed('space'):
                print("Chose player manually.")
                break
            # Check if the opponent is good
            if self.enough_resources():
                break
            else: 
                pyautogui.click(1780, 650) # Click the search opponent button
                Utility.wait() # Wait for opponent to be found


class attack:
    def __init__(self, troops: int, potions: int, siege: True, heroes: list) -> None:
        self.potions = potions
        self.troops = troops
        self.heroes = heroes # (king, queen, warden, royal champion)
        self.siege = siege

        self.start() # Attack the opponent

    def start(self) -> None:

        # Siege machine select and deploy 
        if self.siege:
            self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*1.5)+(CARD_SPACE_SIZE[0])*0+(CARDS_PACKS_SPACE)*1,
                            BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*0.5)+(CARD_SPACE_SIZE[1])*0)
            self.click_at(324, 424)
        
        # King select and deploy
        if self.heroes[0]:
            self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*2.5)+(CARD_SPACE_SIZE[0])*0+(CARDS_PACKS_SPACE)*2,
                            BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*0.5)+(CARD_SPACE_SIZE[1])*0)
            self.click_at(193, 624)

        # Queen select, deploy and activate ability
        if self.heroes[1]:
            self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*2.5)+(CARD_SPACE_SIZE[0])*0+(CARDS_PACKS_SPACE)*2,
                            BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*1.5)+(CARD_SPACE_SIZE[1])*1)
            self.click_at(296, 439)
            Utility.wait(2)
            self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*2.5)+(CARD_SPACE_SIZE[0])*0+(CARDS_PACKS_SPACE)*2,
                            BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*1.5)+(CARD_SPACE_SIZE[1])*1)

        # Royal champion select and deploy
        if self.heroes[3]:
            self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*3.5)+(CARD_SPACE_SIZE[0])*1+(CARDS_PACKS_SPACE)*2,
                            BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*1.5)+(CARD_SPACE_SIZE[1])*1)
            self.click_at(174, 625)

        # Troops select and deploy
        if self.troops >= 1:
            self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*0.5)+(CARD_SPACE_SIZE[0])*0+(CARDS_PACKS_SPACE)*0,
                            BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*0.5)+(CARD_SPACE_SIZE[1])*0)
            self.drag_deploy(242, 449, 229, 551, 0.2*self.troops)

        # Warden select and deploy
        if self.heroes[2]:
            self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*3.5)+(CARD_SPACE_SIZE[0])*1+(CARDS_PACKS_SPACE)*2,
                            BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*0.5)+(CARD_SPACE_SIZE[1])*0)
            self.click_at(190, 487)

        # Spells select and deploy
        Utility.wait(10)
        if self.potions >= 1:
            self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*4.5)+(CARD_SPACE_SIZE[0])*1+(CARDS_PACKS_SPACE)*3,
                            BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*0.5)+(CARD_SPACE_SIZE[1])*0)
            self.click_at(598, 349)
        self.click_at(600, 605) if self.potions >= 2 else None

        # Warden ability
        Utility.wait(5)
        self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*3.5)+(CARD_SPACE_SIZE[0])*1+(CARDS_PACKS_SPACE)*2,
                        BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*0.5)+(CARD_SPACE_SIZE[1])*0) if self.heroes[2] else None

        # Spells select and deploy
        Utility.wait(5)
        if self.potions >= 3:
            self.click_at(  BAR_POSITION[0]+CARDS_OFFSET[0]+int((CARD_SIZE[0])*4.5)+(CARD_SPACE_SIZE[0])*1+(CARDS_PACKS_SPACE)*3,
                            BAR_POSITION[1]+CARDS_OFFSET[1]+int((CARD_SIZE[1])*0.5)+(CARD_SPACE_SIZE[1])*0)
            self.click_at(819, 488)
        self.click_at(813, 243) if self.potions >= 4 else None
        self.click_at(826, 697) if self.potions >= 5 else None

        # Finish attack
        Utility.wait(2*60)
        self.get_loot_taken()
        pyautogui.click(957, 925)
        Utility.wait(3)

        # Check for star bonus
        self.check_star_bonus()

    def check_star_bonus(self) -> None:
        if Utility.sample_pixel(956, 778) == (255, 255, 255):
            pyautogui.click(956, 778)
            Utility.wait(1)
        
    def click_at(self, x: int, y: int) -> None:
        Utility.wait(1)
        pyautogui.click(x, y)
        
    def drag_deploy(self, x1: int, y1: int, x2: int, y2: int, duration) -> None:
        Utility.wait(1)
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, duration)      

    def get_loot_taken(self) -> None:
        print("Loot taken:")
        gold = Utility.get_number_at_position(750, 450, 230, 50)
        print(f"Gold: {gold}")
        elixar = Utility.get_number_at_position(750, 520, 230, 50)
        print(f"Elixar: {elixar}")
        darkelixar = Utility.get_number_at_position(810, 580, 170, 50)
        print(f"Dark Elixar: {darkelixar}")



        
