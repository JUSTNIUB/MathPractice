#梯度下降法
import random
import matplotlib.pyplot as plt

_x = [i/100 for i in range(100)]
_y = [i*3+4+random.random() for i in _x]

w = random.random()
b = random.random()
for a in range(100):
    for x,y in zip(_x,_y):
        z = w*x+b
        o = z-y
        loss = o**2

        p = -2*o*x
        pb = -2*o

        w = 0.01*p+w    #梯度下降法 找到loss的最低点，通过求导得知当前函数是单调增加还是减少的。
        b = 0.01*pb+b   #这里的方法就是让w变化,斜率要带上负号
        print(f"w={w};b={b};loss={loss}")

plt.plot(_x,_y,".")

plt.plot(_x,[w*i+b for i in _x])
plt.show()

