Rows=3
Columns=3
MyDtype = numpy.dtype([('Tree', bool), ('Burning', bool), ('ProbImmune', 'f'), ('Value', 'f', (3,))])
MyGrid = FireGrid((Rows, Columns), MyDtype)
#initilize Grid
for y in range(Rows):
    for x in range(Columns):
        MyGrid['ProbImmune'][y][x]  = random()
        if random() < 0.75:
            MyGrid['Tree'][y][x]    = True
            MyGrid['Burning'][y][x] = random() < 0.1
        else:
            MyGrid['Tree'][y][x]    = False
            MyGrid['Burning'][y][x] = False

MyGrid.SetValue()
MyGrid.SetBoundary()
print(MyGrid['Value'])
print(MyGrid['Value'])
MyFigure, MyAxes = plt.subplots(1,1)
MyAxes.imshow(MyGrid['Value'])
MyFigure