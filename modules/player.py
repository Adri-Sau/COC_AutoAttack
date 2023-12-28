from . import utility as Utility
import pyautogui
import keyboard

class army:
    def open_army(self) -> None:
        pyautogui.click(60, 833)

    def close_army(self) -> None:
        pyautogui.click(1619, 137)

    def is_ready(self) -> True:
        time_remaining = 0
        while True:
            # Check if the user wants to quit the application 
            if keyboard.is_pressed('esc'):
                print("Application closed. With esc key")
                return False

            if time_remaining == 0:

                self.open_army()
                if Utility.sample_pixel(291, 233) == (142, 190, 45):
                    break

                time_remaining_string = Utility.get_text_at_position(990, 215, 160, 25).lower()
                time_remaining = Utility.get_time_seconds(time_remaining_string)

                self.close_army()
                print(f"Army not ready, {time_remaining} left")
                Utility.wait(1)
                time_remaining -= 1

        return True