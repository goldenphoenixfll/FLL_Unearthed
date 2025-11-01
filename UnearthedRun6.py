from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Setup everything
hub = PrimeHub()
llm = Motor(Port.B)
rlm = Motor(Port.F)
lsm = Motor(Port.A,Direction.COUNTERCLOCKWISE)
rsm = Motor(Port.E,Direction.CLOCKWISE)
#Silo = Motor(Port.F, [[12, 40], [12, 12]])
robot = DriveBase(left_motor=lsm,right_motor=rsm,wheel_diameter=62.4,axle_track=128.5)
robot.use_gyro(True)

#The Run
robot.settings(straight_speed=400, turn_rate=30)
robot.straight(150)
robot.turn(-40)
rlm.run_angle(speed=600,rotation_angle=-250)
robot.straight(767)
rlm.run_angle(speed=600,rotation_angle=250)
robot.straight(-80)
robot.settings(turn_rate=67)
robot.turn(-45)
robot.straight(239)
robot.turn(40)
robot.settings(straight_speed=700)
robot.straight(-260)
wait(200)
robot.straight(225)
robot.settings(straight_speed=400)
robot.turn(-45)
robot.straight(280)
robot.turn(-45)
rlm.run_angle(speed=600,rotation_angle=-467)
robot.straight(167)
llm.run_angle(200,500)
rlm.run_angle(speed=600,rotation_angle=250)
robot.straight(-167)