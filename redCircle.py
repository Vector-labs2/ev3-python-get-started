# please use X: 707, Y: 123, Angle: 90, then click "Move"
# configure robot - load redCircle_robot.json

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor(INPUT_4)
color = ColorSensor(INPUT_2)

tank_drive.on(50, 50)
sleep(.2)
tank_drive.on(10, -10)
gyro.wait_until_angle_changed_by(65)
tank_drive.on(0, 0)

tank_drive.on(50,50)
sleep(1.3)

tank_drive.on(-50,-50)
sleep(2.35)

