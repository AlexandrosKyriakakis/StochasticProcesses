import numpy as np

mytable = np.array([
    [-1, 1/8, 3/8],
    [1/4, -1, 3/4],
    [1/5, 1/5, -4/5]
])
mysol = np.array([
    [0],
    [0],
    [-2/5]
])
mysol2 = np.array([-1/2,0,0])
print (np.linalg.inv(mytable).dot(mysol))
print(1-0.24390244)