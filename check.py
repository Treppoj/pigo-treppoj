from gopigo import *
SAFE = 30 #Safe distance

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

    def quickCheck(self):
        self.status['dist'] = us_dist(15)
        if us_dist(15) >= SAFE:
            print "All clear"
            self.fwd()
        else:
            print "Obstacle " + str(self.status['dist']) + "mm ahead"