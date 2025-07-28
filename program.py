from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Color, Direction, Port, Stop, Icon
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, multitask, run_task, wait, Matrix, vector

from base_robot import *

# base_robot.setup_robot()
# exit(0)
# def main():

robot = BaseRobot()
hub = robot.hub


async def main():
    pressed = []
    while True:
        pressed = hub.buttons.pressed()
        await wait(10)

        while any(pressed):
            # print("Listening for button...")
            if Button.RIGHT in pressed:
                print("Stop Mission")
                pressed = []

            if Button.LEFT in pressed:
                hub.light.on(Color.ORANGE)
                # while not Button.LEFT in pressed:
                print("Left Button Pressed")
                # simulate 30 second mission run here
                await wait(3000)
                hub.light.on(Color.GREEN)
                pressed = []

        # print('Front Color Sensor ', await CSF.color(), await CSF.hsv())
        # print('Back Color Sensor ', await CSB.color(), await CSB.hsv())

        # mission_found = True
        # if mission_found:
        #     break

        # print("Program ending...")
        # program_running = False
        # await wait(100)
        # robot.hub.system.shutdown()


# Runs the main program from start to finish
run_task(main())
# Set up all devices.
# noinspection PyTypeChecker
# prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
# timer = StopWatch()
# CSF = ColorSensor(Port.D)
# CSB = ColorSensor(Port.C)
# right_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
# left_wheel = Motor(Port.E, Direction.CLOCKWISE)
# left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
# right_motor = Motor(Port.B, Direction.CLOCKWISE)
# robot = DriveBase(left_wheel, right_wheel, 56, 150)
#
# # Initialize variables.
# SENSOR_COLOR = 56
# WHEEL_DIAMETER = 56
# AXLE_DISTANCE = 150
# STRAIGHT_SPEED = 400
# STRAIGHT_ACCEL = 600
# TURN_RATE = 150
# TURN_ACCEL = 360
#
#
# async def subtask():
#     await wait(1250)
#     await right_motor.run_angle(2000, -265)
#
#
# async def subtask2():
#     await wait(500)
#     await right_motor.run_angle(575, -500)
#
#
# async def Round_1():
#     await wait(0)
#     # right edge should be aligned to 2 1/2 from the home side
#     await multitask(
#         move(68, 80),
#         subtask(),
#     )
#     await robot.turn(-88)
#     await move(-3, 35)
#     await right_motor.run_angle(500, -265)
#     await wait(300)
#     # Picked up plankton sample
#     await move(28.5, 100)
#     await right_motor.run_angle(2000, 570)
#     # Whale 1 Flipped
#     await move(-10, 100)
#     await right_motor.run_angle(2000, -570)
#     # Whale 2 Flipped
#     await move(63.5, 50)
#     await right_motor.run_angle(575, 500)
#     # Picked up SeaBed Sample!
#     await multitask(
#         move(25.5, 50),
#         subtask2(),
#     )
#     await robot.turn(-18)
#     await move(20, 50)
#     await robot.turn(-50)
#     await move(70, 100)
#
#
# async def Round_2():
#     await wait(0)
#     print('Yellow Round started!')
#     await move(34, 50)
#     await robot.arc(150, angle=85)
#     await move(22, 50)
#     await wait(500)
#     # Pull out treasure box!
#     await move(-20, 50)
#     await robot.turn(-90)
#     await move(30, 50)
#     await move(-4, 50)
#     # ToDo: Broadcast ReadyToLiftDiver
#     await robot.turn(15)
#     await move(-17, 50)
#     await robot.turn(-55)
#     await move(15, 30)
#     await move(-1, 30)
#     right_motor.dc(50)
#     right_motor.track_target(900)
#     await move(-14, 50)
#     await robot.turn(80)
#     right_motor.track_target(720)
#     await move(5, 20)
#     right_motor.track_target(360)
#     await move(-6, 20)
#     # ToDo: set move motors E+A and need to come back to home
#
#
# async def Round_3():
#     await wait(0)
#     await multitask(
#         move(25, 50),
#         left_motor.run_angle(180, 200),
#         right_motor.run_angle(720, 610),
#     )
#     await robot.turn(45)
#     await move(16, 50)
#     await robot.turn(-45)
#     await move(42, 50)
#     await left_motor.run_angle(1000, -250)
#     await left_motor.run_angle(300, 250)
#     await move(-15, 50)
#     await robot.turn(-85)
#     await multitask(
#         left_motor.run_angle(250, -200),
#         right_motor.run_angle(720, -610),
#     )
#     await move(22, 50)
#     await multitask(
#         left_motor.run_angle(200, 220),
#         right_motor.run_angle(500, 500),
#     )
#     await move(-20, 50)
#     await robot.turn(83)
#     await move(15, 50)
#     await right_motor.run_angle(500, -400)
#     await multitask(
#         robot.arc(-2000, distance=-750),
#         right_motor.run_angle(500, -100),
#     )
#
#
# async def subtask3():
#     await wait(1000)
#     await move(-40, 100)
#
#
# async def Round_5():
#     await wait(0)
#     await move(19.5, 60)
#     await robot.turn(-42)
#     await move(21.5, 40)
#     await move(-7, 40)
#     await robot.turn(42)
#     await move(38, 60)
#     await robot.turn(-95)
#     await move(56, 50)
#     await move(-20, 60)
#     await move(2, 40)
#     left_motor.dc(100)
#     await left_motor.run_angle(360, -180)
#     await move(-1, 60)
#     await robot.turn(-55)
#     await move(-9, 60)
#     await robot.turn(155)
#     await left_motor.run_angle(720, 180)
#     await move(11, 40)
#     await left_motor.run_angle(720, -120)
#     await robot.turn(-50)
#     await move(2.5, 40)
#     await multitask(
#         Lift_Sub(),
#         subtask3(),
#     )
#     await multitask(
#         Lower_Green_Arm(),
#         robot.turn(25),
#     )
#     await move(-52, 100)
#
#
# async def Cleaning_code():
#     await wait(0)
#     await move(1000, 20)
#
#
# async def Round_7():
#     await wait(0)
#     robot.settings(straight_speed=250)
#     await robot.arc(-280, distance=960)
#     await robot.arc(-280, distance=-940)
#
#
# async def Round_6():
#     await wait(0)
#     await multitask(
#         move(69, 60),
#         Move_the_Boat(),
#     )
#     await robot.turn(45)
#     await move(18, 60)
#     left_motor.dc(100)
#     await left_motor.run_angle(138, 277)
#     await wait(500)
#     await move(-10, 60)
#     await robot.turn(88)
#     await move(-3, 30)
#     await right_motor.run_angle(90, 180)
#     await move(9, 30)
#     right_motor.dc(100)
#     await right_motor.run_angle(180, 360)
#     await move(-15, 30)
#     await robot.turn(43)
#     await move(-8, 30)
#     await right_motor.run_angle(163, 327)

#     await move(10, 30)
#
#
# async def Lower_Plankton_Arm():
#     await wait(0)
#     await wait(300)
#     left_motor.dc(100)
#     await left_motor.run_angle(720, 180)
#
#
# async def Lift_Plankton_Arm():
#     await wait(0)
#     left_motor.dc(100)
#     await left_motor.run_angle(360, -180)
#
#
# async def Lift_Sub():
#     await wait(0)
#     await left_motor.run_angle(360, -180)
#
#
# async def Lower_Green_Arm_2():
#     await wait(0)
#     await left_motor.run_angle(720, 300)
#
#
# async def Move_the_Boat():
#     await wait(0)
#     right_motor.dc(100)
#     await right_motor.run_angle(180, -180)
#
#
# async def move(distance_in_cm, speed_percentage):
#     await wait(0)
#     robot.use_gyro(True)
#     robot.settings(straight_speed=600 * (speed_percentage / 100))
#     await robot.straight(distance_in_cm * 10)
#     # We could not find a code to reset gyro, so we are just reseting both wheels instead :)
#     left_wheel.reset_angle(0)
#     right_wheel.reset_angle(0)
#
#
# async def main():
#     robot.settings(straight_speed=STRAIGHT_SPEED)
#     robot.settings(turn_rate=TURN_RATE)
#     robot.settings(turn_acceleration=TURN_ACCEL)
#     robot.settings(straight_acceleration=STRAIGHT_ACCEL)
#     prime_hub.light.on(Color.BLUE)
#     prime_hub.system.set_stop_button(Button.CENTER)
#     while True:
#         await wait(0)
#         while not Button.LEFT in prime_hub.buttons.pressed():
#             await wait(0)
#         if True:
#             print('Left Button Pressed!')
#             print(prime_hub.battery.voltage())
#             print('Front Color Sensor ', await CSF.color(), await CSF.hsv())
#             print('Back Color Sensor ', await CSB.color(), await CSB.hsv())
#         if await CSB.color() == Color.YELLOW and await CSF.color() == Color.RED:
#             await wait(500)
#             await Round_2()
#             await wait(1000)
#             raise SystemExit
#         if await CSB.color() == Color.BLUE and await CSF.color() == Color.BLUE:
#             await wait(500)
#             await Round_1()
#             await wait(1000)
#             raise SystemExit
#         if await CSB.color() == Color.RED and await CSF.color() == Color.RED:
#             await Round_7()
#         if await CSB.color() == Color.GREEN and await CSF.color() == Color.RED:
#             await wait(500)
#             await Round_3()
#             await wait(1000)
#             raise SystemExit
#         if await CSB.color() == Color.GREEN and await CSF.color() == Color.NONE:
#             print('Green Round 2 Started')
#             await wait(500)
#             await Round_5()
#             await wait(1000)
#             print('Green Round 2 Ended')
#         if await CSB.color() == Color.RED and await CSF.color() == Color.NONE:
#             await wait(500)
#             await Round_6()
#             await wait(1000)
#             raise SystemExit
#         if await CSB.color() == Color.NONE:
#             await wait(500)
#             robot.reset()
#             await wait(1000)
#             await prime_hub.speaker.beep(500, 100)
#
#
# run_task(main())
