import matplotlib.pyplot as plt  
import matplotlib.animation as animation
from utils import UPDATEINTERVAL


class Animator(object):
    """Animator is used to plot the grid on matplotlib window"""
    def __init__(self,update, grid):
        fig, ax = plt.subplots() 
        img = ax.imshow(grid, interpolation='nearest') 
        ani = animation.FuncAnimation(fig, update, fargs=(img, grid), 
                                      frames = 10, 
                                      interval=UPDATEINTERVAL, 
                                      save_count=50) 
        plt.show()
