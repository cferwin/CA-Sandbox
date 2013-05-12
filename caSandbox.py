import map
import time

m = map.Map("data/test_data.txt")

while True:
    m.print_cells()
    m.update_cells()
    time.sleep(0.5)
