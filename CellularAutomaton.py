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
def figureout(a):
    print(a)

class CAGrid(numpy.ndarray):

    def __new__(cls,shape, *args, **kwargs):
        print('in CAGrid new')
        print('  Args: ', args)
        print('KWargs: ', kwargs)

        if 'buffer' in kwargs:
            raise TypeError("buffer not allowed in constructor.  Initilize grid after constructor.")
            #Taking a buffer requires COPPYING the data instead of using the already existing memory location.
            #This could cause memory usage problems.
            #The data has to be coppied because the Base array which handles boundary conditions is larger than
            # the real cells.
            #databuffer= kwargs['buffer']
            #del kwargs['buffer']
            #print('Buffer values will be used, but not the memory locations')
        BaseShape = tuple([d+2 for d in shape])

        Base = numpy.ndarray.__new__(cls, BaseShape,*args, **kwargs)

        #ni stands for new instance.  It is the object this __new__ will return
        ni = Base[1:BaseShape[0]-1,1:BaseShape[1]-1]
        ni.Base        = Base
        ni.TopLeft     = Base[0:BaseShape[0]-2, 0:BaseShape[1]-2]
        ni.Top         = Base[0:BaseShape[0]-2, 1:BaseShape[1]-1]
        ni.TopRight    = Base[0:BaseShape[0]-2, 2:BaseShape[1]]
        ni.Left        = Base[1:BaseShape[0]-1, 0:BaseShape[1]-2]
        ni.Right       = Base[1:BaseShape[0]-1, 2:BaseShape[1]]
        ni.BottomLeft  = Base[2:BaseShape[0],   0:BaseShape[1]-2]
        ni.Bottom      = Base[2:BaseShape[0],   1:BaseShape[1]-1]
        ni.BottomRight = Base[2:BaseShape[0],   2:BaseShape[1]]
        ni.Neighbors   = [ni.Top, ni.TopRight, ni.Right, ni.BottomRight, ni.Bottom, ni.BottomLeft, ni.Left, ni.TopLeft]
        OldBase = Base.copy()
        Old     = OldBase[1:BaseShape[0]-1,1:BaseShape[1]-1]
        Old.Base        = OldBase
        Old.TopLeft     = Old.Base[0:BaseShape[0]-2, 0:BaseShape[1]-2]
        Old.Top         = Old.Base[0:BaseShape[0]-2, 1:BaseShape[1]-1]
        Old.TopRight    = Old.Base[0:BaseShape[0]-2, 2:BaseShape[1]]
        Old.Left        = Old.Base[1:BaseShape[0]-1, 0:BaseShape[1]-2]
        Old.Right       = Old.Base[1:BaseShape[0]-1, 2:BaseShape[1]]
        Old.BottomLeft  = Old.Base[2:BaseShape[0],   0:BaseShape[1]-2]
        Old.Bottom      = Old.Base[2:BaseShape[0],   1:BaseShape[1]-1]
        Old.BottomRight = Old.Base[2:BaseShape[0],   2:BaseShape[1]]
        Old.Neighbors   = [ni.Top, ni.TopRight, ni.Right, ni.BottomRight, ni.Bottom, ni.BottomLeft, ni.Left, ni.TopLeft]
        ni.Old = Old
        ni.TrueArray         = numpy.full(ni.shape,True,dtype=numpy.dtype('b'))

        # ni.OldTopLeft     = Base[0:BaseShape[0]-2, 0:BaseShape[1]-2]
        # ni.OldTop         = Base[0:BaseShape[0]-2, 1:BaseShape[1]-1]
        # ni.OldTopRight    = Base[0:BaseShape[0]-2, 2:BaseShape[1]]
        # NewInstance.OldLeft        = Base[1:BaseShape[0]-1, 0:BaseShape[1]-2]
        # NewInstance.OldRight       = Base[1:BaseShape[0]-1, 2:BaseShape[1]]
        # NewInstance.OldBottomLeft  = Base[2:BaseShape[0],   0:BaseShape[1]-2]
        # NewInstance.OldBottom      = Base[2:BaseShape[0],   1:BaseShape[1]-1]
        # NewInstance.OldBottomRight = Base[2:BaseShape[0],   2:BaseShape[1]]

        return ni


    def __array_finalize_(self, obj):
        print('in _array_finalize')

    def update(self):
        count = numpy.zeros(self.shape)
        for n in self.Old.Neighbors:
            count = count + n['Value']
        numpy.copyto(self.Old,self)         #Default is no change for count = 2
        numpy.place(self['Value'],count>3,False)     #If count > 3: new value = False
        numpy.place(self['Value'],count==3,True)      #If count = 3: new value = True
        numpy.place(self['Value'],count<2,False)     #if count < 2: new value = False








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

