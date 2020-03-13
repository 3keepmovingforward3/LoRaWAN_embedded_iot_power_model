import random as random


class State:

    # instance attribute
    def __init__(self, name, qp, dp):
        self.name = name
        self.pValue = 1 + random.random() * 0.05
        self.qp = qp * self.pValue
        self.dp = dp * self.pValue
