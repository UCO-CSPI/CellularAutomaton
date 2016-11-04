from CellularAutomaton import *

class C(object):
    def __new__(cls, *args):
        print('Cls in __new__:', cls)
        print('Args in __new__:', args)
        return object.__new__(cls)

    def __init__(self, *args):
        print('type(self) in __init__:', type(self))
        print('Args in __init__:', args)


class D(C):
    def __new__(cls, *args):
        print('D cls is:', cls)
        print('D args in __new__:', args)
        return C.__new__(C, *args)

    def __init__(self, *args):
        # we never get here
        print('In D __init__')

c=C('hello from c')
print('\n')

obj = D('hello from d')
print('\n')
print('\n')


import numpy as np
Rows = 1
Columns = 10
mydtype = np.dtype([('Value', 'f')])
#mydtype = np.dytpe('f')
x = np.array([[0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11.], [10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20, 21],
              [20., 21., 22., 23., 24., 25., 26., 27., 28., 29., 30, 31]])
#data = np.array([[ (1.,),  (2.,),  (3.,),  (4.,),  (5.,),  (6.,),  (7.,),  (8.,),  (9.,), (10.,)], \
#                [(11.,), (12.,), (13.,), (14.,), (15.,), (16.,), (17.,), (18.,), (19.,), (20.,)], \
#               [(21.,), (22.,), (23.,), (24.,), (25.,), (26.,), (27.,), (28.,), (29.,), (30.,)]], dtype=mydtype)
#x = CAGrid((3,10),mydtype, buffer=data)
#x = CAGrid((3,10),mydtype)
print(type(x))
print(x[1:2, 1:Columns+1])

#x = np.recarray((Rows+2, Columns+2),dtype=[('Value', float)])
#for yy in range(Rows+2):
#    for xx in range(Columns+2):
#        x.Value[yy][xx] = 10*yy + xx
#repr(x)

#the acutal ellements with be items 1 - 10,  0 and 11 are for ofset

# print('x is')
print(x['Value'])
print(x.shape)
print(np.sin(x['Value']))

print(x)
print('right is')
right=x[0:2][1:8]
print(right)
right=x[0:3]
print('x[0:3]')
print(right)
right=x[0:3][1:9]
print('x[0:3][1:9]')
print(right)
print('The stuff below works **************')
right=x[0:3,2:12]
print('x[0:3, 2:12]')
print(right)
x[0]=[100,101,102,103,104,105,106,107,108,109,110,111]
print(x)
print(right)

print('left=x[0:3, 0:10]')
left=x[0:3, 0:10]
print(left)

print('top=x[0:1,1:11]')
top=x[0:1,1:11]
print(top)

print('bottom=x[1:2,1:11]')
bottom=x[2:3,1:11]
print(bottom)

print('\n \n \n')
Columns = 10
Rows = 1
LastColumn=Columns+1
LastRow = Rows+1

print('tl=x[0:LastRow-2,2:LastColumn-1]')
tl=x[0:LastRow-1,0:LastColumn-1]
print(tl)

print('top')
t=x[0:LastRow-1,1:LastColumn]
print(t)

print('tr=x[0:LastRow-2,2:LastColumn+1]')
tr=x[0:LastRow-1,2:LastColumn+1]
print(tr)

print('Right')
r=x[1:LastRow,2:LastColumn+1]
print(r)

print('Bottom Right')
br=x[2:LastRow+1,2:LastColumn+1]
print(br)

print('Bottom')
b=x[2:LastRow+1,1:LastColumn]
print(b)

print('Bottom Left')
bl=x[2:LastRow+1,0:LastColumn-1]
print(bl)

print('Left')
l=x[1:LastRow,0:LastColumn-1]
print(l)

x[1][LastColumn]=x[1][1]
print('x[1] is')
print(x[1])
print('right is')
print(r)
x[1][1]=3.14
print('x[1] is')
print(x[1])
print('right is')
print(r)
print(x.shape)
