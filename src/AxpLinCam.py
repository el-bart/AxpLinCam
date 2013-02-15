#!/usr/bin/python


class Camera:
    def __init__(self, host, user, password):
        self.__host = host
        self.__user = user
        self.__pass = password

    def up(self, multi):
        print "up"
        return True

    def down(self, multi):
        print "down"
        return True

    def left(self, multi):
        print "left"
        return True

    def right(self, multi):
        print "right"
        return True

    def home(self):
        print "home"
        return True

    def stop(self):
        print "stop"
        return True


