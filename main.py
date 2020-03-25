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
battery_capacity = (1 - random.random() * 0.05)*6600e-6

sleep = node.State("Sleep", 8e-6, 8e-6)
listen = node.State("Wakeup & Listen", 500e-6, 1000e-6)
camera = node.State("Camera Wakeup & Image Recognition", 1100e-6, 2200e-9)
alert = node.State("Alert", 1260e-6, 25320e-6)


#  Location: Rohnert Park, California
#
def charge(t):
    return (2.675 * math.cos(2 * t * math.pi / 365) + 12.175) * 500e-6


def main():

    #  Day 365 = Winter Solstice
    #  Day 1 = Summer Solstice
    #  Normalized to battery
    #
    print("{:.3e}".format(((battery_capacity+charge(365)) -
                           ((0.9*sleep.qp*24) + (0.1*listen.qp)*24)))+"mAh after 24 hours")  # alpha simulation


if __name__ == '__main__':
    main()
