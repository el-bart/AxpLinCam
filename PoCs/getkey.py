#!/usr/bin/python

# taken from http://code.activestate.com/recipes/577977-get-single-keypress

import sys
import tty
import termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        # handle arrow keys
        if ord(ch) == 27:
            ch = sys.stdin.read(1)
            if ord(ch) == 91:
                ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print "waiting for 10 keys:"
for i in range(1,10):
    k = getch()
    print k + " (" + str( ord(k) ) + ")"
