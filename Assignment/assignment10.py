import numpy as np
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr = np.nan_to_num(arr)
arr = arr.T
print(arr)

arr = np.zeros((2, 3, 4))
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr.shape)

arr = np.array([[1, np.nan, 3], [4, 5, np.nan], [7, 8, 9]])
col_mean = np.nanmean(arr, axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col_mean, inds[1])
print(arr)

arr = np.array([[5, -1], [-9, 3]])
arr[arr < 0] = 0
print(arr)

import numpy as np
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
avg = (arr1 + arr2) / 2
print(avg)

import numpy as np
from scipy import stats

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np.mean(arr))
print(np.median(arr))
print(stats.mode(arr, axis=None).mode[0])

import numpy as np

A = np.array([[1, -2, 3],
              [-1, 3, -2],
              [2, -5, 5]])
B = np.array([9, 6, 17])

x = np.linalg.solve(A, B)
print(x)

import matplotlib.pyplot as plt
import numpy as np

sem1 = [80, 75, 90, 85, 70]
sem2 = [78, 82, 88, 79, 75]
subjects = ['Math', 'Sci', 'Eng', 'CS', 'PE']

x = np.arange(len(subjects))
plt.bar(x - 0.2, sem1, width=0.4, label='Sem 1')
plt.bar(x + 0.2, sem2, width=0.4, label='Sem 2')
plt.xticks(x, subjects)
plt.legend()
plt.show()
