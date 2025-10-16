from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait


# Setup everything
hub = PrimeHub()
llm = Motor(Port.B)
rlm = Motor(Port.F)
lsm = Motor(Port.A,Direction.COUNTERCLOCKWISE)
rsm = Motor(Port.E,Direction.CLOCKWISE)
robot = DriveBase(left_motor=lsm,right_motor=rsm,wheel_diameter=62.4,axle_track=128.5)
robot.use_gyro(True)

# The Run
robot.settings(straight_speed=450,turn_rate=100)
robot.straight(300)
robot.turn(180)
robot.straight(-655)
robot.turn(-90)
robot.settings(straight_speed=100)
robot.straight(155)
rlm.run_angle(speed=100,rotation_angle=220)
wait(500)
rlm.run_angle(speed=-200,rotation_angle=220)
llm.run_angle(speed=70,rotation_angle=-50)
wait(1000)
robot.straight(-150)
llm.run_angle(speed=977,rotation_angle=-200)
robot.turn(40)
rlm.run_angle(speed=500,rotation_angle=300)
robot.settings(straight_speed=977,turn_rate=500)
robot.turn(50)
robot.straight(900)
 