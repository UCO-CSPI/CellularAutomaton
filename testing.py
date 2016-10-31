from CellularAutomaton import *

def print_grid(grid):
    print(grid[0][0], grid[0][1], grid[0][2],'\n',
    grid[1][0], grid[1][1], grid[1][2],'\n',
    grid[2][0], grid[2][1], grid[2][2])


def test_neighbors():
    rows = 3
    columns = 3
    i=0
    grid=[[0 for x in range(columns)] for y in range(rows)]
    for x in range(columns):
        for y in range(rows):
            grid[x][y]=cell()
            i = i + 1

    print('Before SetNeighbors')
    print_grid(grid)

    SetNeighbors(grid,columns,rows)
    print('After SetNeighbors')
    print_grid(grid)

    for x in range(columns):
        for y in range(rows):
            g=grid[x][y]
            print('Neighbors of {} are {}, {}, {}, {}'.format(g.value,g.Neighbors[0],g.Neighbors[1],g.Neighbors[2],g.Neighbors[3]))

def test_update(stats):

    rows = 3
    columns = 3
    i=0
    grid=[[0 for x in range(columns)] for y in range(rows)]
    for x in range(columns):
        for y in range(rows):
            grid[x][y]=cell(stats[i])
            i = i + 1
    #print('after init')
    #print_grid(grid)
    SetNeighbors(grid,columns,rows)
    print('After SetNeighbors')
    print_grid(grid)

    for row in grid:
        for c in row:
            c.update()
    print('after update')
    print_grid(grid)


test_update(stats = (0,1,0,1,0,1,0,1,0))
test_update(stats = (0,0,0,0,1,0,0,0,1))
test_update(stats = (0,1,0,1,1,1,0,0,0))
test_update(stats = (0,1,0,1,0,1,0,0,0))