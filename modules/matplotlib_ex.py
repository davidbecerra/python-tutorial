import matplotlib.pyplot as plt
import numpy as np


# Plot a function : f(x) = x^2
domain = range(0, 100)
y = [x ** 2 for x in domain]
plt.plot(y)
plt.ylabel('Numbers')
plt.show()


# Plot Histogram
mu, sigma = 0, 1
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50)

plt.xlabel('Data points')
plt.ylabel('Probability')
plt.title('Histogram of Normally Distributed Values')
plt.grid(True)
plt.show()
# from http://matplotlib.org/users/pyplot_tutorial.html