import math
import node
import numpy as np
import matplotlib.pyplot as plt

# Global state objects
# State Object Arguments
# String: state name
# qp: Quiescent power; aka static power
# dp: Dynamic power
# Battery Capacity is numpy vector
battery_capacity = np.linspace(2000, 18000, endpoint=True)
days = np.linspace(4, 10)

sleep = node.State("Sleep", 8, 8)
listen = node.State("Wakeup & Listen", 500, 1000)
camera = node.State("Camera Wakeup & Image Recognition", 1100, 2200)
alert = node.State("Alert", 1260, 2520)


#  Location: Rohnert Park, California
#
def charge(t):
    return (2.675 * math.cos(2 * t * math.pi / 365) + 12.175) * 500e-6


def main():

    #  Day 364 = Winter Solstice
    #  Day 1 = Summer Solstice
    #  Normalized to battery
    #
    model = (battery_capacity - ((0.9 * sleep.qp * 24 * days) + (0.1 * listen.qp) * 24 * days))
    plt.plot(battery_capacity, model)
    plt.grid(True)
    plt.ylim(bottom=0)
    plt.xlim(xmin=9000)
    plt.xlabel('Prospective Battery Size in milli-amp hours (mAh)')
    plt.ylabel('Power Model 4-10 day range')
    plt.show()

if __name__ == '__main__':
    main()
