#矩阵测试:数加减，加减，点乘，数乘，叉乘，转置
import numpy as np
import torch
import matplotlib.pyplot as plt

a = torch.tensor([[1,2],[3,4],[5,6]])
b = torch.tensor([[5,6],[7,8],[9,10]])
c = torch.tensor([[1,2],[3,4]])
d = torch.tensor([1,2,3])
e = torch.tensor([3,4,5])

a = torch.tensor([[3,4,5,6,7],[1,2,3,4,9],[6,7,9,4,3]])
c = torch.tensor([6,4,3,2,1])

a = torch.tensor([[[2,2],[1,5]],[[1,2],[5,5]],[[6,2],[1,7]]])
c = torch.tensor([[5,1],[3,4]])
print(a.shape)
print(c.shape)

# #加减
# print(a+b)
# print(a-b)
# #点乘
# print(a*b)
# #数乘
# print(3*a)
# #数加
# print(3+a)
# print(a)
# print(c)
#叉乘
print((a@c).shape)
print(torch.matmul(a,c))

#转置
# print(a)
# print(a.t())