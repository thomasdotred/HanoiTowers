from first_attempt.game import Game
from first_attempt.hanoiAgents import TowerAgent

def main():
    print("setting up game")
    g1 = Game(3)
    g1.display_state()
    [g1.check_attribute_is_valid(att) for att in ["a", "b", "c"]]

    TowerAgent
    # g1.move_disk("a", "c", True)
    # g1.move_disk("a", "b", True)
    # g1.move_disk("c", "b", True)
    # g1.move_disk("a", "c", True)
    # g1.move_disk("b", "a", True)
    # g1.move_disk("b", "c", True)
    # g1.move_disk("a", "c", True)

if __name__ == "__main__":
    main()