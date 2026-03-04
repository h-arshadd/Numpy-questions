import numpy as np
array=np.random.randint(0,50,size=(5,5))
col_sum=np.sum(array, axis=0)
mask=col_sum>100
filtered=array[:,mask]
print(array)
print(col_sum)
print(filtered)