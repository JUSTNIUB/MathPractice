#学习numpy和torch操作文件
import numpy as np
import torch
import matplotlib.pyplot as plt

#用torch 和 numpy定义一个变量
a = torch.tensor([[1,2],[3,4]])
print(a,type(a))
b = np.array([[2,3],[1,4]])
print(b,type(b))
# b = numpy.ndarray([1,2])#注意ndarray 和 array不同
# print(b,type(b))


#numpy类型和torch类型相互转换
e = a.numpy()
print(e,type(e))
f = torch.from_numpy(b)
print(f,type(f))

#画图
x = np.arange(-1,1,0.1)
y = x**2
y1 = np.tile(np.array([3]),x.shape)
#log 造0框架
x1 = np.arange(0.1,10,0.1)
y2 = np.log(x1)
y3 = np.zeros_like(x1)
y4 = np.log(x1)/np.log(np.array([0.5]))#换底公式 :计算机中的log底数默认都是10


# plt.plot(x,y)
# plt.plot(x,y1)
# plt.plot(x1,y2)
# plt.plot(x1,y3)
# plt.plot(x1,y4)

#sidmod 函数
# testExp_x = np.arange(-100,100,0.1)
# testExp_y = 1/(1+np.exp(-testExp_x))
# testExp_y1 = (np.exp(testExp_x)-np.exp(-testExp_x))/(np.exp(testExp_x)+np.exp(-testExp_x))
# plt.plot(testExp_x,testExp_y)
# plt.plot(testExp_x,testExp_y1)
# plt.show()

#求导t
testGradx = torch.tensor(3.0,requires_grad=True)
testGrady = 3**testGradx.log()+testGradx
#way1
# testGrady.backward()
print(testGradx,testGradx.log())
print("求导2：",torch.autograd.grad(testGrady,testGradx))