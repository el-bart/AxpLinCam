#!/usr/bin/python


class Camera:
    def __init__(self, host, user, password):
        self.__host = host
        self.__user = user
        self.__pass = password

    def up(self, multi=False):
        print "up"
        return True

    def down(self, multi=False):
        print "down"
        return True

    def left(self, multi=False):
        print "left"
        return True

    def right(self, multi=False):
        print "right"
        return True

    def home(self):
        print "home"
        return True

    def stop(self):
        print "stop"
        return True


