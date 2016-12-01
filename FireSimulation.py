from CellularAutomaton import *
from random import random
import matplotlib
from matplotlib import pyplot as plt


class FireGrid(CAGrid):
    """This class derives from CAGrid and changes update to make this a first simulation"""

    def Update(self):
        """Update rules for a simple fire simulation"""


        print('in set value')
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                if self['Tree'][y][x]:
                    if self['Burning'][y][x]:
                        self['Tree'][y][x] = False

                elif self['Tree'][y][x]:
                    self['Value'][y][x] = (0, 0, 1)
                else:
                    self['Value'][y][x] = (1, 1, 1)

    def SetValue(self):
        print('in set value')
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                if self['Burning'][y][x]:
                    self['Value'][y][x]=(1,0,0)
                elif self['Tree'][y][x]:
                    self['Value'][y][x]=(0,0,1)
                else:
                    self['Value'][y][x]=(1,1,1)
