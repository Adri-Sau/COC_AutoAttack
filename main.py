import pyautogui
import time
import keyboard
import pytesseract
import scripts.opponent as Opponent

pytesseract.pytesseract.tesseract_cmd = 'E:/Programmi/Tesseract/tesseract.exe'

TARGET_GOLD = 700_000
TARGET_ELIXAR = 700_000
TARGET_DARKELIXAR = 7_000

TIME_SINCE_SKIP = 5

def main() -> None:
    print("Application started.\n")

    key = input("Press D for debug mode, or press any other key to continue:")

    if key == "d":
        while True:
            # Check if the user wants to quit the application
            if keyboard.is_pressed('esc'):
                break

            print(f"Mouse position: {pyautogui.position()}" )
            time.sleep(0.5)
    else:
        Opponent.search(TARGET_GOLD, TARGET_ELIXAR, TARGET_DARKELIXAR, TIME_SINCE_SKIP)


if __name__ == '__main__':
    main()