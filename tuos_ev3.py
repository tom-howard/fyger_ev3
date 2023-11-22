import os
import sys

class ev3Utils():
    
    def __init__(self):
        # set the console just how we want it
        self.reset_console()
        self.set_cursor(False)
        self.set_font('Lat15-Terminus24x12')

        # print something to the output panel in VS Code
        self.ev3_print('Program Starting!')

    def ev3_print(self, *args, **kwargs):
        '''
        Print messages to the EV3 screen AND
        Print messages to stderr (to show in VS Code output panel).
        '''
        print(*args)
        print(*args, **kwargs, file=sys.stderr)


    def reset_console(self):
        '''Resets the console to the default state'''
        print('\x1Bc', end='')


    def set_cursor(self, state):
        '''Turn the cursor on or off'''
        if state:
            print('\x1B[?25h', end='')
        else:
            print('\x1B[?25l', end='')


    def set_font(self, name):
        '''Sets the console font

        A full list of fonts can be found with `ls /usr/share/consolefonts`
        '''
        os.system('setfont ' + name)