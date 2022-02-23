import argparse
import numpy as np
import random

def cli() -> None:
    """Receives CLI input from the user and calls the dice function
    """
    parser = argparse.ArgumentParser(description='Roll dice')

    parser.add_argument('dice', type=str, nargs='+', help='enter dice to roll in format 1d20 2d6 etc')

    args = parser.parse_args()
    print(type(args))
    rollDice(parseDice(args.dice))

def rollDice(dice: np.ndarray) -> None:
    """Rolls the dice
        args(np.ndarray)): nx2 list of parsed dice inputs where n is number of user inputs
    """
    for die in dice:
        numberOfDice = int(die[0])
        for i in range(0, numberOfDice):
            print(random.randint(1, int(die[1])))
    

def parseDice(dice: list[str]) -> np.ndarray:
    """Parses the dice inputs
        dice(list[str]): list of dice inputs in format 1d20, 6d4, etc.
        returns: (np.ndarray) parsed dice inputs
    """
    allDice = np.array(dice[0].split('d'))
    for d in range(1, len(dice)):
        allDice = np.vstack((allDice, dice[d].split('d')))

    return allDice

if __name__ == "__main__":
    cli()