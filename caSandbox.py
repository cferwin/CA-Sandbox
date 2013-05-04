import sys

cells = [
    [False, False, False, False, True],
    [False, True, False, False, False],
    [False, False, True, False, False],
    [False, True, True, False, True],
    [True, False, False, False, False],
]

for row in cells:
    for cell in row:
        if cell is True:
            sys.stdout.write('#')
        else:
            sys.stdout.write('O')
    sys.stdout.write('\n')
