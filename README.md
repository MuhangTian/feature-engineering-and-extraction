# Feature Engineering and Extraction Module Tutorial
## Statistical Features
1. User passes an array (or numpy array) of data from pre-process module into Features() class
2. call functions in Features() class to get summary statistics
3. For instance, suppose the array of data is stored as *arr*, then to get all relavant summary statistics (like mean, median, mode...etc), simply call Features(*arr*).summarize()

## Time Domain Features
1. root_mean_square(): Calculate root mean squared value of an array of data
2. energy(): calculate energy of a time domain data over a given interval, passed as an array of data
3. average_power(): calculate the average power of an array of data over a given interval

