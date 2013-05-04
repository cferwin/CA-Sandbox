import map

m = map.Map()

m.print_cells()

def print_cells():
    # Print some cells for testing
    print(m.get_cell(0, 4))
    print(m.get_cell(4, 0))
    print(m.get_cell(0, 0))

print_cells()
# Update the cells
m.set_cell(0, 4, False)
m.set_cell(4, 0, False)
m.set_cell(0, 0, True)
print_cells()
m.print_cells()
