#Normalization

#Data normalization is used when you want to adjust the values in the feature vector 
#so that they can be measured on a common scale. One of the most common forms of normalization 
#that is used in machine learning adjusts the values of a feature vector so that they sum up to 1. 
#Add the following lines to the previous file:

import numpy as np 
from sklearn import preprocessing

data = np.array([[3, -1.5, 2, -5.4], 
                 [0,4,-0.3, 2.1], 
                 [1,3.3, -1.9, -4.3]])

data_normalized = preprocessing.normalize(data, norm='l1') 
print ("\nL1 normalized data =", data_normalized)