
import numpy as np
import matplotlib.pyplot as plt
import torch
import math

# x = np.arange(0.00001,100,0.01)
# y = [math.log(i,10) for i in x]
#
# print(math.log(10))

# x = np.arange(100,0,-0.1)
# print(x)
# y = [math.log(i,10) for i in x]

# x = np.arange(0,100)
# y = [3 for i in x]

# x = [1,2,3,4]
# y = x**2

# x = np.arange(-100,100,0.01)
# y = [math.sin(i) for i in x]

x = torch.tensor(1)
y = np.array(1)

print(x,type(x))
print(y,type(y))

x = torch.tensor([[1,2],[3,4]])
print(x.shape)
y = np.array([1,2])
print(y.shape)

#
# plt.plot(x,y)
# plt.show()