import numpy as np
array=np.random.randint(50,200,size=(7,5))
print(array)
total_sales=np.sum(array,axis=0)
print(total_sales)
highest_sales=np.argmax(total_sales)
print(highest_sales)
mask=np.any(array>180,axis=1)
print(mask)
