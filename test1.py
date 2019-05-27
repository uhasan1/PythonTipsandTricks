listA = [1,2,3,4,5,6]

for i in (listA):
    print(i)

# How to get the reverse of a list:
print(listA[::-1])


import numpy as np
from sklearn.datasets.samples_generator import make_blobs

X, y = make_blobs(n_samples=15, centers=3, n_features=2)

print(X)
print(X[1])
print(X[1,1])
print(X[1][1])
