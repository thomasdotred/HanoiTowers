from game import Agent


class KeyboardAgent(Agent):
    def __init__(self):
        self.keys = []

    def getAction(self, state):
        old = input("pole to remove disk from:   ")
        new = input("pole to movee disk to from: ")



