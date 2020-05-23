#numpy操作日常训练 ：log 平方 e 定义对象 形状查看 zero_likes like 求导等操作
import numpy as np
import torch
import matplotlib.pyplot as plt

x = np.arange(0,10,0.01)#具备 浮点能力
y = x**1.2+1+np.random.rand(x.shape[0])
z = np.zeros_like(x)

#numpy没有求导给它转成张量再求导,这里好像不能对序列求导，自动求导是个技术活
tx = torch.arange(0,1,0.1,requires_grad=True)
#tx= torch.tensor([3.0],requires_grad=True)
# h = torch.from_numpy(y)
# h = tx**2+1
# h[1].backward()
# print(tx[1].grad)



#plt.plot(x,y)
#plt.plot(x,np.log(y))
plt.plot(x,np.exp(x))
plt.plot(x,np.tile(np.array(10000),x.shape))
plt.plot(np.tile(np.array(0),x.shape),x*1000)



plt.plot(x,z)
plt.show()