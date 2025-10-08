from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup everything
hub = PrimeHub()
llm = Motor(Port.B)
rlm = Motor(Port.F)
lsm = Motor(Port.A,Direction.COUNTERCLOCKWISE)
rsm = Motor(Port.E,Direction.CLOCKWISE)
robot = DriveBase(left_motor=lsm,right_motor=rsm,wheel_diameter=62.4,axle_track=128.5)
robot.use_gyro(True)

#The Run
robot.settings(straight_speed=600)
robot.straight(300)
robot.turn(180)
robot.straight(-640)
robot.turn(-90)
robot.settings(straight_speed=100)
robot.straight(130)
rlm.run_angle(speed=100,rotation_angle=260)
llm.run_angle(speed=100,rotation_angle=-5)
robot.use_gyro(True)
robot.straight(-200)