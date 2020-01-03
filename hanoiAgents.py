from game import Agent

class startFinishAgent(Agent):
    def __init__(self):
        Agent.__init__(self)

    def getAction(self, game):
        return "a", "c"

class hardCodedAdent3(Agent):
    def __init__(self):
        Agent.__init__(self)

    def getAction(self, game):
        hard_coded_moves =[
            ("a", "c"),
            ("a", "b"),
            ("c", "b"),
            ("a", "c"),
            ("b", "a"),
            ("b", "c"),
            ("a", "c")
        ]
        return hard_coded_moves[game.counter]


class hardCodedAdent2(Agent):
    def __init__(self):
        Agent.__init__(self)

    def getAction(self, game):
        hard_coded_moves =[
            ("a", "c"),
            ("a", "b"),
            ("c", "b"),
            ("a", "c"),
            ("b", "a"),
            ("b", "c"),
            ("a", "c")
        ]
        return hard_coded_moves[game.counter]


class KeyboardAgent(Agent):
    def __init__(self):
        self.keys = []

    def getAction(self, state):
        old = input("pole to remove disk from a, b or c:  ")
        new = input("pole to move disk to from a, b or c: ")
        return old, new
