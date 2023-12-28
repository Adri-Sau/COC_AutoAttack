import pyautogui
import pytesseract
import re
import random
import time

def wait(seconds: int=5) -> None:
    if seconds <= 0:
        return
    time.sleep(seconds + random.random()*2 - 1)


def get_text_at_position(x: int, y: int, width: int, height: int) -> str:

    image = pyautogui.screenshot(region=(x, y, width, height))

    raw_text = pytesseract.image_to_string(image, config="--psm 6")
    list_of_strings = re.findall('[A-Za-z0-9]', raw_text)
    text = "".join(list_of_strings)

    return text


def get_number_at_position(x: int, y: int, width: int, height: int) -> int:

    image = pyautogui.screenshot(region=(x, y, width, height))

    raw_text = pytesseract.image_to_string(image, config="--psm 6").replace("s", "5").replace("S", "5")
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

def get_time_seconds(time_string: str) -> int:

    time_string = time_string.lower().replace("s", "").replace("m", ":").replace("h", ":").replace("d", ":")
    time_list = time_string.split(":")
    time_list = [int("".join(re.findall(r'\d', i))) if "".join(re.findall(r'\d', i)) != '' else 0 for i in time_list]
    time_list.reverse()

    seconds = 0
    for i in range(len(time_list)):
        seconds += time_list[i] * 60**i

    return seconds

def get_time_string(seconds: int) -> str:
    days = seconds // 86400
    seconds -= days * 86400

    hours = seconds // 3600
    seconds -= hours * 3600

    minutes = seconds // 60
    seconds -= minutes * 60

    time_string = f"{days}d {hours}h {minutes}m {seconds}s"

    return time_string
