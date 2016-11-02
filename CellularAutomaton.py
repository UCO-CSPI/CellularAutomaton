import numpy

class cell:
    """Cell is an object for cellular automaton simulations"""


    #InitialState = False
    #DefaultState = False
    ProbInitialTrue = 0.5


    def __init__(self, state=None, Neighbors=None):
        if state is None:
            if numpy.random.rand() <= cell.ProbInitialTrue:
                self.state = True
            else:
                self.state = False
        else:
            self.state = state
        if Neighbors is None:
            self.Neighbors=[]
        else:
            self.Neighbors=Neighbors
        self.__set_value()
        self.OldState=self.state

    def __str__(self):   #instead, we should really define __getitem__(self,i) which is called for x[i]
        return self.value.__str__()

    def set_old_state(self):
        self.OldState = self.state


    def update(self):
        c=0
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
        elif c == 0:
            self.state = False
        self.__set_value()

    def __set_value(self):
        #self.value=self.state
        if self.state:
            self.value = 1
        else:
            self.value = 0

    def set_value(self):
        self.__set_value()

class CAGrid(numpy.ndarray):

    class CANeighborList():

        def __init__(self):
            self.Neighbors = [1, 2, 3, 4]

    def __array_finalize_(self, obj):
        print('in _array_finalize')




def SetNeighbors(grid, columns, rows, IncludeDiagonalNeighbors=True):
    LastColumn = columns -1
    LastRow = rows - 1

    for y in range(rows):
        for x in range(columns):
            grid[y][x].Neighbors[:]=[] #Clear the neighbor list

            #Find the indexes for right, left, top, bottom
            #to the right
            if x == LastColumn:
                r=0
            else:
                r=x+1
            #to the left
            if x == 0:
                l=LastColumn
            else:
                l = x-1
            #to the top
            if y == 0:
                t=LastRow
            else:
                t=y-1
            #to the botom
            if y == LastRow:
                b=0
            else:
                b=y + 1

            grid[y][x].Neighbors.append(grid[y][r])  #right
            grid[y][x].Neighbors.append(grid[y][l])  #left
            grid[y][x].Neighbors.append(grid[t][x])  #top
            grid[y][x].Neighbors.append(grid[b][x])  #bottom
            if IncludeDiagonalNeighbors:
                grid[y][x].Neighbors.append(grid[t][r])  # top right
                grid[y][x].Neighbors.append(grid[t][l])  # top left
                grid[y][x].Neighbors.append(grid[b][r])  # bottom right
                grid[y][x].Neighbors.append(grid[b][l])  # bottom left

