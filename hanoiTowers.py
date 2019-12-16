import os

from game import Game
# from first_attempt.hanoiAgents import TowerAgent

'''
# Code for loading agents from blahAgents.py module

def loadAgent(pacman, nographics):
    # Looks through all pythonPath Directories for the right module,
    pythonPathStr = os.path.expandvars("$PYTHONPATH")
    if pythonPathStr.find(';') == -1:
        pythonPathDirs = pythonPathStr.split(':')
    else:
        pythonPathDirs = pythonPathStr.split(';')
    pythonPathDirs.append('.')

    for moduleDir in pythonPathDirs:
        if not os.path.isdir(moduleDir): continue
        moduleNames = [f for f in os.listdir(moduleDir) if f.endswith('gents.py')]
        for modulename in moduleNames:
            try:
                module = __import__(modulename[:-3])
            except ImportError:
                continue
            if pacman in dir(module):
                if nographics and modulename == 'keyboardAgents.py':
                    raise Exception('Using the keyboard requires graphics (not text display)')
                return getattr(module, pacman)
#     raise Exception('The agent ' + pacman + ' is not specified in any *Agents.py.')
'''

def main():
    print("setting up game")
    g1 = Game(3)
    g1.display_state()



    g1.run()

    # Winning strat
    # g1.move_disk(("a", "c"), True)
    # g1.move_disk(("a", "b"), True)
    # g1.move_disk(("c", "b"), True)
    # g1.move_disk(("a", "c"), True)
    # g1.move_disk(("b", "a"), True)
    # g1.move_disk(("b", "c"), True)
    # g1.move_disk(("a", "c"), True)

if __name__ == "__main__":
    main()