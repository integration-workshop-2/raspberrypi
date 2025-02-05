from control_motor.control_motor import ControlMotor

control_motor = ControlMotor(1)

while 1:
	control_motor.execute_controlled_movement()
