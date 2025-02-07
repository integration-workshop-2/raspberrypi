from flask import Blueprint, jsonify

from data.parameters.routine.control_motor.parameter import ControlMotorParameter
from data.use_cases.routine.control_motor.use_case import ControlMotorUseCase

control_motor_bp = Blueprint("control_motor_bp", __name__)


@control_motor_bp.route("/control_motor/<int:cylinder_number>", methods=["GET"])
def get_readings_from_vital_signs_sensors(cylinder_number: int):
    parameter = ControlMotorParameter(cylinder_number=cylinder_number)
    use_case = ControlMotorUseCase()
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200
