import numpy as np
import matplotlib.pyplot as plt
#定义一个numpy array对象
a = np.array(1)
print(a)
a = np.array([1,2,3,4])
print(a)

#利用numpy对象绘制一条曲线
x = np.arange(-10,10,0.1)
y = x**2
#print(x)
# plt.plot(x,y)
# plt.show()
#numpy操作 造一个相似矩阵
x = np.array([[1,2,3],[3,4,5]])
y = np.tile(np.array(3),x.shape)
print("-----op tile----")
print(y)
