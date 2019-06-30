import logging
LOGGER = logging.getLogger(__name__)

class Updater(object):
    """Updater class which contains function to update"""
    def __init__(self):
        LOGGER.info("Updater Initialized")
        pass
        
    @staticmethod
    def update(self, img, grid):
        """TODO: Docstring for update.

        :img: 
        :grid: TODO
        :returns: TODO

        """
        N = len(grid)
        newGrid = grid.copy() 
        LOGGER.info("updating....")
        for i in range(N): 
            for j in range(N): 
      
                # compute 8-neghbor sum 
                # using toroidal boundary conditions - x and y wrap around  
                # so that the simulaton takes place on a toroidal surface. 
                total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] 
                             +grid[(i - 1) % N, j] + grid[(i + 1) % N, j] 
                             +grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N]
                             +grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N])) 
      
                # apply Conway's rules 
                if grid[i, j]  == 1: 
                    if (total < 2) or (total > 3): 
                        newGrid[i, j] = 0 
                else: 
                    if total == 3: 
                        newGrid[i, j] = 1 
      
        # update data 
        img.set_data(newGrid) 
        grid[:] = newGrid[:] 
        return img, 
