import curses

class Map:
    def __init__(self, screen, path):
        """ Initialize the map.
            
            Variables:
            screen  object  A Curses screen
            path    string  The path to the data file to be loaded
        """

        self.screen = screen
        if curses.has_colors():
            curses.start_color()

        # This array is the map itself. It can be loaded from a file using
        # load_file().
        self.cells = []
        # Load the file specified
        self.load_file(path)

    def load_file(self, path):
        """ Load a file of 1's and 0's representing the map's cells
            
            Sets self.cells to the cell data represented

            Variables:
            path    string  Path to the data file
        """

        # Try to open the data file
        try:
            f = open(path, 'r')
        except OSError:
            print("Error: File at", path, "could not be opened.")
            exit(1)
        except:
            print("Error: something went wrong opening the file at", path)
            exit(1)

        # Parse the file's contents
        for line in f:
            line = line.strip()

            if line[:2] == "//":
                # Don't parse comments
                pass
            else:
                # Create a new row
                self.cells.append([])

                # Load the cells
                for char in line:
                    if char == '0':
                        # Dead cell
                        self.cells[-1].append(False)
                    elif char == '1':
                        # Alive cell
                        self.cells[-1].append(True)

    def get_cell(self, x, y):
        """ Get the state of a cell.

            Returns the cell's state

            Variables:
            x       int     X coordinate of the cell
            y       int     Y coordinate of the cell
        """

        # Far boundaries of the map
        max_y = len(self.cells)-1
        def max_x(y):
            return len(self.cells[y])-1

        # Correct Y coordinate
        if y > max_y:
            # Y is off the bottom edge of the map
            y -= max_y + 1
        elif y < 0:
            # Y is off the top edge of the map
            y += max_y + 1

        # Correct X coordinate
        if x > max_x(y):
            # X is off the right edge of the map
            x -= max_x(y) + 1
        elif x < 0:
            # X is off the left edge of the map
            x += max_x(y) + 1

        return self.cells[y][x]

    def set_cell(self, x, y, state):
        """ Set the state of a cell.

            Returns the cell's new state

            Variables:
            x       int     X coordinate of the cell
            y       int     Y coordinate of the cell
            state   bool    The cell's new state
        """
        self.cells[y][x] = state

        return self.cells[y][x]

    def print_cells(self, x=0, y=0, refresh=True, live_color_pair=1, dead_color_pair=2):
        """ Prints the entire map to the screen.
            
            Variables
            x                   int     X coordinate of the top-left corner of the map
            y                   int     Y coordinate of the top-left corner of the map
            refresh             bool    Should the screen be refreshed after
                                        the function has finished
            live_color_pair     int     ID of the curses color pair used for
                                        printing live cells
            dead_color_pair     int     ID of the curses color pair used for
                                        printing dead cells
        """
        x_start = x - 1
        y_start = y - 1

        for row in self.cells:
            # Update the screen coordinates
            x = x_start
            y += 1

            for cell in row:
                x += 1

                self.screen.move(y, x)

                if cell is True:
                    self.screen.addch('#', curses.color_pair(live_color_pair))
                elif cell is False:
                    self.screen.addch('O', curses.color_pair(dead_color_pair))
                else:
                    self.screen.addch('!')

        if refresh:
            self.screen.refresh()

    def get_next_cell_state(self, x, y):
        """ Calculate the next state of a cell based on its current neighbors.
            Used for updating the map without letting the iterative method of
            updating to influence the cell updates.

            Returns the cell's next state

            Variables:
            x       int     X coordinate of the cell
            y       int     Y coordinate of the cell
        """
        neighbors = []
        neighbor_coordinates = [
              (x+1, y)
            , (x+1, y-1)
            , (x,   y-1)
            , (x-1, y-1)
            , (x-1, y)
            , (x-1, y+1)
            , (x,   y+1)
            , (x+1, y+1)
        ]
        state = False
        alive = 0
        low_death_threshold = 2
        high_death_threshold = 3
        born_number = 3

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
        
        # return the current cell's next state based on the neighbors' states
        state = self.get_cell(x, y)
        if alive > high_death_threshold or alive < low_death_threshold:
            # The cell dies from over or undercrowding
            return False
        else:
            if state is True:
                # The cell continues to live, no change
                return True
            else:
                if alive == born_number:
                    # Create a new cell
                    return True
                else:
                    # The cell is dead and remains dead, no change
                    return False

    def update_cells(self):
        """ Update the map. """
        # The coordinates will change to (0, 0) on the first iteration
        x = -1
        y = -1
        i = 0
        new_cells = []

        # Generate the new cell states
        for row in self.cells:
            y += 1
            x = -1
            for cell in row:
                x += 1
                new_cells.append(self.get_next_cell_state(x, y))

        # Set the current cells to the states just generated
        x = -1
        y = -1
        for row in self.cells:
            y += 1
            x = -1
            for cell in row:
                x += 1
                self.set_cell(x, y, new_cells[i])
                i += 1
