"""
button_input.py

Handles the recommendation button input.

This class can work in two modes:
1. PocketBeagle GPIO mode, if Adafruit_BBIO.GPIO is installed.
2. Mock mode, where pressing Enter simulates the hardware button.
"""

import time

try:
    import Adafruit_BBIO.GPIO as GPIO
    GPIO_AVAILABLE = True
except ImportError:
    GPIO_AVAILABLE = False


class ButtonInput:
    def __init__(self, pin="P2_08", active_low=True, sleep_time=0.05):
        self.pin = pin
        self.active_low = active_low
        self.sleep_time = sleep_time
        self.mock_mode = not GPIO_AVAILABLE

    def setup(self):
        if self.mock_mode:
            return

        GPIO.setup(self.pin, GPIO.IN)

    def wait_for_press(self):
        if self.mock_mode:
            input("\nPress Enter to simulate the PocketBeagle button...")
            return True

        pressed_value = GPIO.LOW if self.active_low else GPIO.HIGH

        print("\nWaiting for PocketBeagle button press...")

        while True:
            if GPIO.input(self.pin) == pressed_value:
                time.sleep(0.2)
                return True

            time.sleep(self.sleep_time)

    def cleanup(self):
        if not self.mock_mode:
            GPIO.cleanup()
