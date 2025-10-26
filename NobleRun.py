from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

hub = PrimeHub()

# Set up all devices.
llm = Motor(Port.B)#for left attachment
rlm = Motor(Port.F)#for right attachment
lsm = Motor(Port.A, Direction.COUNTERCLOCKWISE)#for left side of drive base
rsm = Motor(Port.E, Direction.CLOCKWISE)#for right side of drive base
robot = DriveBase(lsm, rsm, wheel_diameter=56, axle_track=111.3) # wheel_diameter=56mm, axle_track=111.3mm
robot.use_gyro(True)

# Initialize variables.
run_number = 1
max_run = 5



async def run1():
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
    robot.turn(60,then=Stop.NONE)
    robot.straight(-800)


async def run2():
    # The Run
    robot.settings(straight_speed=450,turn_rate=100)
    robot.straight(300)
    robot.turn(180)
    robot.straight(-655)
    robot.turn(-90)
    robot.settings(straight_speed=100)
    robot.straight(155)
    rlm.run_angle(speed=100,rotation_angle=250)
    wait(500)
    rlm.run_angle(speed=-200,rotation_angle=250)
    llm.run_angle(speed=70,rotation_angle=-60)
    wait(1000)
    robot.straight(-140)
    llm.run_angle(speed=977,rotation_angle=-200)
    robot.turn(40)
    rlm.run_angle(speed=500,rotation_angle=300)
    robot.settings(straight_speed=977,turn_rate=500)
    robot.turn(50)
    robot.straight(900)


async def run3():
    # The Run
    robot.settings(straight_speed=500)
    # Go into the boat
    robot.straight(500)
    # Pull sand off of the boat
    robot.straight(-200)
    robot.settings(straight_speed=100)
    robot.use_gyro(False)
    robot.settings(150)
    # Push the boat up and deliver a flag
    robot.straight(260)
    # Go back to base
    robot.settings(straight_speed=200)
    robot.turn(15,then=Stop.NONE)
    robot.straight(-700)


async def run4():
    robot.use_gyro(True)
    robot.settings(straight_speed=500)
    #rlm.run_angle(speed=1500,rotation_angle=300)
    robot.straight(1075)
    robot.turn(90)
    robot.straight(100)
    robot.turn(-15)
    rlm.run_angle(speed=1500,rotation_angle=1000)
    robot.turn(33)
    robot.settings(straight_speed=300)
    robot.straight(-190)
    #robot.turn(45)
    robot.straight(135)
    robot.turn(-90)
    robot.settings(straight_speed=977)
    robot.straight(800)

async def main():

    runs = [run1, run2, run3, run4]

    current = 0

    while True:

        hub.display.number(number= current + 1)

if hub.button.left.is_pressed():
    
    current = (current - 1) % len(runs)

elif hub.button.right.is_pressed():

    current = (current + 1) % len(runs)

elif hub.button.center.is_pressed():

    runs[current]()


run_task(main())
