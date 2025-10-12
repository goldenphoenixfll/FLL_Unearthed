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
robot = DriveBase(left_motor=lsm,right_motor=rsm,wheel_diameter=62.4,axle_track=128.5)
robot.use_gyro(True)

#The Run
robot.settings(straight_speed=500)
#rlm.run_angle(speed=1500,rotation_angle=300)
robot.straight(980)
robot.turn(90)
robot.straight(40)
robot.turn(-15)
llm.run_angle(speed=1500,rotation_angle=1000)
robot.turn(15)
robot.settings(straight_speed=300)
robot.straight(-150)
robot.turn(45)
robot.straight(-320)
robot.straight(200)