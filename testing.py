from CellularAutomaton import *

def print_grid(grid):
    str = ''
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            str += grid[x][y].value.__str__() + '   '
        str += '\n'
    print(str)

def test_neighbors():
    rows = 3
    columns = 3
    i=0
    grid=[[0 for x in range(columns)] for y in range(rows)]
    for x in range(columns):
        for y in range(rows):
            grid[x][y]=Cell()
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

def test_update(rows, columns, interations, states):

    i=0
    grid=[[0 for x in range(columns)] for y in range(rows)]
    for y in range(rows):
        for x in range(columns):
            grid[y][x]=Cell(states[i])
            i = i + 1
    SetNeighbors(grid,columns,rows)
    print('After SetNeighbors')
    print_grid(grid)

    for i in range(interations):
        for row in grid:
            for c in row:
                c.update()
        SetOldStates(grid)
        print('After Update i = {}'.format(i+1))
        print_grid(grid)

def test_set_value():
    rows = 4
    columns = 4
    grid=[[0 for x in range(columns)] for y in range(rows)]
    for x in range(columns):
        for y in range(rows):
            grid[x][y]=Cell(False)
    SetNeighbors(grid,columns,rows)
    print('After SetNeighbors')
    print_grid(grid)

    grid[0][1].state = True
    grid[1][1].state = True
    grid[1][2].state = True
    grid[2][0].state = True
    grid[2][2].state = True
    for x in range(columns):
        for y in range(rows):
            grid[x][y].set_value()

    print('After set values')
    print_grid(grid)




print('test_update(3, 3, 2, states = (0,1,0,1,0,1,0,1,0))')
test_update(3, 3, 2, states = (0,1,0,1,0,1,0,1,0))
print('next should give a stable block in upper right corner.')
test_update(3, 3, 2, states = (1,1,0,1,1,0,0,0,0))
print('next should go from vertical line to filled, to dead,')
test_update(3, 3, 2, states = (0,0,0,1,1,1,0,0,0))
print('next should go give a line blinker')
test_update(4, 5, 5, states = (0,0,0,0,0,
                               0,0,0,0,0,
                               0,1,1,1,0,
                               0,0,0,0,0))
print('next')
test_update(3,3,3,states = (0,1,0,1,0,1,0,1,0))
