#分类问题
import numpy as np
import torch
from torch import optim
import matplotlib.pyplot as plt
import random

#造两堆数据
#1.使用激活函数效果确实会好很多
#2.这里的输出是概率值，1代表 在线的上方 0代表在线的下方  模型拟合的函数反映了 x,y 和 标签的关系
#3.为什么这里画直线时使用 w1x1 + w2x2 + b = 0也能拟合的很好？ 因为带入进 sigmoid(0) = 0.5 刚刚好是中间的分界点，
#  一般来讲，在这条线上的点有一半概率是1 一半概率是0，正好用来做 分界线。
#4.这里只有一个神经元，其模型是(2,1) 即输入两个特征(x,y)，输出一个特征(0或者1)
#5.总结：画图使用的不熟练

trainData = [[x,torch.rand(1)*2-1] for x in torch.arange(0,1,0.0005)]



def jud(x):
    return -2*x+1

for onepot in trainData:
    if onepot[1]<jud(onepot[0]):
        onepot.append(torch.tensor(0))
    else:
        onepot.append(torch.tensor(1))

random.shuffle(trainData)
print(trainData)
# plt.plot([x[0] for x in trainData if x[2]==torch.tensor(0)],[x[1] for x in trainData if x[2]==torch.tensor(0)],'.')
# plt.plot([x[0] for x in trainData if x[2]==torch.tensor(1)],[x[1] for x in trainData if x[2]==torch.tensor(1)],'.')
# plt.show()

# xs = torch.arange(0,1,0.01)
# ys = xs*3+4+torch.rand(xs.shape[0])/10
#

class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = torch.nn.Parameter(torch.rand(1))
        self.w2 = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))

    def forward(self,x1,x2):
        #return (self.w1*x1+self.w2*x2+self.b) #不加效果会很差
        return torch.sigmoid(self.w1 * x1 + self.w2 * x2 + self.b)#加了效果会很好
if __name__ == "__main__":
    line = Line()
    #opt = optim.SGD(line.parameters(),lr=0.1)
    opt = optim.Adam(line.parameters(), lr=0.1)
    # plt.ion()
    for equam in range(60):
        for data in trainData:
            z = line(data[0],data[1])
            loss = (z-data[2])**2

            opt.zero_grad()
            loss.backward()
            opt.step()
            print(line.w1.item(), line.w2.item(), loss.item())
            # v = [line.w1*e[0]+line.w2*e[1]+line.b for e in trainData]
        plt.cla()
        plt.plot([x[0] for x in trainData if x[2] == torch.tensor(0)],
                 [x[1] for x in trainData if x[2] == torch.tensor(0)], '.')
        plt.plot([x[0] for x in trainData if x[2] == torch.tensor(1)],
                 [x[1] for x in trainData if x[2] == torch.tensor(1)], '.')
        plt.plot([x[0] for x in trainData],
                 [-(x[0] * line.w1.item() + line.b.item() - 0) / line.w2.item() for x in trainData])
        plt.title(loss.item())
        plt.pause(0.01)


    plt.ioff()
    plt.show()
# plt.plot([x[0] for x in trainData if x[2]==torch.tensor(0)],[x[1] for x in trainData if x[2]==torch.tensor(0)],'.')
# plt.plot([x[0] for x in trainData if x[2]==torch.tensor(1)],[x[1] for x in trainData if x[2]==torch.tensor(1)],'.')
# plt.plot([x[0] for x in trainData],[-(x[0]*line.w1.item()+line.b.item()-0.5)/line.w2.item()  for x in trainData])
# plt.show()