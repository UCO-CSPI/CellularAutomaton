<h1>Assignment</h1>
For this assignment:
+ Fork This Repository
+ Create a new branch based on your name
+ By inheriting one of the classes in this repository, recreate a simulation simular to that shown in figure 10.3.3.  The setup of this problem is described in in the text, especially the paragraph before the exercises.
+ Turn in your assignment and ask questions by creating a <a href = https://help.github.com/articles/about-pull-requests/>pull request</a>.

NOTES/Hints:
+ For the plotting to work using the CAGrid class, there is a change to the CAGrid test code you need to make.  A good way of getting matplotlib to plot good colors for tree, empty and burning is to give a tuple of RGB values at each grid location.  This has several required changes.
    + To do this, you can set the 'value' field to a touple.  This requires specifing the numpydtype to contain 3 floats rather than one.  My code for the dtype is `MyDtype = numpy.dtype([('Tree', bool), ('Burning', bool), ('ProbImmune', 'f'), ('Value', 'f', (3,))]).`  The relevent part is `('Value', 'f', (3,))` in which the "(3,)" indicates there are thee floats rather than just one.
    + My code for setting the values is below.  I put this as a method of my FireGrid class.  The method below is overloading the underlying CAGrid method.
    
      ```python
      def SetValue(self):
          for y in range(self.shape[0]):
              for x in range(self.shape[1]):
                  if self['Burning'][y][x]:
                      self['Value'][y][x]=(1,0,0)
                  elif self['Tree'][y][x]:
                      self['Value'][y][x]=(0,.75,0)
                  else:
                      self['Value'][y][x]=(.34,.231,.05)
        ```
    + The tuples cause matplotlib.matshow to fail.  The code ```MyAxes.matshow(MyGrid['Value'])``` returns an error.  Instead, use ```MyAxes.imshow(MyGrid['Value'],interpolation='nearest')```
