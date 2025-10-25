from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
color_sensor_R = ColorSensor(Port.E)
color_sensor_L = ColorSensor(Port.A)
LLM = Motor(Port.D, Direction.COUNTERCLOCKWISE)
RLM = Motor(Port.F, Direction.CLOCKWISE)
LMM = Motor(Port.C, Direction.CLOCKWISE)
RMM = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(LLM, RLM, wheel_diameter=56, axle_track=116)

async def subtask():
    await drive_base.straight(500)
    await wait(1000)
    await drive_base.straight(-500)

async def subtask2():
    await multitask(
        LMM.run_angle(500, 720),
        RMM.run_angle(500, -720),
    )


async def run_1():
    await wait(0)
    print("running run 1 hahaha")
    drive_base.settings(straight_speed=950)
    LLM.control.limits(acceleration=2000)
    RMM.control.limits(acceleration=2000)
    drive_base.use_gyro(True)
    drive_base.reset(0, 0)
    prime_hub.imu.reset_heading(0)
    print(prime_hub.battery.voltage())
    await prime_hub.speaker.beep(500, 1000)
    for count in range(4):
        await wait(0)
        await drive_base.turn(90)
        await drive_base.straight(100)
    drive_base.stop()


async def run_2():
    await wait(0)
    drive_base.settings(straight_speed=950)
    LLM.control.limits(acceleration=2000)
    RMM.control.limits(acceleration=2000)
    drive_base.use_gyro(True)
    drive_base.reset(0, 0)
    prime_hub.imu.reset_heading(0)
    print(prime_hub.battery.voltage())
    await wait(50)
    await prime_hub.speaker.beep(500, 1000)
    await multitask(
        subtask(),
        subtask2(),
    )
    drive_base.straight(0)

async def run_3():
    await wait(0)
    await prime_hub.speaker.beep(420, 1000)
    drive_base.use_gyro(False)
    drive_base.use_gyro(True)
    prime_hub.imu.reset_heading(0)
    for count2 in range(4):
        await wait(0)
        await drive_base.turn(-179)
        await drive_base.straight(200)
    print(prime_hub.battery.voltage())


# Initialize variables.
runs = [run_1, run_2, run_3]
current = 0

async def main():
    global current #current run
    prime_hub.display.number(current+1)
    prime_hub.system.set_stop_button(Button.BLUETOOTH)
    await wait(50)
    while True:
        prime_hub.display.number(number=current + 1)
        while not any(prime_hub.buttons.pressed()):
            await wait(0)
        if Button.LEFT in prime_hub.buttons.pressed():
            current = (current - 1) % len(runs)
        elif Button.RIGHT in prime_hub.buttons.pressed():
            current = (current + 1) % len(runs)
        elif Button.CENTER in prime_hub.buttons.pressed():
            print(f"now running {runs[current]=}")
            await runs[current]()
            print(f"done task {current=}")
        await wait(240)


run_task(main())

