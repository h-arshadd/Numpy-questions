import numpy as np
array = np.random.randint(0,20,size=(7,4))
print(array)
mean_arr=np.mean(array, axis=1)
std_arr=np.std(array, axis=1)
print(mean_arr)
print(std_arr)
mask = (mean_arr > 10) & (std_arr > 5)
filtered=array[mask,:]
print(filtered)