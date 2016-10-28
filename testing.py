from CellularAutomaton import *

rows = 10
columns = 100
grid=[[cell() for x in range(columns)] for y in range(rows)]
SetNeighbors(grid, columns, rows)
for row in grid:
    for c in row:
        c.update()