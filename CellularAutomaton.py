import numpy
class cell:
    #InitialState = False
    #DefaultState = False


    def __init__(self, state=None, Neighbors=None):
        if state is None:
            if numpy.random.randint(2) == 1:
                self.state = True
            else:
                self.state = True #False
        else:
            self.state = state
        if Neighbors is None:
            self.Neighbors=[]
        else:
            self.Neighbors=Neighbors
        self.__set_value()
        self.OldState=self.state

    def __str__(self):
        return self.value.__str__()

    def update(self):
        c=0
        self.OldState = self.state
        for n in self.Neighbors:
            if n.OldState: #This needs changed to old state
                c += 1
        if c == 4:
            self.state = False
        elif c == 3:
            self.state = True
        #if c = 2, don't change state.
        elif c == 1:
            self.state = False
        self.__set_value()

    def __set_value(self):
        if self.state:
            self.value = 1
        else:
            self.value = 0

def SetNeighbors(grid, columns, rows):
    LastColumn = columns -1
    LastRow = rows - 1

    for y in range(rows):
        for x in range(columns):
            grid[y][x].Neighbors[:]=[] #Clear the neighbor list
            #to the right
            if x == LastColumn:
                grid[y][x].Neighbors.append(grid[y][0])
            else:
                grid[y][x].Neighbors.append(grid[y][x+1])
            #to the left
            if x == 0:
                grid[y][x].Neighbors.append(grid[y][LastColumn])
            else:
                grid[y][x].Neighbors.append(grid[y][x-1])
            #to the top
            if y == 0:
                grid[y][x].Neighbors.append(grid[LastRow][x])
            else:
                grid[y][x].Neighbors.append(grid[y-1][x])
            #to the botom
            if y == LastRow:
                grid[y][x].Neighbors.append(grid[0][x])
            else:
                grid[y][x].Neighbors.append(grid[y + 1][x])