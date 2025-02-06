from flask import Blueprint, jsonify
from data.use_cases.vital_signs_sensors.get_readings_from_vital_signs_sensors.use_case import (
    GetReadingsFromVitalSignsSensorsUseCase,
)

vital_signs_sensors_bp = Blueprint("vital_signs_sensors_bp", __name__)


@vital_signs_sensors_bp.route("/vital_signs_sensors", methods=["GET"])
def get_readings_from_vital_signs_sensors():
    use_case = GetReadingsFromVitalSignsSensorsUseCase()
    response = use_case.execute()
    return jsonify(response), 200
