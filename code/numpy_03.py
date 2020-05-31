import numpy as np

#求逆 行列式 linalg(numpy的线性代数模块)
if __name__ == "__main__":
    x = np.array([[1.,2.],[3.,4.]])
    y = x*4
    print(np.linalg.inv(x))#逆
    print(np.linalg.det(x))#行列式
    print(x.T)#转置

    #最小二乘法,求出 w  ；wx=y
    print(np.linalg.inv(x.T@x)@x.T@y)
    #过时方法，求逆
    # a = np.matrix(x)
    # print(a.I)
    #求特征向量
    print(x)
    print(np.linalg.eig(x))#返回两个值，特征值和特征向量
    #SVD 求奇异值矩阵
    x = np.array([[1.,2.],[3.,4.],[5.,6.]])
    print(np.linalg.svd(x))#返回三个值 中间那个为奇异值