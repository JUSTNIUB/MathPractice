import numpy as np
#矩阵基本操作,造矩阵，矩阵运算

#对角阵
a = np.diag([1,2,3,4])
print(a)
#单位矩阵
a = np.eye(4,4)
print(a)
#下三角矩阵
a = np.tri(3,3)
print(a)
#0 1 矩阵
a = np.zeros((3,4))
print(a)
a = np.ones((3,4))
print(a)

b = np.array([1,2])
a = np.array([3,4])
print(np.sum(a*b))#求矩阵元素和
print(a*b)


