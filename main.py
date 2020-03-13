import node
import numpy as np


def main():
    state1 = node.State("Sleep", 8**-9, 8**-9)
    state2 = node.State("Wakeup & Listen", 500**-6, 1000**-6)
    state3 = node.State("Camera Wakeup & Image Recognition", 1100**-6, 2200**-9)
    state4 = node.State("Alert", 1260**-9, 25320**-9)


def run():
    daysPerYear = np.linspace(1, 366, 366) # time vector


if __name__ == '__main__':
    main()
    run()
