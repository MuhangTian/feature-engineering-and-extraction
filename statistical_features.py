import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

class Features:
    def __init__(self, data) -> None:
        self.data = data
    def get_skewness(self, bias=False):
        return ss.skew(self.data, bias=bias)
    def get_kurtosis(self, bias=False):
        return ss.kurtosis(self.data, bias=bias)
    def summarize(self):
        mean = np.average(self.data)
        median = np.median(self.data)
        sd = np.std(self.data)
        print('Mean: ' + str(mean) + '\n' +
              'Median: ' + str(median) + '\n' +
              "Standard Deviation: " + str(sd) + '\n' +
              'Skewness: ' + str(self.get_skewness()) + '\n' +
              'Kurtosis: ' + str(self.get_kurtosis()) + '\n')
        
'''An example with random data stored in an array (write another function to achieve this later?)'''     
arr = np.random.rand(40) 
data = Features(arr)
print(data.get_kurtosis())
print(data.get_skewness())
data.summarize()
