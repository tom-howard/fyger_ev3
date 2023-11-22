#!/usr/bin/env python3

# Connect the right motor to Motor Port D and the left motor to Port A
# Connect the Colour Sensor to Sensor Port 2

import time
import ev3dev.ev3 as ev3
from tuos_ev3 import ev3Utils

utils = ev3Utils()

def main():
    
    # display something on the screen of the robot
    print('Hello World!')

    # announce program start
    ev3.Sound.speak('Fyger demo starting!').wait()

    # setup the motors
    right_motor = ev3.LargeMotor('outD')
    left_motor = ev3.LargeMotor('outA')
    speed = -25

    # setup a colour sensor
    colour_sensor = ev3.ColorSensor('in2')

    loop_iteration = 0
    # main program loop
    for i in range (4):
        loop_iteration = loop_iteration + 1
        # fetch the colour value from the light sensor
        colour_val = colour_sensor.color
        
        dbg_msg = "[loop {}] colour value: {}".format(loop_iteration, colour_val)
        # print the above message to the EV3 display and the VS Code output panel...
        utils.ev3_print(dbg_msg)
        
        # announce the distance
        ev3.Sound.speak(colour_val).wait()

        # move
        right_motor.run_direct(duty_cycle_sp=speed)
        left_motor.run_direct(duty_cycle_sp=-speed)
        time.sleep(1)

        # stop
        right_motor.run_direct(duty_cycle_sp=0)
        left_motor.run_direct(duty_cycle_sp=0)
        
        # reverse direction
        speed = -speed
    
    # announce program end
    ev3.Sound.speak('Fyger demo ending').wait()

if __name__ == '__main__':
    main()
