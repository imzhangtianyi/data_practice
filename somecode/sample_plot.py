import matplotlib.pyplot as plt
import numpy as np


a = np.array(range(1000))
plt.plot(a, a**.5)
plt.plot(a, np.log(a))
plt.show()