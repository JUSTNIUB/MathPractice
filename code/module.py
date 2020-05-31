#神经网络模型:直线拟合问题
import torch
from torch import optim
import matplotlib.pyplot as plt

class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()
        #设置参数
        self.m = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))
        return
    def forward(self,x):
        #返回推理结果 前向结果 得到预期输出
        return x*self.m+self.b

#训练数据
xs = torch.arange(0,1,0.01)
ys = xs*3+4+torch.rand(100)/10

if __name__ == '__main__':
    #创建一个神经网络
    line = Line()
    #创建一个优化器
    opt  = optim.SGD(line.parameters(),lr=0.1)

    plt.ion()

    for equot in range(60):
        for _x,_y in zip(xs,ys):
            #推理
            z = line(_x)

            #获得损失
            loss = (z-_y)**2
            #优化 : bp算法 梯度下降法
            opt.zero_grad()
            loss.backward()
            opt.step()

            plt.cla()
            plt.plot(xs,[e*line.m+line.b for e in xs])
            plt.plot(xs,ys,'.')
            plt.pause(0.01)

    plt.ioff()
    plt.show()