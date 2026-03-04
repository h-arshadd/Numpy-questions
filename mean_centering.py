import numpy as np
arr1=np.random.randint(1,20,size=(3,4))
print(arr1)
mean=np.mean(arr1, axis=1, keepdims=True)
normalized=arr1-mean
print(normalized)
