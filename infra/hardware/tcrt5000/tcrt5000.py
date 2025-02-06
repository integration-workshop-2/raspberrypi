import RPi.GPIO as GPIO


class TCRT5000:
    def __init__(self, sensor_pin: int = 17) -> None:
        self.__sensor_pin = sensor_pin

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(
            sensor_pin, GPIO.BOTH, callback=self.__interrupt_handler, bouncetime=300
        )

        self.detected = False

    def __interrupt_handler(self, channel: int) -> None:
        self.detected = True

    def get_sensor_reading(self) -> int:
        """If the reading is 1, it detected something"""

        return GPIO.input(self.__sensor_pin)

    def __del__(self) -> None:
        GPIO.cleanup()
