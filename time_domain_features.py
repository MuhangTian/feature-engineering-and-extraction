from math import sqrt
from sklearn.metrics import mean_squared_error
import numpy as np

class time_domain_features():
    def __init__(self, data) -> None:
        self.data = data
        
    def root_mean_squared(self):
        sum = np.sum(np.square(self.data))
        rms = sqrt(sum/len(self.data))
        return rms

    
'''Example'''
arr = np.random.rand(10)
features = time_domain_features(arr)
print(features.root_mean_squared())