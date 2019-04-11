from grid import Grid
from animator import Animator
from updater import Updater


def main():
    """Conway's game of life emulator function
    :returns: Thenga

    """
    N = 20
    the_grid = Grid(N).grid
    nexter = Updater().update
    Animator(nexter, the_grid)

if __name__ == "__main__":
    main()
