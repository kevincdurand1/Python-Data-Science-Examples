#Binarization

#Binarization is used when you want to convert your numerical feature vector into a Boolean vector. 
#Add the following lines to the Python file:

import numpy as np 
from sklearn import preprocessing

data = np.array([[3, -1.5, 2, -5.4], 
                 [0,4,-0.3, 2.1], 
                 [1,3.3, -1.9, -4.3]])

data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data) 
print ("\nBinarized data =", data_binarized)