import pyautogui
import time
import keyboard
import pytesseract
import modules.opponent as Opponent
import modules.player as Player
import modules.utility as Utility

TESSERACT_LOCATION = "E:/Programmi/Tesseract/tesseract.exe"

TARGET_GOLD = 700_000
TARGET_ELIXIR = 700_000
TARGET_DARK_ELIXIR = 7_000

TIME_SINCE_SKIP = 5

pytesseract.pytesseract.tesseract_cmd = TESSERACT_LOCATION

def debug_mode() -> None:
    """
    Enters the debug mode of the application.
    Prints the current mouse position and the color of the pixel at that position.
    Press 'esc' to exit the debug mode.
    """
    print("Application started in debug mode.\n")
    while True:
        # Check if the user wants to quit the application
        if keyboard.is_pressed('esc'):
            break

        if keyboard.is_pressed('p'):
            print(f"{pyautogui.position()[0], pyautogui.position()[1]} : {Utility.sample_pixel(pyautogui.position()[0],pyautogui.position()[1])}")
            Utility.wait(1)


def auto_attack() -> None:
    """
    Function to automate the attack process in Clash of Clans.

    This function waits for the army to be ready, searches for opponents, attacks,
    trains the same army, and repeats the process until the user quits the application.

    Returns:
        None
    """
    Utility.wait(3) # Allow user to change desktop
    army_time_remaining = Player.army().is_ready()
    while True:
        # Check if the user wants to quit the application
        if keyboard.is_pressed('esc'):
            print("Application closed. With esc key")
            break

        # If the army is ready, attack and train the same army
        if army_time_remaining != None and army_time_remaining <= 0:
            Opponent.search(TARGET_GOLD, TARGET_ELIXIR, TARGET_DARK_ELIXIR, TIME_SINCE_SKIP)
            Opponent.attack(10, 5, True, [True, True, True, True])
            Player.army().train_same()
            army_time_remaining = Player.army().is_ready()

        if army_time_remaining != None and army_time_remaining % 60 == 0:
            pyautogui.click(60, 833)
            Utility.wait(1)
            pyautogui.click(1619, 137)
            Utility.wait(1)
            army_time_remaining -= 2

        time.sleep(1)
        army_time_remaining = army_time_remaining - 1 if army_time_remaining != None else Player.army().is_ready()
        # print(f"time remaining: {Utility.get_time_string(army_time_remaining)}")

def main() -> None:
    """
    Entry point of the application.
    """
    print("Application started.\n")

    # Check if the user wants to enter debug mode
    if input("Press D for debug mode, or press any other key to continue:\n") == "d":
        debug_mode()
    else:
        auto_attack()

if __name__ == '__main__':
    main()
