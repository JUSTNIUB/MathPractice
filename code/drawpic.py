import numpy
import torch
import matplotlib.pyplot as plt
#anum = ['幂函数','指数函数','对数函数','激活函数']
#testCase = '幂函数'
# testCase = '指数函数'
# testCase = '对数函数'
testCase = '激活函数'

if testCase == '幂函数':
    x = numpy.arange(-2,2,0.1)
    y = x**2
    y1 = x**3
    x1 = numpy.arange(0.1,10,0.001)
    y2 = x1**(0.5)
    x2 = numpy.arange(-10,-0.1,0.001)
    y3 = x2**(-1.0)
    y4 = x1**(-1.0)
    plt.plot(x, y)
    plt.plot(x, y1)
    plt.plot(x1, y2)
    plt.plot(x2, y3)
    plt.plot(x1, y4)
elif testCase == '指数函数':
    print('enter 指数函数')
    x = numpy.arange(-10,10,0.1)
    y = 2**x
    y1 = 0.5**x
    plt.plot(x,y)
    plt.plot(x,y1)
elif testCase == '对数函数':
    print('enter 对数函数')
    x = numpy.arange(0.1,10,0.1)
    y = numpy.log(x)
    y = torch.from_numpy(y)
    plt.plot(x,y)
    pass
elif testCase == '激活函数':
    print('enter 激活函数')
    x = numpy.arange(-10,10,0.1)
    sigmoidy = 1/(1+numpy.exp(-x))
    tanhy = (numpy.exp(x)-numpy.exp(-x))/(numpy.exp(x)+numpy.exp(-x))
    reluy = []
    for i in x:
        if i>=0:
            reluy.append(i)
        else:
            reluy.append(0)

    plt.plot(x,tanhy)
    plt.plot(x,reluy)
    plt.plot(x,sigmoidy)
    pass
else:
    pass

plt.plot([0 for i in range(-10,10)],[i for i in range(-10,10)])
plt.plot([i for i in range(-10,10)],[0 for i in range(-10,10)])
plt.show()