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
        print()
        print()
        for row in self.cells:
            for cell in row:
                if cell is True:
                    sys.stdout.write('#')
                else:
                    sys.stdout.write('O')
            sys.stdout.write('\n')
        print()
        print()
