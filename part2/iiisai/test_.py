import numpy as np

x_shape = (2, 3, 4, 4)

x = np.linspace(-.5, 0.5, num=np.product(x_shape)).reshape(x_shape)
# pad =1
# pads = ((0, 0), (0, 0), (pad, pad), (pad, pad))

# x_0 = np.pad(x, pads, 'constant')
print(x)
print(x.reshape(2, 3 * 4 * 4))
print(x.reshape(2, 3 * 4 * 4).T)



