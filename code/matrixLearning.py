#矩阵乘法
import torch
a = torch.tensor([[1,2],[3,4],[5,6]])
b = torch.tensor([[5,6],[7,8],[9,10]])
c = torch.tensor([[1,2],[3,4]])
d = torch.tensor([1,2,3])
e = torch.tensor([3,4,5])

print(a+b)
print(a-b)
print(a*b)
print(3*a)
print(3+a)
print(a)
print(c)
print(a@c)
print(torch.matmul(a,c))

print(a)
print(a.t())

#查看矩阵形状
a = torch.tensor([[[1,2,1],[1,4,5]],[[1,2,3],[4,2,1]]])
b = torch.tensor([[[1],[3],[5]],[[2],[4],[7]]])
print(a.shape)
print(b.shape)

#改变形状
a = torch.tensor([1,2,3,4,5,6])
print(a.shape)
b = a.reshape(3,2,1)
print(b)
print(b.reshape(2,3))
print(b.reshape(1,6))