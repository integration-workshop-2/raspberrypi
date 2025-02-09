from infra.hardware.gy906.gy906 import GY906
from infra.hardware.max30102.heartrate_monitor import HeartRateMonitor
from typing import Dict


class GetReadingsFromVitalSignsSensorsUseCase:
    def __init__(self) -> None:
        self.__gy906 = GY906()
        self.__heart_rate_monitor = HeartRateMonitor()

    def execute(self) -> Dict:
        temperature = self.__gy906.get_target_temperature()
        max30102_response = self.__heart_rate_monitor.get_readings()

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
