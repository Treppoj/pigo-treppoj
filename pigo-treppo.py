#GOPIGO AUTNOMIS, ININSTAITED CLASS
#GopiGO methods at

from gopigo import *
import time
STOP_DIST = 50

__author__ = 'John'

class Pigo:

    ########                          ########
    ######## BASIC STATUS AND METHODS ########
    ########                          ########

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 200, 'rightspeed': 200, 'dist': 100}

    def __init__(self):
        print "Wassup boy, I'm Brover, BBBOOOOOOYYYYYY. beep beep."
        self.checkDist()

    def stop(self):
        self.status['ismoving'] = False
        print "Yo, Boss I'm havin' dem Issues stoppin!"
        for x in range(5):
            stop()

    def fwd(self):
        self.status['ismoving'] = True
        print "Yo, G. I tore my ACL, I'm out for dat season doe"
        for x in range(5):
            fwd()

    def bwd(self):
        self.status['ismoving'] = True
        print "Yo, G. I don't fell safe I ain't finna go"
        for x in range(5):
            bwd()

    #check if conditions are safe to continue operating
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "Obstacle is ahead, booooyyy"
            return False
        elif volt() > 14 or volt() < 6:
            print "My voltage is threatening to my life dog, its at: " + str(volt())
            return False
        else:
            return True
    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "Yo there's a obstacle " + str(self.status['dist']) + "mm ahead"
        if not self.keepGoing():
            print "EMERGENCY STOP FROM CHECK DISTANCE METHOD!"
                self.stop()

    ########                             ########
    ######## ADVANCED STATUS AND METHODS ########
    ########                             ########

        def safeDrive(self):
            self.fwd()
            while self.keepGoing():
                self.checkDist()
            self.stop()


        def servoSweep(self):
            for ang in range(20, 160, 5):
                servo(ang)
                time.sleep(.1)


    def dance(self):
        print "Yo G, I just wanna DANCE!"
        if self.keepGoing():
            self.circleRight()
            self.circleLeft()
            self.shuffle()
            self.servoShake()
            self.blink()

########                      ########
######## MAIN APP STARTS HERE ########
########                      ########


brover = Pigo()
while brover.keepGoing():
    brover.fwd()
    time.sleep(2)
    brover.stop()

brover.stop()