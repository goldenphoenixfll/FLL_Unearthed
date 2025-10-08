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
robot.straight(600)
wait(500)
robot.straight(-650)
wait(4000)
#The Other Run
robot.settings(straight_speed=450)
rlm.run_angle(speed=500,rotation_angle=-310)
robot.straight(700)
robot.turn(-39)
robot.straight(170)
rlm.run_angle(speed=200,rotation_angle=350)
robot.settings(straight_speed=977)
robot.straight(-140,then=Stop.NONE)
robot.turn(60,then=Stop.NONE)
robot.straight(-800)




#Original Code
'''robot.settings(straight_speed=450)
robot.straight(650)
robot.turn(-35)
robot.straight(60)
rlm.run_angle(speed=500,rotation_angle=-310)
robot.straight(60)
rlm.run_angle(speed=200,rotation_angle=550)
robot.straight(-110)
robot.turn(-55)
robot.use_gyro(False)
robot.straight(135)
llm.run_angle(speed=300,rotation_angle=-550)
llm.run_angle(speed=280,rotation_angle=550)
robot.settings(straight_speed=977)
robot.arc(radius=-100,angle=-180,then=Stop.NONE)
#robot.straight(-500)'''