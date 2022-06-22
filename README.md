# Feature Engineering and Extraction Module Tutorial
## Statistical Features
1. User passes an array (or numpy array) of data from pre-process module into Features() class
2. call functions in Features() class to get summary statistics
3. For instance, suppose the array of data is stored as *arr*, then to get all relavant summary statistics (like mean, median, mode...etc), simply call Features(*arr*).summarize()
