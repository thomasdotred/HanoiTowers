import time


class Agent:
    """
    An agent must define a getAction method
    """
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
        # raise NotImplementedError()
        # return {"old": "a", "new": "b"}


class Game:
    def __init__(self, agents=[], num=3, catch_exceptions=True, rules=[]):
        self.num = num
        self.a = [i for i in range(num, 0, -1)]
        self.b = []
        self.c = []

        self.agents = agents
        self.gameOver = False
        self.result = False
        self.moveHistory = []
        self.catchExceptions = catch_exceptions
        self.rules = rules
        self.counter = 0

    def get_state(self):
        return self.a, self.b, self.c

    def display_state(self):
        print(f"\t a: {self.a}")
        print(f"\t b: {self.b}")
        print(f"\t c: {self.c}")
        print("----------------------------------------")

    def check_attribute_is_valid(self, att):
        existing = self.__dir__()
        if not hasattr(self, att):
            raise AttributeError(f"object '{self.__class__.__name__}' has no attribute '{att}'")

    def remove_disk(self, old):
        values = getattr(self, old)
        moving_disk = values.pop()
        setattr(self, old, values)
        return moving_disk

    def add_disk(self, new, moving_disk):
        values = getattr(self, new)
        values.append(moving_disk)
        setattr(self, new, values)

    def move_disk(self, action: tuple, display_state=True):
        old, new = action
        disk = self.remove_disk(old)
        self.check_legal_move(disk, action)
        self.add_disk(new, disk)
        if display_state:
            self.display_state()

    def check_legal_move(self, disk, action):
        old, new = action
        disk_on_new_location = getattr(self, new)

        if len(disk_on_new_location) > 0 and disk > disk_on_new_location[-1]:
            self.display_state()
            raise Warning(f"invalid move: Can't put a disk on one what is smaller.\nattempted move: {disk} onto stack of [{disk_on_new_location[-1]}]")


        # if len(getattr(self, old)) == 0:
        #     self.gameOver = True

    def run(self):
        self.counter = 0
        while not self.gameOver:

            agent = self.agents
            move_time = 0

            # observe state of game
            observation = self.get_state()


            # check total time
            # check agent move time


            # get action
            self.agents = Agent()
            action = self.agents.getAction(self)

            # execute the action
            self.moveHistory.append(action)
            self.move_disk(action)

            # check for end state
            self.counter = self.counter + 1
            self.check_end_state()
            time.sleep(0.1)
        # end game results
        self.display_state()

        self.display_results()



    def check_end_state(self):
        pole_c = getattr(self, "c")
        if len(pole_c) == self.num:
            self.result = True
            self.gameOver = True

    def display_results(self):
        print("################################")
        print(f"Game ended!")
        print(f"Won game?: {self.result}")
        print(f"Number of moves: {self.counter}")
        print(f"History of moves: {self.moveHistory}")
