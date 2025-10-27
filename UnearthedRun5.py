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
'''llm.run_angle(speed=350,rotation_angle=-500)
llm.run_angle(speed=200,rotation_angle=500)'''
robot.settings(straight_speed=400)
robot.straight(500)
robot.turn(-25)
robot.straight(150)
robot.turn(25)
robot.straight(45)
robot.turn(-25)
robot.turn(27)
robot.straight(-90)
robot.turn(36)
llm.run_angle(speed=350,rotation_angle=-500)
robot.straight(200)
llm.run_angle(speed=200,rotation_angle=500)
robot.turn(20)
wait(500)
robot.turn(-23)
robot.settings(straight_speed=200)
robot.straight(-150)
robot.settings(turn_rate=20,straight_speed=977)
robot.turn(-45)
robot.straight(-600)