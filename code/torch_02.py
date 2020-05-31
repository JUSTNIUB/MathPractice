import torch

#自动求导 , 求导是针对某一点而言，而非某个函数而言
a = torch.tensor([3.0],requires_grad=True)
b = a**2+10

# b.backward()
# print(a.grad)
print(torch.autograd.grad(b,a))