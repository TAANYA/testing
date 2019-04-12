from initiator import Empty, Glider, Gosper, Random

class Grid(object):
    """Grid class deals with all things that will be done to grid"""
    def __init__(self, N):
        self.N = N
    
    def Init(self, config=Empty):
        """Pattern Initializer

        :arg1: TODO
        :returns: TODO

        """
        self.config = config(self.N)
        self.grid = self.config.pattern(10,10).grid
        return self
