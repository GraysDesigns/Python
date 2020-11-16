import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(1, 11)
y = x * x
plt.title("Line graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x, y, color = "red")
plt.show
