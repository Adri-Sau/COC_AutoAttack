import pyautogui
import pytesseract
import re
import random
import time

def wait(seconds: int=5) -> None:
    time.sleep(seconds + random.random()*2 - 1)


def get_text_at_position(x: int, y: int, width: int, height: int) -> str:

    image = pyautogui.screenshot(region=(x, y, width, height))

    raw_text = pytesseract.image_to_string(image, config="--psm 6")
    list_of_strings = re.findall('[A-Za-z0-9]', raw_text)
    text = "".join(list_of_strings)

    return text


def get_number_at_position(x: int, y: int, width: int, height: int) -> int:

    image = pyautogui.screenshot(region=(x, y, width, height))

    raw_text = pytesseract.image_to_string(image, config="--psm 6")
    raw_text = raw_text.replace("\n", "")
    list_of_strings = re.findall(r'\d', raw_text)
    text = "".join(list_of_strings)

    try:
        return int(text)
    except ValueError:
        print(f"{raw_text} -> {text} doen't contain numbers")
        return -1
    
def sample_pixel(x: int, y: int) -> tuple:
    image = pyautogui.screenshot(region=(x, y, 1, 1))
    return image.getpixel((0, 0))