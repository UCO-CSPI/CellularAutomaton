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
    """Class for implementing cellular automaton grid simulations.

    Provides a framework for implementing 2D cellular automaton (CA) simulations using numpy arrays.
    Each instance of the class has a numpy array for the cell data.  The class automatically creates
    boundary cells surrounding the simulation grid.  I also creates views into the simulation grid
    for use with numpy array operations for calculation.

    Since this class inherits numpy.ndarray, several unique approaches must be used (espicially for
    class instance creation.)  The document at
    https://docs.scipy.org/doc/numpy/user/basics.subclassing.html explains using ndarray as a
    subclass and these special approaches.

    Also important in the concept of an array view.  A view to an array does not use new data in
    memory, but simply 'views' the data which already exists.  Because of this efficiency, this class
    creates many views into the grid.  These views can be used later for efficient calculation through
    numpy calls rather than iterating over items through interpreted python code.

    The class methods are:

    __new__ -> class initialization method.
                The array or grid shape must be provided.  The constructor will not take data.
                It creates an array 2 bigger than the shape argument pass.  This is allows for boundary
                cells in each direction.  It then returns a numpy array for the main simulation data.
                This is actually a view into the data of the bigger array.  The bigger array is
                available through .Base or .base. It also creates view arrays for the neighbors to
                the top, top right, left, bottom left ...

     __array_finalize_ ->  Always called after initialization

     __init__ -> is not used since it is not always called for subclasses of ndarray.

     Update -> This implements the rules of the
     SetValue
     SetBoundary

    """

    def __new__(cls,shape, *args, **kwargs):

        if 'buffer' in kwargs:
            raise TypeError("buffer not allowed in constructor.  Initilize grid after constructor.")
            #Taking a buffer requires COPPYING the data instead of using the already existing memory location.
            #This could cause memory usage problems.
            #The data has to be coppied because the Base array which handles boundary conditions is larger than
            # the real cells.
            #If we did want to try and take a buffer, the code below would probably be needed as well as a
            # copying the data to the new array after it has been created, copyto(ni, buffer).
            #databuffer= kwargs['buffer']
            #del kwargs['buffer']
            #print('Buffer values will be used, but not the memory locations')
        BaseShape = tuple([d+2 for d in shape])

        Base = numpy.ndarray.__new__(cls, BaseShape,*args, **kwargs)

        #ni stands for new instance.  It is the object this __new__ will return
        ni = Base[1:BaseShape[0]-1,1:BaseShape[1]-1]                 #ni.Base might not be needed since this
        ni.Base        = Base                                        # is already defined as base by numpy
        #Create views for the neighbors in each direction.
        ni.NTopLeft     = Base[0:BaseShape[0]-2, 0:BaseShape[1]-2]
        ni.NTop         = Base[0:BaseShape[0]-2, 1:BaseShape[1]-1]
        ni.NTopRight    = Base[0:BaseShape[0]-2, 2:BaseShape[1]]
        ni.NLeft        = Base[1:BaseShape[0]-1, 0:BaseShape[1]-2]
        ni.NRight       = Base[1:BaseShape[0]-1, 2:BaseShape[1]]
        ni.NBottomLeft  = Base[2:BaseShape[0],   0:BaseShape[1]-2]
        ni.NBottom      = Base[2:BaseShape[0],   1:BaseShape[1]-1]
        ni.NBottomRight = Base[2:BaseShape[0],   2:BaseShape[1]]
        ni.Neighbors    = [ni.NTop,    ni.NTopRight,   ni.NRight, ni.NBottomRight,
                           ni.NBottom, ni.NBottomLeft, ni.NLeft,  ni.NTopLeft]
        #Create views for the grid boundaries.
        ni.TopRow       = Base[1:2,                           1:BaseShape[1]-1]
        ni.BottomRow    = Base[BaseShape[0]-2:BaseShape[0]-1, 1:BaseShape[1]-1]
        ni.LeftColumn   = Base[1:BaseShape[0]-1,              1:2]
        ni.RightColumn  = Base[1:BaseShape[0]-1,              BaseShape[1]-2:BaseShape[1]-1]
        ni.BTopRow      = Base[0:1,                           1:BaseShape[1]-1]
        ni.BBottomRow   = Base[BaseShape[0]-1:BaseShape[0],   1:BaseShape[1]-1]
        ni.BLeftColumn  = Base[1:BaseShape[0]-1,              0:1]
        ni.BRightColumn = Base[1:BaseShape[0]-1,              BaseShape[1]-1:BaseShape[1]]

        OldBase = Base.copy()
        Old     = OldBase[1:BaseShape[0]-1,1:BaseShape[1]-1]
        Old.Base        = OldBase
        Old.NTopLeft     = Old.Base[0:BaseShape[0]-2, 0:BaseShape[1]-2]
        Old.NTop         = Old.Base[0:BaseShape[0]-2, 1:BaseShape[1]-1]
        Old.NTopRight    = Old.Base[0:BaseShape[0]-2, 2:BaseShape[1]]
        Old.NLeft        = Old.Base[1:BaseShape[0]-1, 0:BaseShape[1]-2]
        Old.NRight       = Old.Base[1:BaseShape[0]-1, 2:BaseShape[1]]
        Old.NBottomLeft  = Old.Base[2:BaseShape[0],   0:BaseShape[1]-2]
        Old.NBottom      = Old.Base[2:BaseShape[0],   1:BaseShape[1]-1]
        Old.NBottomRight = Old.Base[2:BaseShape[0],   2:BaseShape[1]]
        Old.Neighbors   = [Old.NTop, Old.NTopRight, Old.NRight, Old.NBottomRight,
                           Old.NBottom, Old.NBottomLeft, Old.NLeft, Old.NTopLeft]
        ni.Old       = Old
        ni.TrueArray = numpy.full(ni.shape,True,dtype=numpy.dtype('b'))
        ni.count     = numpy.zeros(ni.shape)
        ni.UpdateCount = 0

        return ni


    def __array_finalize_(self, obj):
        print('in _array_finalize')

    def Update(self):
        """Implements a single time step using Game of Life Rules

        def update(self)
        Method currently takes no arguments.

        Method sums the 'Value' of the neighbor cells and then applies the game of life rules.
        Method uses array operations for calculations rather than iterators so that we take
            full advantage of underlying C and Blas routines rather than slower Python code.

        Method also updates the boundary cells after the update to the main grid.
        """


        #Determine number of neighbors
        numpy.place(self.count,self.TrueArray,0)
        for n in self.Neighbors:
            self.count = self.count + n['Value']

        #Implement Game of Life Rules  (Note: self.Old is actually not needed for Game of Life.  Probably not for others as well.)
        numpy.copyto(self.Old,self)                #Default is no change for count = 2
        numpy.place(self['State'],self.count>3,False)   #If count > 3: new value = False
        numpy.place(self['State'],self.count==3,True)   #If count = 3: new value = True
        numpy.place(self['State'],self.count<2,False)   #if count < 2: new value = False
        self.SetValue()
        self.SetBoundary()

        self.UpdateCount +=1


    def SetBoundary(self):
        """Method copies array items from the data grid cells to the surrounding boundary condition cells.

            def setboundary(self):"""

        # copy the rows and columns.  These are views into the base created in __new__
        numpy.copyto(self.BBottomRow, self.TopRow)
        numpy.copyto(self.BLeftColumn, self.RightColumn)
        numpy.copyto(self.BTopRow, self.BottomRow)
        numpy.copyto(self.BRightColumn, self.LeftColumn)

        # copy the corners
        self.Base[0][0] = self[self.shape[0] - 1][self.shape[1] - 1]  # Set Top Left Corner
        self.Base[0][self.Base.shape[1] - 1] = self[self.shape[0] - 1][0]  # Set Top    Right Corner
        self.Base[self.Base.shape[0] - 1][self.Base.shape[1] - 1] = self[0][0]  # Set Bottom Right Corner
        self.Base[self.Base.shape[0] - 1][0] = self[0][self.shape[1] - 1]  # Set Bottom Left Corner

    def SetValue(self):
        numpy.copyto(self['Value'],self['State'])


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

