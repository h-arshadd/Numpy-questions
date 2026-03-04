import numpy as np
array=np.random.randint(1,20,size=(7,7))
print(array)
np.fill_diagonal(array,0)
print(array)
row_max = np.max(array, axis=1)
print(row_max)
row_index = np.argmax(row_max)
print(row_index)