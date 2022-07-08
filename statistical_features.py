import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

class Features:
    """
    Class containing methods that return statistical features of the data
    data : (arr) array of the data that need to get statistical features from
    """
    def __init__(self, data) -> None:
        self.data = data
    def get_skewness(self, bias=False):
        """
        Parameters
        ----------
        bias : (bool), whether bias is included in skewness
        
        Returns
        -------
        skewness value in float
        """
        return ss.skew(self.data, bias=bias)
    def get_kurtosis(self, bias=False):
        """
        Parameters
        ----------
        bias : (bool) whether bias is included in kurtosis
        
        Returns
        -------
        Kurtosis value in float
        """
        return ss.kurtosis(self.data, bias=bias)
    def summarize(self):
        """
        Returns
        -------
        Print all summary statistics of the data passed to __init__ function
        Summary statistics include: mean, median, standard deviation, mode, range, skewness, and kurtosis
        """
        mean = np.average(self.data)
        median = np.median(self.data)
        sd = np.std(self.data)
        mode = ss.mode(self.data)
        range = np.max(self.data) - np.min(self.data)
        print('Mean: ' + str(mean) + '\n' +
              'Median: ' + str(median) + '\n' +
              'Mode: ' + str(mode) + '\n' +
              'Range: ' + str(range) + '\n' +
              "Standard Deviation: " + str(sd) + '\n' +
              'Skewness: ' + str(self.get_skewness()) + '\n' +
              'Kurtosis: ' + str(self.get_kurtosis()) + '\n')
