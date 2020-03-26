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
battery_capacity = 7200

sleep = node.State("Sleep", 8, 8)
listen = node.State("Wakeup & Listen", 500, 1000)
camera = node.State("Camera Wakeup & Image Recognition", 1100, 2200)
alert = node.State("Alert", 1260, 25320)


def main():

    #  Day 365 = Winter Solstice
    #  Day 1 = Summer Solstice
    #  Normalized to battery
    #
    lit = battery_capacity - ((0.9*sleep.qp*24*5) + (0.1*listen.qp)*24*5)  # alpha simulation
    print(str(lit)+' mAh')


if __name__ == '__main__':
    main()
