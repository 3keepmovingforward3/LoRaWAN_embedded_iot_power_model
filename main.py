import node

# Global state objects
# State Object Arguments
# String: state name
# qp: Quiescent power; aka static power
# dp: Dynamic power
#
batterycapacity = 6600e-6 # Returns a float multiplied by the specified power of 10.
sleep = node.State("Sleep", 8e-6, 8e-6)
listen = node.State("Wakeup & Listen", 500e-6, 1000e-6)
camera = node.State("Camera Wakeup & Image Recognition", 1100e-6, 2200e-9)
alert = node.State("Alert", 1260e-6, 25320e-6)

def main():
    hour = batterycapacity - ((0.9*sleep.qp) + (0.1*listen.qp)) # alpha simulation
    
if __name__ == '__main__':
    main()
