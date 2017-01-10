#One Hot Encoding

#A lot of times, we deal with numerical values that are sparse and scattered all over the place. 
#We don't really need to store these big values. This is where One Hot Encoding comes into picture. 
#We can think of One Hot Encoding as a tool to tighten the feature vector. It looks at each feature and 
#identifies the total number of distinct values. It uses a one-of-k scheme to encode the values. 
#Each feature in the feature vector is encoded based on this. This helps us be more efficient in terms of space.

import numpy as np 
from sklearn import preprocessing

data = np.array([[3, -1.5, 2, -5.4], 
                 [0,4,-0.3, 2.1], 
                 [1,3.3, -1.9, -4.3]])

encoder = preprocessing.OneHotEncoder() 
encoder.fit([[0, 2, 1, 12], [1, 3, 5, 3], [2, 3, 2, 12], [1, 2, 4, 3]]) 
encoded_vector = encoder.transform([[2, 3, 5, 3]]).toarray() 
print ("\nEncoded vector =", encoded_vector)