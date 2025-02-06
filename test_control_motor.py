from data.use_cases.routine.control_motor.use_case import ControlMotorUseCase

use_case = ControlMotorUseCase(cylinder_number=1)
use_case.execute()

use_case = ControlMotorUseCase(cylinder_number=2)
use_case.execute()

use_case = ControlMotorUseCase(cylinder_number=3)
use_case.execute()
