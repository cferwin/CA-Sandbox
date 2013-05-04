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

    def print_cells(self):
        """ Prints the entire map to the screen. """
        for row in self.cells:
            for cell in row:
                if cell is True:
                    sys.stdout.write('#')
                else:
                    sys.stdout.write('O')
            sys.stdout.write('\n')
