#!/usr/bin/python

import requests


# main class for managing the camera device
class Camera:
    # stores all the required parameters
    def __init__(self, host, user, password):
        self.__host = host
        # NOTE: currently user name name and password are not used (required only for streaming)
        self.__user = user
        self.__pass = password

    # basic moves
    def up(self, multi=False):
        self.__moveAction("up",   0 if multi else 1)
    def down(self, multi=False):
        self.__moveAction("down", 0 if multi else 1)
    def left(self, multi=False):
        self.__moveAction("left", 0 if multi else 1)
    def right(self, multi=False):
        self.__moveAction("right", 0 if multi else 1)

    # misc move commands
    def home(self):
        self.__moveAction("home", None)
    def stop(self):
        self.__moveAction("stop", None)

    # IR LEDs control
    def irLed(self, on):
        self.__irLedAction(on)


    # actual implementation
    def __moveAction(self, act, step):
        # basic link with the command
        cmd = "ptzctrl.cgi?-act=" + act
        # is direct move command?
        if step is not None:
            cmd += "&-step=" + str(step)
        self.__action(cmd, '[Success]call ptz funtion ok')

    # implementation of working with IR LEDs
    def __irLedAction(self, on):
        # basic link with the command
        mode = "open" if on else "close"
        cmd  = "param.cgi?cmd=setinfra&-status=" + mode
        self.__action(cmd, '')

    # common command processing code
    def __action(self, command, response):
        link = "http://" + self.__host + "/web/cgi-bin/hi3510/" + command
        # send the request
        r = requests.get(link)
        # ensure it didn't failed
        r.raise_for_status()
        # check the response
        txt = ' '.join( r.text.splitlines() ).encode("utf-8")
        if txt != response:
            raise Exception( "invalid/unknown reponse from '" + self.__host + "': " + txt )
