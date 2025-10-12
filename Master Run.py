

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
max_run = 3

async def subtask():
    await robot.straight(500)
    await wait(1000)
    await robot.straight(-500)

async def subtask2():
    await multitask(
        lsm.run_angle(500, 720),
        rsm.run_angle(500, -720),
    )

async def run2():
    await wait(0)
    robot.settings(straight_speed=950)
    llm.control.limits(acceleration=2000)
    rsm.control.limits(acceleration=2000)
    robot.use_gyro(True)
    robot.reset(0, 0)
    hub.imu.reset_heading(0)
    print(hub.battery.voltage())
    await wait(50)
    await hub.speaker.beep(500, 1000)
    await multitask(
        subtask(),
        subtask2(),
    )
    robot.straight(0)

async def run1():
    await wait(0)
    await hub.speaker.beep(500, 1000)
    for count in range(4):
        await wait(0)
        await robot.turn(90)
        await robot.straight(100)
    robot.stop()

async def run3():
    await wait(0)
    await hub.speaker.beep(420, 1000)
    robot.use_gyro(False)
    robot.use_gyro(True)
    hub.imu.reset_heading(0)
    for count2 in range(4):
        await wait(0)
        await robot.turn(-179)
        await robot.straight(200)
    print(hub.battery.voltage())

async def main():
    global run_number
    hub.display.number(run_number)
    #print(run_number)
    hub.system.set_stop_button(Button.BLUETOOTH)
    await wait(50) #waitfor everything to settle
    while True:
        await wait(240)# wait for the human to release the button
        while not any(hub.buttons.pressed()):
            await wait(0)
        if Button.LEFT in hub.buttons.pressed():
            #wrap around run number using modulo arithmetic
            #left button going counter clockwise for the run number
            run_number = ((run_number - 1) - 1) % max_run + 1
            #print(run_number)
            hub.display.number(run_number)
        else:
            if Button.RIGHT in hub.buttons.pressed():
                #right button going clockwise for the run number
                run_number = ((run_number - 1) + 1) % max_run + 1
                #print(run_number)
                hub.display.number(run_number)
            else:
                if Button.CENTER in hub.buttons.pressed():
                    if run_number == 1:
                        print('now running run1')
                        await run1()
                    else:
                        if run_number == 2:
                            print('now running run2')
                            await run2()
                        else:
                            if run_number == 3:
                                print('now running run3')
                                await run3()
                            else:
                                print('exit')
                                break
                else:
                    continue


run_task(main())