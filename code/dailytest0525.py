#日常训练函数运用
import numpy as np
import torch

#求行列式
a = np.array([[1,2],[3,4]])
print(np.linalg.det(a))

b = torch.tensor([[1.,2.],[3.,4.]])
print(b.det())

#斜对角阵
a = np.diag([1,2,3,4])
print(a)
b = torch.diag(torch.tensor([1,2,3,4]))
print(b)

#单位矩阵
c = np.eye(3,4)
print(c)
d = torch.eye(3,3)
print(d)

#下三角矩阵
f = torch.tril(torch.ones(3,3))
print(f)
g = np.zeros((3,3))
print(g)
h = torch.zeros(3,3)
print(h)

#内积
a = np.array([1,2])
b = np.array([3,4])
print(np.sum(a*b))

#求特征向量和特征值
print('======特征向量和特征值求解=======')
a = torch.tensor([[1.,2.],[3.,4.]])
print(torch.eig(a))
print(torch.eig(a,eigenvectors=True))

