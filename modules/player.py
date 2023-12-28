from . import utility as Utility
import pyautogui

class army_ready:
    def __init__(self):
        self.open_army()
        self.check_if_ready()
        self.close_army()

    def open_army(self) -> None:
        pyautogui.click(60, 833)

    def close_army(self) -> None:
        pyautogui.click(1619, 137)

    def check_if_ready(self) -> None:
        while True:
            if Utility.sample_pixel(291, 233) == (142, 190, 45):
                break
            else:
                Utility.wait(1)