from . import utility as Utility
import pyautogui

class army:
    def open(self) -> None:
        pyautogui.click(60, 833)
        Utility.wait(1)

    def close(self) -> None:
        pyautogui.click(1619, 137)
        Utility.wait(1)

    def is_ready(self) -> int | None:
        self.open()
        if Utility.sample_pixel(291, 233)[1] >= 180:
            self.close()
            return 0

        time_remaining_string = Utility.get_text_at_position(1020, 215, 100, 22).lower()
        time_remaining = Utility.get_time_seconds(time_remaining_string)
        print(f"time_remaining_string: {time_remaining_string}")
        print(f"time_remaining: {time_remaining}")

        self.close()
        # print(f"Army not ready, {Utility.get_time_string(time_remaining)} left")
        return time_remaining if time_remaining >= 0 else None

    def train_same(self) -> None:
        self.open()
        pyautogui.click(1430, 150)
        Utility.wait(1)
        pyautogui.click(1545, 315)
        Utility.wait(1)
        self.close()
        print("Army trained\n")
