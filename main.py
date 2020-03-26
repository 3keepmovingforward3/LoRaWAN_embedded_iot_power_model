import math
import node
import random as random


# Global state objects
# State Object Arguments
# String: state name
# qp: Quiescent power; aka static power
# dp: Dynamic power
#
# Returns a float multiplied by the specified power of 10.
# Statistical p-value = 0.05
#
battery_capacity = (1.0 - random.random() * 0.05)*6600e-3

sleep = node.State("Sleep", 8e-3, 8e-3)
listen = node.State("Wakeup & Listen", 500e-3, 1000e-3)
camera = node.State("Camera Wakeup & Image Recognition", 1100e-3, 2200e-3)
alert = node.State("Alert", 1260e-3, 25320e-3)


#  Location: Eureka, California
# a = amplitude
#
def charge(t):
    a = 0.5*(14.0 + 55.0/60.0)
    c = 0.5*(14.0 - 55.0/60.0)

    return (a * math.cos(2.0 * t * math.pi / 365.0) + c) * 500e-3


def main():

    #  Day 365 = Winter Solstice
    #  Day 1 = Summer Solstice
    #  Normalized to battery
    #
    print(str(((battery_capacity+charge(365)) -
               ((0.9*sleep.qp*24) + (0.1*listen.qp)*24)))+"mAh after 24 hours")  # alpha simulation


if __name__ == '__main__':
    main()
