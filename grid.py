from initiator import Empty
import logging
LOGGER = logging.getLogger(__name__)

class Grid(object):
    """Grid class deals with all things that will be done to grid"""
    def __init__(self, N):
        LOGGER.info("Grid Initialization of size %d in 3  2  1  ", N)
        self.N = N
    
    def Init(self, config=Empty):
        """Pattern Initializer

        :arg1: TODO
        :returns: TODO

        """
        if config.__name__ not in ["Random", "Gosper", "Glider", "Empty"]:
            LOGGER.error("Meaningless Grid configuration; Give a sane value")
            raise KeyError
        else:
            LOGGER.info("Configuration used: %s", config.__name__)

        try:
            self.config = config(self.N)
            self.grid = self.config.pattern(10,10).grid
        except Exception as e:
            LOGGER.error("Abort! Abort!")
            raise e

        LOGGER.info("Grid successfully Initialized")

        return self
