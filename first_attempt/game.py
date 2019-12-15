class Agent:
    """
    An agent must define a getAction method
    """
    def getAction(self, state):
        raise NotImplementedError()
        # return {"old": "a", "new": "b"}


class Game:
    def __init__(self, agents, num=3,catch_exceptions=True, rules = []):
        self.a = [i for i in range(num, 0, -1)]
        self.b = []
        self.c = []

        self.agents = agents
        self.gameOver = False
        self.moveHistory = []
        self.catchExceptions = catch_exceptions
        self.rules = rules

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

    def move_disk(self, old: str, new: str, display_state=False):
        disk = self.remove_disk(old)
        self.check_legal_move(disk, new)
        self.add_disk(new, disk)
        if display_state:
            self.display_state()

    def check_legal_move(self, disk, new):
        disk_on_new_location = getattr(self, new)

        if len(disk_on_new_location) > 0 and disk > disk_on_new_location[-1]:
            self.display_state()
            raise AssertionError("invalid move")

    def run(self):
        while not self.gameOver:
            agent = self.agents
            move_time = 0

            # observe state of game
            observation = self.get_state()
            # check total time
            # check agent move time


            # get action
            action = agent.getAction(observation)

            # execute the action
            self.moveHistory.append(action)
            self.move_disk()

            # check for end state
