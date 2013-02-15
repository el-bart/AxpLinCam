#!/usr/bin/python

import sys
import tty
import termios
import xml.dom.minidom
import AxpLinCam


# helper function that returns key that has been pressed
def getChar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# call to print help message on the screen
def printHelp():
    print ""
    print "move step-by-step:"
    print "\tw - up (alt: arrow up)"
    print "\ts - down (alt: arrow down)"
    print "\ta - left (alt: arrow left)"
    print "\td - right (alt: arrow right)"
    print "move continous:"
    print "\tW - up"
    print "\tS - down"
    print "\tA - left"
    print "\tD - right"
    print "misc:"
    print "\tc - close (alt: ctrl+C)"
    print "\th - help"
    print "\tz - stop (alt: space bar)"
    print "\tx - home (alt: home button)"
    print ""
    print "NOTE: arrows can be used instead of w-s-a-d keys"
    print ""


# main part - processes an user-requested action
def processAction(cam):

    # read the key
    c = getChar()

    # check basic directions
    if c == 'w':
        return cam.up()
    if c == 's':
        return cam.down()
    if c == 'a':
        return cam.left()
    if c == 'd':
        return cam.right()

    # check basic directions, in continous mode
    if c == 'W':
        return cam.up(True)
    if c == 'S':
        return cam.down(True)
    if c == 'A':
        return cam.left(True)
    if c == 'D':
        return cam.right(True)

    # other functions
    if c == 'c':
        print "exiting..."
        sys.exit(0)
    if c == 'z' or c == ' ':
        return cam.stop()
    if c == 'x':
        return cam.home()
    if c == 'h':
        printHelp()
        return True

    # signal?
    if ord(c) == 3:     # ctrl+C
        sys.exit(0)
    # check for special keys
    if ord(c) == 27:    # 27 is escape
        c = getChar()

        # check for contorl keys
        if c == 'H':
            return cam.home()

        # check for arrows
        if c == '[':
            c = getChar()
            if c == 'A':
                return cam.up()
            if c == 'B':
                return cam.down()
            if c == 'C':
                return cam.right()
            if c == 'D':
                return cam.left()
        raise Exception("unknown special key: '" + c + "' (" + str(ord(c)) + ")" )

    # if everything failed, just rise an excaption...
    raise Exception("unknown key: '" + c + "' (" + str(ord(c)) + ")" )


# gets the content of a given node (shorter notation)
def getXmlNode(node, name):
    return node.getElementsByTagName(name)[0].childNodes[0].nodeValue

# parses config file and returns tuple with host, user and pass
def parseConfig(path):
    cfg = xml.dom.minidom.parse(path)
    h   = getXmlNode(cfg, 'host')
    u   = getXmlNode(cfg, 'user')
    p   = getXmlNode(cfg, 'pass')
    return (h, u, p)


#
# MAIN
#

# check for config file
if len(sys.argv) != 1+1:
    print sys.argv[0] + " <config.xml>"
    sys.exit(1)

# parse it
host, user, password = parseConfig(sys.argv[1])
# init video camera device
cam = AxpLinCam.Camera(user=user, password=password, host=host)

# show user what are the options
printHelp()
print "for video type:"
print "\tmplayer -user \"" + user + "\" -passwd \"xxxx\" \"rtsp://" + host + "/11  # high resolution"
print "\tmplayer -user \"" + user + "\" -passwd \"xxxx\" \"rtsp://" + host + "/12  # low resolution"
print ""

# main loop (can be braked from the internal call
while True:
    try:
        processAction(cam)
    except Exception as ex:
        print "ERROR: " + str(ex)
