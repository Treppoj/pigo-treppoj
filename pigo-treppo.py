from gopigo import *
import time

__author__ = 'John'

class Pigo:

    isMoving = False
    servoPos = 90

    def __init__(self):
        print "Wassup boy, I'm Brover, BBBOOOOOOYYYYYY. beep beep."

    def stop(self):
        slef.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "Yo, Boss I'm havin' dem Issues stoppin!"

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(.1)
            print "Yo, G. I tore my ACL, I'm out for dat season doe"


brover = Pigo()
brover.fwd()
time.sleep(2)
brover.stop()
