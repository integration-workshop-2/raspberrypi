from data.use_cases.vital_signs_sensors.get_readings_from_vital_signs_sensors.use_case import (
    GetReadingsFromVitalSignsSensorsUseCase,
)

use_case = GetReadingsFromVitalSignsSensorsUseCase()

while True:
    print(use_case.execute())
