import torch
import numpy

#torch操作
a = torch.tensor([1.,2.])
print(a)
b = torch.arange(0.1,10,0.1)
print(b)
print(b.shape)
c = numpy.array([3,4,5,6,7])

#互相转换 numpy->torch
d = torch.from_numpy(c)
print(d)
e = d.numpy()
print(e)