import torch
#torch操作 shape换形状等 求逆

a = torch.rand(1,2,2,1)
print(a)
a = a.permute(0,2,3,1)
a = torch.tensor([[1.,2.],[3.,4.]])
print(torch.inverse(a))