from gopigo import *
import time

__author__ = 'John'

class Pigo:

    ########                          ########
    ######## BASIC STATUS AND METHODS ########
    ########                          ########

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 200, 'rightspeed': 200}

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

    ########                             ########
    ######## ADVANCED STATUS AND METHODS ########
    ########                             ########

########                      ########
######## MAIN APP STARTS HERE ########
########                      ########




brover = Pigo()
brover.fwd()
time.sleep(2)
brover.stop()
