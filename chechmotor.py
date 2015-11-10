from gopigo import *


def checkMotor(self):
    for x in range(5):
        fwd()
    while True:
        v = volt()
        print v
