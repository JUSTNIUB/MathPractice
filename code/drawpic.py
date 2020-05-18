import matplotlib.pyplot as plt

x = [i for i in range(-10,10)]
y = [i**2 for i in x]

plt.plot(x,y)
plt.plot(x,[2*i-1 for i in x])
plt.show()