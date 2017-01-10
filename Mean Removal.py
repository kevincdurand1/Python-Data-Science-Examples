#Mean Removal

#It's usually beneficial to remove the mean from each feature so that it's centered on zero. 
#This helps us in removing any bias from the features. Add the following lines to the file that we opened earlier:

import numpy as np 
from sklearn import preprocessing

data = np.array([[3, -1.5, 2, -5.4], 
                 [0,4,-0.3, 2.1], 
                 [1,3.3, -1.9, -4.3]])

data_standardized = preprocessing.scale(data) 
print ("\nMean =", data_standardized.mean(axis=0) )
print ("Std deviation =", data_standardized.std(axis=0))