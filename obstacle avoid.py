from gopigo import *
import time
SAFE = 30 #Safe distance

class Pigo:

    ########                          ########
    ######## BASIC STATUS AND METHODS ########
    ########                          ########

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 150, 'rightspeed': 150, 'dist': 100}

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

    def clear(self):
        if self.status['dist'] < STOP_DIST:
            print "Obstacle is ahead, booooyyy"
            return False
        elif volt() > 14 or volt() < 6:
            print "My voltage is threatening to my life dog, its at: " + str(volt())
            return False
        else:
            return True

    def quickCheck(self):
        self.status['dist'] = us_dist(15)
        if us_dist(15) >= SAFE:
            print "All clear"
            self.safeDrive()
        else:
            print "Obstacle " + str(self.status['dist']) + "mm ahead"

    def safeDrive(self):
        self.fwd()
        while self.quickCheck()

    def servoSweep(self):

    def isTherePath(self):

    def turnTo(self):

    def safeAng(self):

    def backTrack(self):


    ########                          ########
    ######## BASIC STATUS AND METHODS ########
    ########                          ########


    def obstacleAvoid(self):
        while True:
            if self.quickCheck():
                self.safeDrive()
            else:
                self.servoSweep()
                if self.isTherePath():
                    self.turnTo(self.safeAng())
                else:
                    self.backTrack()


brover = Pigo()
brover.quickCheck()







