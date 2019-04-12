from grid import Grid
from animator import Animator
from updater import Updater
from initiator import Gosper


def main():
    """Conway's game of life emulator function
    :returns: Thenga

    """
    N = 100
    the_grid = Grid(N).Init(Gosper).grid
    nexter = Updater().update
    Animator(nexter, the_grid)

if __name__ == "__main__":
    main()
