#Scaling

#The values of each feature in a datapoint can vary between random values. 
#So, sometimes it is important to scale them so that this becomes a level playing field. 
#Add the following lines to the file and run the code:

import numpy as np 
from sklearn import preprocessing

data = np.array([[3, -1.5, 2, -5.4], 
                 [0,4,-0.3, 2.1], 
                 [1,3.3, -1.9, -4.3]])

data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1)) 
data_scaled = data_scaler.fit_transform(data) 
print("\nMin max scaled data =", data_scaled)