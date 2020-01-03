import argparse
import os
import sys
from game import Game
from hanoiAgents import startFinishAgent, hardCodedAdent3, KeyboardAgent


# Code for loading agents from blahAgents.py module

# def loadAgent(agent):
#     # TODO change to individual files for agents
#     agent_module = __import__("hanoiAgents")
#     avalible_agents = agent_module.__dict__.keys()
#
#     if agent not in list(avalible_agents):
#         raise ImportError(f"agent '{agent}' does not exist in agents module")
#     else:
#
#         return getattr(agent_module, agent)

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
    raise Exception('The agent ' + pacman + ' is not specified in any *Agents.py.')




def getArgs(args):
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-a",
        "--agents",
        default="hardCodedAdent3",
        help="Agent to run control game"
    ),
    ap.add_argument(
        "-n",
        "--num",
        default=3,
        help="number of disks in game"
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
        agents=agent,
        num=args["num"],
        catch_exceptions=args["catch_exceptions"],
        rules=args["rules"]
    )
    g1.display_state()
    g1.run()


if __name__ == "__main__":
    main(sys.argv)