import numpy as np

# b = np.random.rand(3,2)
# c = np.random.randint(3,9, size=(2,4))
# print(b)
# print(c)

# p113 Linear Algebra
# a = np.array([[1,2], [3,4]])
# b = np.array([[-4],[1]])
# inv_a = np.linalg.inv(a)
# c = np.linalg.solve(a,b)
# d = np.linalg.det(a)
# e = np.linalg.eig(a)

# print(inv_a)
# print(c)
# print(d)
# print(e)

# Pyplot Module 
# p114
# from matplotlib import pyplot as plt
# plt.plot([1,2,3],[1,4,9],'c',markersize=12,linewidth=5)
# plt.plot([2,3,4],[5,6,7])
# plt.xlabel('Sequence')
# plt.ylabel('Time(sec')
# plt.title('Experimental Result')
# plt.legend(['Mouse', 'Cat'])
# plt.grid()
# plt.show()

#page118

import matplotlib.pyplot as plt

gaussian = lambda x: np.exp(-(0.5 - x) ** 2/ 1.5)

x = np.arange(-2,2.5,0.01)
y = gaussian(x)

plt.plot(x, y)
plt.xlabel('x values')
plt.ylabel('exp(-(0.5-x)**2/1.5')
plt.title('Gaussian Function')
plt.show()