import numpy as np
array=np.random.randint(0,50,size=(6,6))
print(array)
mod_arr=np.where(array>30,-1,array)
print(mod_arr)
mean_arr=np.mean(mod_arr,axis=0)
mask=mean_arr>10
filtered=mod_arr[:,mask]
print(filtered)
