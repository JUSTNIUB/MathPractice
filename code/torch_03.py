import torch

#矩阵运算 加减乘除 叉乘 转置
a = torch.tensor([[1.,2.],[3.,4.],[5.,6.]])
b = torch.tensor([[8.,2.],[3.,4.],[5.,10.]])
c = torch.tensor([[1.,2.],[3.,4.]])
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