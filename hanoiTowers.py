import argparse
import os
import sys
import pdb
from game import Game

def loadAgent(pacman):
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
                return getattr(module, pacman)
    raise Exception(f'The agent {pacman} is not specified in any *Agents.py.')


def getArgs(args):
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-n",
        "--num",
        required=True,
        type=int,
        help="number of disks in game"
    ),
    ap.add_argument(
        "-a",
        "--agents",
        default="KeyboardAgent",
        help="Agent to run control game"
    )
    ap.add_argument(
        "-c",
        "--catch_exceptions",
        default=True,
        help="catch exceptions"
    )
    ap.add_argument(
        "-r",
        "--rules",
        default=[],
        help="rules for game"
    )

    return vars(ap.parse_args(args=args))


def main(args):
    print("setting up game")
    args = getArgs(sys.argv[1:])
    # args = {
    #     "num": 3,
    #     "agents": [KeyboardAgent()],
    #     "catch_exceptions": True,
    #     "rules": []
    # }

    agent = loadAgent(args["agents"])
    g1 = Game(
        agents=[agent],
        num=args["num"],
        catch_exceptions=args["catch_exceptions"],
        rules=args["rules"]
    )
    g1.display_state()
    g1.run()


if __name__ == "__main__":
    main(sys.argv)