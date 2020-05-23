#torch 训练的基本模型
import torch
from torch import optim
import matplotlib.pyplot as plt

#定义张量 xs ys
xs = torch.arange(0,1,0.01)
ys = xs*4+5+torch.rand(100)#要查下rand的用途

class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()
        #定义模型的参数
        self.w = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))

    def forward(self,x):
        return self.w*x+self.b

if __name__ == "__main__":
    #定义一个模型
    line = Line()
    #定义一个优化器
    opt = optim.SGD(line.parameters(),lr=0.1)
    #开始绘画功能
    plt.ion()

    for equm in range(60):
        for _x,_y in zip(xs,ys):
            z = line(_x)
            loss = (z-_y)**2
            #优化器
            opt.zero_grad()# why we need it ???
            loss.backward()# ???
            opt.step()     # ???
            v = [line.w*e+line.b for e in xs]
            plt.cla()
            plt.plot(xs, ys, '.')
            plt.plot(xs,v)
            plt.pause(0.01)

    plt.ioff()
    plt.show()



