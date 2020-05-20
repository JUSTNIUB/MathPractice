#torch基本框架

#导入
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch import optim

#定义torch 张量
xs = torch.arange(0,1,0.01)
print(type(xs))
ys = xs*3+4+torch.rand(100)
print(ys)

class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()
        #模型初始化
        self.w = torch.nn.Parameter(torch.rand(1))#定义神经网络参数 初始值随机一个张量
        self.b = torch.nn.Parameter(torch.rand(1))#定义神经网络参数 Parameter集合了所有参数

    #前向推理过程
    def forward(self,x):
        return self.w*x + self.b

if __name__ == '__main__':
    #初始化一个网络模型
    line = Line()

    #定义优化器
    #opt = optim.SGD(line.parameters(),lr=0.1)
    opt = optim.Adam(line.parameters(),lr=0.1)
    plt.ion()#开始动态绘画
    for epoch in range(60):
        for _x,_y in zip(xs,ys):
            #前向推理
            z = line(_x)
            #获取损失
            loss = (z-_y)**2
            #求导
            #梯度清空
            opt.zero_grad()
            #自动求导
            loss.backward()

            #学习过程:优化过程
            opt.step()

            print(line.w.item(),line.b.item(),loss.item())
            plt.cla()
            plt.plot(xs,ys,".")
            v = [line.w*e+line.b for e in xs]
            plt.plot(xs,v)
            plt.pause(0.01)
    plt.ioff()
    plt.show()