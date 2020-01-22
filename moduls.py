import random

def dela(x, y):
    for i in range(1,1000):
        if i % x == 0 and i % y ==0:
            print(i, end = ', ')