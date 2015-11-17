from gopigo import *


def checkMotor():
    for x in range(5):
        fwd()
    while True:
        v = volt()
        print v

