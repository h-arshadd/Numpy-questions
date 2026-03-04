import numpy as np
array=np.random.randint(1,20,size=(5,5))
print(array)
array = np.where(array % 2 == 0, 0, array)
print(array)
zero_counts = np.sum(array == 0, axis=1)
print(zero_counts)
row_index = np.argmax(zero_counts)
print(row_index)