from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait
#Setup everything
hub = PrimeHub()
llm = Motor(Port.B)
rlm = Motor(Port.F)
lsm = Motor(Port.A,Direction.COUNTERCLOCKWISE)
rsm = Motor(Port.E,Direction.CLOCKWISE)
robot = DriveBase(left_motor=lsm,right_motor=rsm,wheel_diameter=62.4,axle_track=128.5)
robot.use_gyro(True)


async def run1():
    await robot.use_gyro(True)
    #await #The Run
    await robot.settings(straight_speed=480)
    #await # Knock down one of the grass
    await robot.straight(650)
    #await # Grab brush and knock out the other grass
    await wait(500)
    await robot.straight(-620)
    #await # Wait to align the robot 
    await wait(500)
    #await #The Other Run
    await robot.settings(straight_speed=450)
    #await # Come closer to the mission model
    await robot.straight(200)
    await robot.turn(20)
    await robot.straight(550)
    await robot.turn(-70)
    #await # Push two landmass
    await robot.settings(straight_speed=300)
    await robot.straight(300)
    await rlm.run_angle(speed=200,rotation_angle=350)
    #await # Go back to base
    await robot.settings(straight_speed=977)
    await robot.straight(-140,then=Stop.NONE)
    await robot.turn(60,then=Stop.NONE)
    await robot.straight(-800)

async def run2():
    robot.use_gyro(True)
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
    robot.use_gyro(True)
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
    robot.straight(200)
    robot.turn(-63)
    robot.straight(67)
    llm.run_angle(speed=1000,rotation_angle=1300)
    robot.straight(-20)
    llm.run_angle(speed=500,rotation_angle=-200)
    robot.turn(55)
    robot.straight(600)

async def run5():
    robot.use_gyro(True)
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

    # Initialize variables.
runs = [run1, run2, run3, run4, run5]
current = 0

async def main():
    global current #current run
    hub.display.number(current+1)
    hub.system.set_stop_button(Button.BLUETOOTH)
    await wait(50)
    while True:
        hub.display.number(number=current + 1)
        while not any(hub.buttons.pressed()):
            await wait(0)
        if Button.LEFT in hub.buttons.pressed():
            current = (current - 1) % len(runs)
        elif Button.RIGHT in hub.buttons.pressed():
            current = (current + 1) % len(runs)
        elif Button.CENTER in hub.buttons.pressed():
            print(f"now running {runs[current]=}")
            await runs[current]()
            print(f"done task {current=}")
        await wait(240)


run_task(main())
