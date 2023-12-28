import pyautogui
import time
import keyboard
import pytesseract
import modules.opponent as Opponent
import modules.player as Player
import modules.utility as Utility

pytesseract.pytesseract.tesseract_cmd = 'E:/Programmi/Tesseract/tesseract.exe'

TARGET_GOLD = 800_000
TARGET_ELIXAR = 800_000
TARGET_DARKELIXAR = 8_000

TIME_SINCE_SKIP = 5

def main() -> None:
    print("Application started.\n")

    if input("Press D for debug mode, or press any other key to continue:") == "d":
        while True:
            # Check if the user wants to quit the application
            if keyboard.is_pressed('esc'):
                break

            print(f"{pyautogui.position()}, {Utility.sample_pixel(pyautogui.position()[0],pyautogui.position()[1])}" )
            time.sleep(0.5)
    else:
        Utility.wait(3) # Allow user to change desktop
        Player.army_ready()
        Opponent.search(TARGET_GOLD, TARGET_ELIXAR, TARGET_DARKELIXAR, TIME_SINCE_SKIP)


if __name__ == '__main__':
    main()
