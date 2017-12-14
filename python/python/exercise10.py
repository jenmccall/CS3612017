import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0, 2, 100)
    y = np.linspace(0, 2, 100)
    formula = (np.sin(pow((x - 2), )) * (np.e ** (-1 * pow(x, 2)))

    plt.title("(sin(x - 2))^2 * e^(-x^2)")
    plt.xlabel("x")
    plt.ylabel("y")
         
    plt.plot(x, formula)
    plt.show()
