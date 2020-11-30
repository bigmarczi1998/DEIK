import matplotlib.pyplot as plt
import numpy as np

# norbi
def sigmoid(x):
    return 1 / (1 + np.power(np.e, -x))


def sigmoid_derivaltja(x):
    return sigmoid(x) * (1 - sigmoid(x))


x = np.arange(-3, 3, 0.01)
y = sigmoid(x)
dy = sigmoid_derivaltja(x)

plt.plot(x, y, 'g-')
plt.plot(x, dy, 'r-')
plt.xlabel("x erteke")
plt.ylabel("y ereteke")
plt.title("Sigmoid fgv")
plt.show()




# marcsi
import math


def function(vector):
    fx_s = []
    for i in vector:
        fx = 1 / (1 + math.exp(-i))
        fx_s.append(fx)
    return fx_s


def main():
    vector = np.arange(-3, 3, 0.01)
    fx_s = function(vector)
    print(fx_s)
    plt.plot(fx_s)
    plt.show()


if __name__ == '__main__':
    main()
