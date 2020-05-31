import numpy as np

#指数运算，对数运算,形状属性 shape
if __name__ == "__main__":
    x = np.arange(0.1,10,0.1)
    y = np.log(x)#log 函数以10为底
    y2 = np.zeros_like(x)
    y3 = np.exp(x)#指数操作
    print(y)
    print(y2)
    print(y3)
    print(x.shape)