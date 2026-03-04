import numpy as np
array=np.random.randint(-20,20,size=(6,4))
print(array)
total_mean=np.mean(array, axis=1)
print(total_mean)
mask=total_mean>0
filtered=array[mask,:]
filtered[filtered < 0] = 0
print(filtered)

