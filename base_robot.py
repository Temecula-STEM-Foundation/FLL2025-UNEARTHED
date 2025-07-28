from pybricks import version
from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Button, Port, Direction
import usys
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

from utils import get_battery_percentage

WHEEL_DIAMETER = 56  # mm
AXLE_TRACK = 150  # Distance between the points where both wheels touch the ground, mm

SENSOR_COLOR = 56
STRAIGHT_SPEED = 400
STRAIGHT_ACCEL = 600
TURN_RATE = 150
TURN_ACCEL = 360


class BaseRobot:
    def __init__(self):
        print(f"PrimeHub Firmware: {usys.version}")
        print(f"Pybricks Version: {version}")

        # noinspection PyTypeChecker
        self.hub: PrimeHub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
        # self.hub.system.set_stop_button()
        self.hub.light.on(Color.GREEN)

        # Get voltage and calculate the percentage
        voltage_mv = self.hub.battery.voltage()
        battery_pct = get_battery_percentage(voltage_mv)
        print(f"Battery: {battery_pct}% ({voltage_mv / 1000:.2f}V)")

        self.right_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.left_wheel = Motor(Port.E, Direction.CLOCKWISE)
        self.drive_base = DriveBase(self.left_wheel, self.right_wheel, WHEEL_DIAMETER, AXLE_TRACK)
        self.drive_base.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)

        self.right_motor = Motor(Port.B, Direction.CLOCKWISE)
        self.left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)

        self.front_color_sensor = ColorSensor(Port.D)
        self.back_color_sensor = ColorSensor(Port.C)


# def setup_robot():
#     # Set up all devices.
#     # noinspection PyTypeChecker
#     print(usys.version)
#     prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
#     print(version)
#     print(prime_hub.battery.voltage())
#     prime_hub.light.on(Color.BLUE)
#     prime_hub.system.set_stop_button(Button.CENTER)


# This base_robot.py file is not meant to be run like the mission files.
# But if someone does try (accidentally probably) to run it, show this
# error message.
if __name__ == "__main__":
    print("Don't run the base_robot.py file. Nothing to do here.")
    print("You probably meant to run one of the mission files.")
