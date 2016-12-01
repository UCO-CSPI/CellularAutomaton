from FireSimulation import *

Rows=3
Columns=3
MyDtype = numpy.dtype([('Tree', bool), ('Burning', bool), ('ProbImmune', 'f'), ('Value', 'f', (3,))])
FireGrid.IncludeDiagonalNeighbors = False
MyGrid = FireGrid((Rows, Columns), MyDtype)
#initilize Grid
for y in range(Rows):
    for x in range(Columns):
        MyGrid['ProbImmune'][y][x]  = random() * 4
        if random() < 0.75:
            MyGrid['Tree'][y][x]    = True
            MyGrid['Burning'][y][x] = random() < 0.25
        else:
            MyGrid['Tree'][y][x]    = False
            MyGrid['Burning'][y][x] = False

MyGrid.SetValue()
MyGrid.SetBoundary()
print(MyGrid['Value'])
MyFigure, MyAxes = plt.subplots(1,1)
MyAxes.imshow(MyGrid['Value'])
MyFigure
print('starting update')
MyGrid.Update()
print('after update')
print(MyGrid['Value'])

