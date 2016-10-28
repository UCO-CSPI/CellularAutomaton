import numpy
class cell:
    #InitialState = False
    #DefaultState = False


    def __init__(self, state=None, Neighbors=None):
        if state is None:
            if numpy.random.randint(2) == 1:
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

    def __str__(self):
        return self.value.__str__()

    def update(self):
        c=0
        for n in self.Neighbors:
            if n.state:
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

rows = 10
columns = 10
grid=[[cell() for x in range(columns)] for y in range(rows)]

print(grid[1][5])
for c in grid[1]:
    print(c)