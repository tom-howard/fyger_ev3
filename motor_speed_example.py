#!/usr/bin/env python3

# Connect the right motor to Motor Port D and the left motor to Port A

import time
import ev3dev.ev3 as ev3
from tuos_ev3 import ev3Utils

utils = ev3Utils()

def main():
    
    # display something on the screen of the robot
    print('Hello World!')

    # announce program start
    ev3.Sound.speak('Motor speed example starting!').wait()

    # setup the motors
    right_motor = ev3.LargeMotor('outD')
    left_motor = ev3.LargeMotor('outA')
    
    direction = 1
    # main program loop
    while True:
        right_speed = 0
        left_speed = 0
        for i in range (5):
            right_speed = right_speed + (direction*15)
            left_speed = -1*right_speed
            
            dbg_msg = "Right: {}%, Left: {}%".format(right_speed, left_speed)
            utils.ev3_print(dbg_msg)
            
            # announce the distance
            ev3.Sound.speak(abs(right_speed)).wait()

            # move
            right_motor.run_direct(duty_cycle_sp=right_speed)
            left_motor.run_direct(duty_cycle_sp=left_speed)
            time.sleep(1)

            # stop
            right_motor.run_direct(duty_cycle_sp=0)
            left_motor.run_direct(duty_cycle_sp=0)
            time.sleep(1)
            
        # reverse direction
        direction = -direction
    
if __name__ == '__main__':
    main()
