import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

normalized_global=((arr-np.min(arr))/(np.max(arr)-np.min(arr)))
print(normalized_global)
sum=arr.sum (axis=1)
normalized_row = arr/sum
print(normalized_row)