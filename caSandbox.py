import map
import curses

# Set up Curses screen
screen = curses.initscr()

curses.noecho()
screen.keypad(True)
curses.cbreak()
curses.halfdelay(5)     # Wait for half a second for input before continuing
curses.start_color()

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

# Initialize the map
m = map.Map(screen, "data/test_data.txt")

i = 0

while True:
    # Check for exit key
    char = screen.getch()
    if char == ord('q'):
        break

    # Advance the simulation
    m.print_cells(x=10, y=10)
    m.update_cells()

# Clean up
curses.nocbreak()
screen.keypad(False)
curses.echo()

curses.endwin()
