from CellularAutomaton import *

import numpy

MyGrid = CAGrid((3,3),dtype=[('State', 'bool_')])
print(MyGrid)

print('Setting to zeros_like')
MyGrid['State']=numpy.zeros_like(MyGrid['State'])
print(MyGrid)
print(MyGrid[0][0])

MyDType = numpy.dtype([('State', 'bool_'), ('cell', cell)])
print(MyDType)
print(repr(MyDType))

MyGrid = CAGrid((3,3), dtype=MyDType)
print(MyGrid)

MyCells = MyGrid['cell']

MyCells[0][0] = cell()


print(MyGrid['cell'][0][0].state)