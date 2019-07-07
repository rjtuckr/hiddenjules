from random import *

#  Gonk's Fluke System
#  Gives each skill challenge a 15% chance for a lucky or unlucky chance encounter


def fluke_system():
    roll_one = randint(-1000, 1000)
    if roll_one <= -850:
        fluke_result = "Unlucky"

    elif roll_one >= 1850:
        fluke_result = "Lucky"

    else:
        fluke_result = None

    return fluke_result