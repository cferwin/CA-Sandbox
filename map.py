import sys

class Map:
    def __init__(self):
        # This array is the map itself. Later this will be loaded from a file.
        self.cells = [
            [False, False, False, False, True]
            , [False, True, False, False, False]
            , [False, False, True, False, False]
            , [False, True, True, False, True]
            , [True, False, False, False, False]
        ]

    def get_cell(self, x, y):
        """ Get the state of a cell.

            Returns the cell's state

            Variables:
            x       int     X coordinate of the cell
            y       int     Y coordinate of the cell
        """
        if x < 0 or y < 0:
            raise IndexError

        return self.cells[x][y]

    def set_cell(self, x, y, state):
        """ Set the state of a cell.

            Returns the cell's new state

            Variables:
            x       int     X coordinate of the cell
            y       int     Y coordinate of the cell
            state   bool    The cell's new state
        """
        self.cells[x][y] = state

        return self.cells[x][y]

    def print_cells(self):
        """ Prints the entire map to the screen. """
        for row in self.cells:
            for cell in row:
                if cell is True:
                    sys.stdout.write('#')
                elif cell is False:
                    sys.stdout.write('O')
                else:
                    sys.stdout.write('!')
            sys.stdout.write('\n')
        print()
        print()

    def update_cell(self, x, y):
        """ Update a cell.

            Returns the cell's new state

            Variables:
            x       int     X coordinate of the cell
            y       int     Y coordinate of the cell
        """
        neighbors = []
        neighbor_coordinates = [
            (x+1, y)
            , (x+1, y-1)
            , (x, y-1)
            , (x-1, y-1)
            , (x-1, y)
            , (x-1, y+1)
            , (x, y+1)
            , (x+1, y+1)
        ]
        alive = 0
        low_threshold = 0
        high_threshold = 2
        state = False

        # Find the cell's neighbors
        for coordinate in neighbor_coordinates:
            try:
                state = self.get_cell(coordinate[0], coordinate[1])
            except:
                state = False
            neighbors.append(state)

        # Count the number of live neighbor cells
        for cell in neighbors:
            if cell is True:
                alive += 1
        
        # Update the current cell based on the neighbors' states
        if alive > high_threshold or alive < low_threshold:
            self.set_cell(x, y, False)
        else:
            self.set_cell(x, y, True)

    def update_cells(self):
        """ Update the map. """
        # The coordinates will change to (0, 0) on the first iteration
        x = -1
        y = -1

        for row in self.cells:
            y += 1
            x = -1
            for cell in row:
                x += 1
                self.update_cell(x, y)
