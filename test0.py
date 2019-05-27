import sys
import numpy as np
import pandas as pd
print(sys.executable)
print(sys.version)

from tqdm import tqdm

class Employee:
    """ A sample Employee class """

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{}  {}'.format(self.first, self.last)


employee_1 = Employee('Ghasak', 'Ibrahim')

print(employee_1.email)
print(employee_1.fullname)

for i in range(10):
    print("Hello world this is {}".format(i))


x = np.array([1, 2, 3, 4, 5])
print(x)

Y = {'Col1': [1, 2, 3, 4, 5], 'Col2': ['g', 2, 4, 5, 98]}

for key, item in Y.items():
    print(key, item[1:3])


Dict = {"X": ["A", "B", "C"], "Y": [100, 200, 300, 500], "Z": [0]}
for key, value in Dict.items():
    print(f"Colum {key}", f"and Value = {value}")

for i in tqdm(range(int(1000000))):
    pass

# There are many things that we would like to add to our current file
A = [1,2,3,4]
B = {"col1": [1,2,3],"col2":[4,5,6]}

# Forms of for loop in python:
# Forms with a list-form,
for item in A:
    print(item)
print("-----------")
for item in B.keys():
    print(item)
print("-----------")
for item in B.values():
    print(item)
print("-----------")
for item in B.items():
    print(item)
    print("The value of keys is {} and the value of list of a key is {}".format(item[0],item[1]))
print("-----------")

# Forms with looping through counters

for i in range(len(A)):
    print(A[i])
print("-----------")

for i in range(len(B.values())):
    print(B["col1"][i])
    print(B["col2"][i])

print("-----------")
# Or

# Usually the dictionaries are not ordered so we can use the following loop to call the values of Col1 or Col2
# for i in range(len(B)):
#     print(B[0][i])
#     print(B[1][i])

# There is anotherway which is not good and no one use just to over come the problem above
# https://stackoverflow.com/questions/4326658/how-to-index-into-a-dictionary
Bnew = {1:[1,2,3],2:[4,5,6],3:[7,8,9]}

for i in range(len(Bnew)):
    print(Bnew[1][i])
    print(Bnew[2][i])

