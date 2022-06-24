from math import sqrt
from sklearn.metrics import mean_squared_error

import numpy as np
import scipy.stats as ss

def root_mean_square(data):
    sum = np.sum(np.square(data))
    rms = sqrt(sum/len(data))
    return rms

def 
    
'''Example'''
arr = np.random.rand(10)
features = time_domain_features(arr)
print(features.root_mean_squared())