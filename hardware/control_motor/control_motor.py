from motor.motor import Motor
from tcrt5000.tcrt5000 import TCRT5000
from time import sleep
from typing import List


class ControlMotor:
    def __init__(self, cylinder_number: int) -> None:
        self.__motor = Motor(cylinder_number=cylinder_number)
        self.__tcrt5000a = TCRT5000(sensor_pin=5)
        self.__tcrt5000b = TCRT5000(sensor_pin=17)

    def execute_controlled_movement(self) -> None:
        for _ in range(512):
            if self.__tcrt5000a.detected or self.__tcrt5000b.detected:
                return

            for i in range(8):
                for j in range(4):
                    self.__motor.set_pin_state(
                        pin=self.__motor.get_control_pins()[j],
                        state=self.__motor.get_half_step_sequence()[i][j],
                    )
                sleep(0.001)
