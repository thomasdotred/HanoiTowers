from game import Agent
import random

class startFinishAgent(Agent):
    def __init__(self):
        Agent.__init__(self)

    def getAction(game):
        
        def calculate_all_moves(game):
            poles = game.state.keys()
            n=0
            # for p in poles:
            #     # n+=len(game.state[p])



        calculate_all_moves(game)
        raise NotImplementedError(f"agent not implemented")


class hardCodedAgent1(Agent):
    def __init__(self):
        Agent.__init__(self)

    def getAction(game):
        hard_coded_moves =[
            ("a", "c")
        ]
        return hard_coded_moves[game.counter]

class hardCodedAgent2(Agent):
    def __init__(self):
        Agent.__init__(self)

    def getAction(game):
        hard_coded_moves =[
            ("a", "b"),
            ("a", "c"),
            ("b", "c"),
        ]
        return hard_coded_moves[game.counter]

class hardCodedAgent3(Agent):
    def __init__(self):
        Agent.__init__(self)

    def getAction(game):
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

class hardCodedAgent4(Agent):
    def __init__(self):
        Agent.__init__(self)

    def getAction(game):
        hard_coded_moves =[
            ('a', 'b'), 
            ('a', 'c'), 
            ('b', 'c'), 
            ('a', 'b'), 
            ('c', 'a'), 
            ('c', 'b'), 
            ('a', 'b'), 
            ('a', 'c'), 
            ('b', 'c'), 
            ('b', 'a'), 
            ('c', 'a'), 
            ('b', 'c'), 
            ('a', 'b'), 
            ('a', 'c'), 
            ('b', 'c')
            ]
        return hard_coded_moves[game.counter]

class randomStateGenerator(Agent):
    def getAction(game):
        n = random.randint(1, 10)
        pole = ("a", "b", "c")
        
        for i in range(n):
            pass

        return NotImplementedError()


class KeyboardAgent(Agent):
    def __init__(self):
        self.keys = []

    def getAction(game):
        old, new = None, None
        while old not in ["a", "b", "c"]:
            old = input("pole to remove disk from a, b or c:  ")
        while new not in ["a", "b", "c"]:
            new = input("pole to move disk to from a, b or c: ")
        return old, new
