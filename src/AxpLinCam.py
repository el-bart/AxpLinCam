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

    # moves
    def up(self, multi=False):
        self.__action("up",   0 if multi else 1)
    def down(self, multi=False):
        self.__action("down", 0 if multi else 1)
    def left(self, multi=False):
        self.__action("left", 0 if multi else 1)
    def right(self, multi=False):
        self.__action("right", 0 if multi else 1)

    # misc commands
    def home(self):
        self.__action("home", None)
    def stop(self):
        self.__action("stop", None)


    # actual implementation
    def __action(self, act, step):
        # basic link with the command
        link = "http://" + self.__host + "/web/cgi-bin/hi3510/ptzctrl.cgi?-act=" + act
        # is direct move command?
        if step is not None:
            link += "&-step=" + str(step)
        # send the request
        r = requests.get(link)
        # ensure it didn't failed
        r.raise_for_status()
        # check the response
        txt = ' '.join( r.text.splitlines() ).encode("utf-8")
        if txt != '[Success]call ptz funtion ok':
            raise Exception( "invalid/unknown reponse from '" + self.__host + "': " + txt )
