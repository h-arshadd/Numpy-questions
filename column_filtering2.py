import numpy as np
array=np.random.randint(-10,20,size=(6,6))
print(array)
mean_arr=np.mean(array,axis=0)
print(mean_arr)
mask=mean_arr>5
filtered=array[:,mask]
print(filtered)

