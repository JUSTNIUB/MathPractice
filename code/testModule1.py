#模块导入
import torch
from torch import optim
import matplotlib.pyplot as plt


#定义类
class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()
        #定义网络参数 并初始化
        self.w = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))
    #推理过程
    def forward(self,x):
        return self.w*x+self.b


#定义一组张量数据
tensorX = torch.arange(0,1,0.01)
tensorY = tensorX*3+5+torch.rand(100)

if __name__ == '__main__':
    #实例化网络对象
    line = Line()
    #定义优化器
    #opt = optim.SGD(line.parameters(),lr=0.1)
    opt = optim.Adam(line.parameters(), lr=0.1)
    plt.ion()
    for num in range(60):
        for _x,_y in zip(tensorX,tensorY):
            #推导
            z = line(_x)
            #获得loss
            loss = (z-_y)**2

            #优化参数
            #清空梯度
            opt.zero_grad()
            #求导
            loss.backward()
            #更新参数
            opt.step()

            print(line.w.item(),line.b.item(),loss.item())
            plt.cla()
            v = [e*line.w+line.b for e in tensorX]
            plt.plot(tensorX,tensorY,'.')
            plt.plot(tensorX,v)
            plt.pause(0.01)
    plt.ioff()
    plt.show()
