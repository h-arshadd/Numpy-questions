import numpy as np

scores = np.array([
    [85, 92, 78, 90],
    [70, 65, 88, 72],
    [95, 89, 92, 97],
    [60, 74, 55, 68],
    [88, 91, 85, 93]
])

# Rows = Students (S1 to S5)
# Columns = Subjects (Math, English, Science, History)
# Average score of each student
average_scores=np.mean(scores, axis=1)
print(average_scores)
# Highest score in each subject
highest_scores=np.max(scores, axis=0)
print(highest_scores)
# Average score above 80
above_eighty= average_scores[average_scores>80]
print(above_eighty)
# Replace all scores below 65 with 0
scores[scores < 65] = 0
print(scores)
# Normalize the scores 
normalized_global=((scores-np.min(scores))/(np.max(scores)-np.min(scores)))
print(normalized_global)