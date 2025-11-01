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
robot.settings(straight_speed=480)
# Knock down one of the grass
robot.straight(650)
# Grab brush and knock out the other grass
wait(500)
robot.straight(-620)
# Wait to align the robot
wait(500)
#The Other Run
robot.settings(straight_speed=450)
# Come closer to the mission model
robot.straight(200)
robot.turn(20)
robot.straight(550)
robot.turn(-70)
# Push two landmass
robot.settings(straight_speed=300)
robot.straight(300)
rlm.run_angle(speed=200,rotation_angle=350)
# Go back to base
robot.settings(straight_speed=977)
robot.straight(-140,then=Stop.NONE)
robot.turn(47,then=Stop.NONE)
robot.straight(-800)
