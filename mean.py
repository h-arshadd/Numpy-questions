import numpy as np
array=np.random.randint(-10,10,size=(5,5))
print(array)
array = np.where(array < 0, 0, array)
print(array)
mean=np.mean(array,axis=0)
mask=mean>2
filtered=array[:,mask]
print(filtered)

