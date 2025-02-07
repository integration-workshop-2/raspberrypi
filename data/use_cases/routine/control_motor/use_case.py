from data.parameters.routine.control_motor.parameter import ControlMotorParameter
from infra.hardware.motor.motor import Motor
from infra.hardware.tcrt5000.tcrt5000 import TCRT5000
from time import sleep


class ControlMotorUseCase:
    def __init__(self) -> None:
        self.__tcrt5000a = TCRT5000(sensor_pin=5)
        self.__tcrt5000b = TCRT5000(sensor_pin=17)

    def execute(self, parameter: ControlMotorParameter) -> None:
        self.__motor = Motor(cylinder_number=parameter.cylinder_number)

        stop = False

        while not stop:
            for _ in range(512):
                for i in range(8):
                    for j in range(4):
                        self.__motor.set_pin_state(
                            pin=self.__motor.get_control_pins()[j],
                            state=self.__motor.get_half_step_sequence()[i][j],
                        )
                        if self.__tcrt5000a.detected or self.__tcrt5000b.detected:
                            stop = True
                    sleep(0.001)
