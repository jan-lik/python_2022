import matplotlib.pyplot as plt
import numpy as np
def func(f, min_x, max_x, N, min_y, max_y):
    x = np.linspace(min_x, max_x, N)
    y = f(x)
    plt.yscale('log')
    plt.grid(True)
    plt. plot(x, y, '--g')
    plt.ylim((min_y, max_y))

    plt.savefig('function.png')
    plt.show()
f = lambda x: x**3
min_x = 0
max_x = 10
N = 50
min_y = 0
max_y = 500
func(f, min_x, max_x, N, min_y, max_y)