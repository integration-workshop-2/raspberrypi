import RPi.GPIO as GPIO
import time
from typing import List


class Motor:
    def __init__(self, cylinder_number: int) -> None:
        GPIO.setmode(GPIO.BCM)

        self.__control_pins = self.__get_control_pins_by_cylinder_number(
            cylinder_number=cylinder_number
        )

        self.__half_step_sequence = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
        ]

        for pin in self.__control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

    def get_control_pins(self) -> List[int]:
        return self.__control_pins

    def get_half_step_sequence(self) -> List[List[int]]:
        return self.__half_step_sequence

    def __get_control_pins_by_cylinder_number(self, cylinder_number: int) -> List[int]:
        control_pins_by_cylinder_number_dict = {
            1: [6, 13, 19, 26],
            2: [18, 23, 24, 25],
            3: [21, 20, 16, 12],
        }

        return control_pins_by_cylinder_number_dict.get(cylinder_number)

    def set_pin_state(self, pin: int, state: int) -> None:
        GPIO.output(channel=pin, value=state)

    def execute_half_step(self) -> None:
        for _ in range(512):
            for i in range(8):
                for j in range(4):
                    GPIO.output(self.__control_pins[j], self.__half_step_sequence[i][j])
                time.sleep(0.001)

    def __del__(self) -> None:
        GPIO.cleanup()
