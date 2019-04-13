from grid import Grid
from animator import Animator
from updater import Updater
from initiator import Gosper
import logging
import sys
LOGGER = logging.getLogger(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def main():
    """Conway's game of life emulator function
    :returns: Thenga

    """
    N = 100
    the_grid = Grid(N).Init(Gosper).grid
    nexter = Updater().update
    Animator(nexter, the_grid)
    LOGGER.info("The End")

if __name__ == "__main__":
    main()
