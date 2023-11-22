#!/usr/bin/env python3

# Connect the right motor to Motor Port D and the left motor to Port A
# Connect an Ultrasonic Sensor to Sensor Port 2

import time
import ev3dev.ev3 as ev3
from tuos_ev3 import ev3Utils

utils = ev3Utils()

def main():
    # announce program start
    ev3.Sound.speak('Ultrasonic example starting!').wait()

    # setup the motors
    right_motor = ev3.LargeMotor('outD')
    left_motor = ev3.LargeMotor('outA')
    speed = 0

    # setup the ultrasonic sensor (on port 2)
    ultrasound_sensor = ev3.UltrasonicSensor('in2')

    # main program loop
    while True:
        # fetch the distance reading from the ultrasonic sensor
        distance = ultrasound_sensor.value()
        if distance > 50 and distance <= 100:
            speed = 25
            dbg_msg = "MOVE! Object detected {} mm ahead".format(distance)
        else:
            speed = 0
            dbg_msg = "STOP! Object detected {} mm ahead".format(distance)

        utils.ev3_print(dbg_msg)
        # control the motors
        right_motor.run_direct(duty_cycle_sp=speed)
        left_motor.run_direct(duty_cycle_sp=speed)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
