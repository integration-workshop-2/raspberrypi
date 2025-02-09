from infra.hardware.gy906.gy906 import GY906
from infra.hardware.max30102.max30102 import MAX30102
from typing import Dict


class GetReadingsFromVitalSignsSensorsUseCase:
    def __init__(self) -> None:
        self.__gy906 = GY906()
        self.__max30102 = MAX30102()

    def execute(self) -> Dict:
        temperature = self.__gy906.get_target_temperature()
        max30102_response = self.__max30102.get_bpm_and_oxygenation_percentage()

        if not max30102_response.bpm or not max30102_response.oxygenation_percentage:
            return {"success": False}

        return {
            "success": True,
            "data": {
                "temperature": temperature,
                "bpm": max30102_response.bpm,
                "oxygenation_percentage": max30102_response.oxygenation_percentage,
            },
        }
