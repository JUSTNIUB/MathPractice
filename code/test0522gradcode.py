#曲线拟合实验
import matplotlib.pyplot as plt
import random

#初始化数据集
xs = [i/100 for i in range(0,100)]

ys = [e*-3+4+random.random() for e in xs]

w = random.random()
b = random.random()
plt.ion()
#开始训练
for i in range(300):
    for _x,_y in zip(xs,ys):
        #推理
        h = w*_x + b
        o = h-_y
        #获得损失
        loss = o**2

        #学习优化
        dw = 2*o*_x
        db = 2*o
        w = w-0.01*dw
        b = b-0.01*db
        v = [e * w + b for e in xs]
        plt.cla()
        plt.plot(xs, ys, '.')
        plt.plot(xs, v)
        plt.pause(0.01)

plt.ioff()
plt.show()