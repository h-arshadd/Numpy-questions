import numpy as np
array=np.arange(1,11)
mask=(array%2==0)
filtered=array[mask]
double=array*2
print(array)
print(filtered)
print(double)