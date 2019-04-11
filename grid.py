import numpy as np

class Grid(object):
    """Grid class deals with all things that will be done to grid"""
    def __init__(self, N):
        self.N = N
        self.grid = np.random.choice((0,1), N * N, p=[0.2, 0.8]).reshape(N, N)
        
