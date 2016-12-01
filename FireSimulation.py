from CellularAutomaton import *
from random import random
import matplotlib
from matplotlib import pyplot as plt


class FireGrid(CAGrid):
    """This class derives from CAGrid and changes update to make this a first simulation"""


    def Update(self):
        """Update rules for a simple fire simulation"""


        #determine the number of neighbors on fire
        numpy.place(self.count,self.TrueArray,0)
        for n in self.Neighbors:
            self.count = self.count + n['Burning']

        #update to new values
        numpy.place(self['Tree'], self['Burning'], False)   # If Burning, new['Tree'] = False else keep old value
        self['Burning'] = numpy.zeros(self.shape)              # If Burning, new['Burning'] = False (it burned out)
        #if tree surrounded by fire then set burning, (If tree and count(neighbors burning) * ran > probImmune)
        numpy.place(self['Burning'], numpy.logical_and(
            self['Tree'],numpy.multiply(self.count,self.ran) > self['ProbImmune']), True)

        self.FinishUpdate()
        self.UpdateCount += 1




        #The for loop structure below is not complete.  I think it is OK down to seting trees on fire.
        # for y in range(self.shape[0]):
        #    for x in range(self.shape[1]):
        #        if self['Tree'][y][x]:
        #            if self['Burning'][y][x]:
        #                self['Tree'][y][x] = False
        #
        #        elif self['Tree'][y][x]:
        #            self['Value'][y][x] = (0, 0, 1)
        #        else:
        #            self['Value'][y][x] = (1, 1, 1)

    def SetValue(self):
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                if self['Burning'][y][x]:
                    self['Value'][y][x]=(1,0,0)
                elif self['Tree'][y][x]:
                    self['Value'][y][x]=(0,0,1)
                else:
                    self['Value'][y][x]=(1,1,1)
