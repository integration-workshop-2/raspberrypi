import adafruit_mlx90614
import board
import busio as io


class GY906:
    def __init__(self) -> None:
        self.__i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
        self.__mlx = adafruit_mlx90614.MLX90614(self.__i2c)

    def get_target_temperature(self) -> float:
        return round(self.__mlx.object_temperature, 2)

    def get_ambient_temperature(self) -> float:
        return round(self.__mlx.ambient_temperature, 2)
