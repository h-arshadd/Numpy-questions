import numpy as np
array=np.random.randint(0,100,size=(6,5))
mask = np.any(array < 10, axis=1)
print("Mask of failed students:", mask)
passed_students = array[~mask]
print("Passed students:\n", passed_students)
averages = np.mean(passed_students, axis=1)
print("Averages of passed students:", averages)

