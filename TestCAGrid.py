from CellularAutomaton import *
import numpy as np

Rows = 1
Columns = 10
mydtype = np.dtype([('Value', 'i')])
#mydtype = np.dytpe('f')
#data = np.array([[0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11.], [10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20, 21],
#              [20., 21., 22., 23., 24., 25., 26., 27., 28., 29., 30, 31]])
#data = np.array([[ (1.,),  (2.,),  (3.,),  (4.,),  (5.,),  (6.,),  (7.,),  (8.,),  (9.,), (10.,)], \
#                [(11.,), (12.,), (13.,), (14.,), (15.,), (16.,), (17.,), (18.,), (19.,), (20.,)], \
#               [(21.,), (22.,), (23.,), (24.,), (25.,), (26.,), (27.,), (28.,), (29.,), (30.,)]], dtype=mydtype)
#x = CAGrid((3,10),mydtype, buffer=data)
x = CAGrid((3,10),mydtype)
print(type(x))

#for y in range(BaseShape[0]):
#     for x in range(BaseShape[1]):
#         Base['Value'][y][x] = 10*y + x + 100


mydtype = np.dtype([('Value', 'b')])
x = CAGrid((3,10),mydtype)
randvalue=np.random.random(x.shape)
np.place(x['Value'],randvalue>.5,True)


print(x)
print('\n')
x.update()
print(x)