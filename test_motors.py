from motor.motor import Motor
from time import sleep

motor_1 = Motor(1)
motor_2 = Motor(2)
motor_3 = Motor(3)

motor_1.execute_half_step()
sleep(2)

motor_2.execute_half_step()
sleep(2)

motor_3.execute_half_step()
sleep(2)
