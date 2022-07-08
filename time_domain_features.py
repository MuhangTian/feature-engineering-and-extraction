from math import sqrt
from sklearn.metrics import mean_squared_error

import numpy as np
import scipy.stats as ss

def root_mean_square(data):
    """
    Calculates root mean squared value of a given data
    
    Parameters
    ----------
    data : array_like
        array of data to get root mean squared value from
        
    Returns:
    -------
    rms : float
        root mean squared value of the data
    """
    data = np.square(data)
    rms = sqrt(np.mean(data))
    return rms

def energy(data):
    """
    Calculate energy of a data set over a time domain
    
    Parameters
    ----------
    data : (array like)
        array of data need to get energy from
    
    Returns
    -------
    energy : float
        energy of time domain data
    """
    data = np.sum(np.square(np.abs(data)))
    return data

def average_power(data):
    """Function that calculates average power of an array of data

    Parameters
    ----------
        data (array like): array of data of interest, to evaluate average power

    Returns
    -------
        float: numerical value of average power
    """
    num = len(data)
    data = energy(data)
    avg_power = data/num
    return avg_power