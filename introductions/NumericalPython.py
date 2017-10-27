'''
Created on Sep 13, 2017

@author: maximilianscherer
'''

import numpy as np

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])                    #Creates a copy of the data by default
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], copy = False)      #Does not create a copy of the data
x = np.asarray([[1, 2, 3, 4], [5, 6, 7, 8]])                  #Does not create a copy of the data

x.ndim # Number of axes

x.shape # Shape of the array

x.dtype # Data type of the array (int/float/double))

print(x)

y = np.array([1, 2, 3, 4])

y * y       # Element wise

y.dot(y)    # Matrix product
np.dot(y, y)# Equal to previous