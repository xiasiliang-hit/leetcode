import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

samples = datasets.load_iris()

#print(samples.data.shape)
#print(samples.target)

print samples.data
print samples.target

def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def pq_function(x):
    p = 10
    q = 10
    return 1 - pow( 1 - pow(x, p), q)


if __name__ =="__main__":
    x = np.arange(-10, 10, 0.1)
    y = [sigmoid(i) for i in x]

#    plt.plot(x,y)

    x2 = np.arange(0, 1, 0.01)
    z = [pq_function(i) for i in x2]
    plt.plot(x2, z)
    
    plt.show()
