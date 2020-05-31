import numpy as np

#numpy操作 形状变换
a = np.array([3,4,5,6])

print(a.reshape(2,2))
print(a.reshape(2,2).T)