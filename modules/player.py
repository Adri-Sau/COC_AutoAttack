from . import utility as Utility
import pyautogui

class army:
    def open(self) -> None:
        """
        Opens the player.

        This method clicks on a specific location on the screen, opening the player window and waits for 1 second.
        """
        pyautogui.click(60, 833)
        Utility.wait(1)

    def close(self) -> None:
        """
        Closes the player window.

        This method clicks on the specified coordinates to close the player window and waits for 1 second.
        """
        pyautogui.click(1619, 137)
        Utility.wait(1)

    def is_ready(self) -> int | None:
            """
            Checks if the player is ready to perform an action.

            Returns:
                int | None: The remaining time in seconds if the player is not ready,
                            None if the player is ready or there has been a problem.
            """
            self.open()
            if Utility.sample_pixel(291, 233)[1] >= 180:
                self.close()
                return 0

            time_remaining_string = Utility.get_text_at_position(1020, 215, 100, 22).lower()
            time_remaining = Utility.get_time_seconds(time_remaining_string)
            print(f"time_remaining_string: {time_remaining_string}")
            print(f"time_remaining: {time_remaining}")

            self.close()
            return time_remaining if time_remaining >= 0 else None

    def train_same(self) -> None:
        """
        Retrains the same army.
        """
        self.open()
        pyautogui.click(1430, 150)
        Utility.wait(1)
        pyautogui.click(1545, 315)
        Utility.wait(1)
        self.close()
        print("Army trained\n")
