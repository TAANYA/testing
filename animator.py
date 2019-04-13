import matplotlib.pyplot as plt  
import matplotlib.animation as animation
from utils import UPDATEINTERVAL
import logging
LOGGER = logging.getLogger(__name__)


class Animator(object):
    """Animator is used to plot the grid on matplotlib window"""
    def __init__(self,update, grid):
        LOGGER.info("Animator class")
        fig, ax = plt.subplots() 
        img = ax.imshow(grid, interpolation='nearest') 
        try:
            ani = animation.FuncAnimation(fig, update, fargs=(img, grid),
                                          frames = 10, interval=UPDATEINTERVAL,
                                          save_count=50)
            plt.show()
        except Exception as e:
            LOGGER.error("Something wrong with matplotlib animation module :/")
            raise e
