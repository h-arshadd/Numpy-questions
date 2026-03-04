import numpy as np

marks = np.array([
    [78, 85, 90, 88],
    [45, 50, 40, 48],
    [92, 88, 84, 91],
    [60, 65, 58, 62],
    [30, 35, 25, 20],
    [80, 82, 79, 85]
])

avg=np.mean(marks,axis=0)
mask = avg > 70
selected_students = marks[mask]

