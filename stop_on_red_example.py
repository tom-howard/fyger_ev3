#!/usr/bin/env python3

# Connect the right motor to Motor Port D and the left motor to Port A
# Connect the Colour Sensor to Sensor Port 2

import time
import ev3dev.ev3 as ev3
from tuos_ev3 import ev3Utils

utils = ev3Utils()

def main():
    # announce program start
    ev3.Sound.speak('Stop on Red example starting!').wait()

    # setup the motors
    right_motor = ev3.LargeMotor('outD')
    left_motor = ev3.LargeMotor('outA')
    speed = 0

    # setup the light (colour) sensor
    colour_sensor = ev3.ColorSensor('in2')

    # main program loop
    while True:
        # fetch the colour value from the light sensor
        colour_val = colour_sensor.color
        if colour_val == 5:
            speed = 0
            dbg_msg = "STOP! Colour Value is {}".format(colour_val)
        else:
            speed = 25
            dbg_msg = "MOVE! Colour Value is {}".format(colour_val)

        utils.ev3_print(dbg_msg)
        # control the motors
        right_motor.run_direct(duty_cycle_sp=speed)
        left_motor.run_direct(duty_cycle_sp=speed)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
