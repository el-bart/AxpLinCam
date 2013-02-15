#!/usr/bin/python

import requests


class Camera:
    def __init__(self, host, user, password):
        self.__host = host
        # NOTE: currently user name name and password are not used (required only for streaming)
        self.__user = user
        self.__pass = password

    def up(self, multi=False):
        self.__move("up",   0 if multi else 1)
    def down(self, multi=False):
        self.__move("down", 0 if multi else 1)
    def left(self, multi=False):
        self.__move("left", 0 if multi else 1)
    def right(self, multi=False):
        self.__move("right", 0 if multi else 1)

    def home(self):
        self.__move("home", 0)
    def stop(self):
        self.__move("stop", 0)

    def __move(self, act, step):
        link = "http://" + self.__host + "/web/cgi-bin/hi3510/ptzctrl.cgi?-act=" + act + "&-step=" + str(step)
        r = requests.get(link)
        if r.status_code != 100:
            r.raise_for_status()
        #r.text.encode("utf-8")


