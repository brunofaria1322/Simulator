import matplotlib.pyplot as plt
import random


def func1(num_pack, loss):
    counter = 0
    while num_pack > 0:
        counter += 1
        if random.random() > loss:
            num_pack -= 1
    return counter
        
def loop(n, num_pack, loss):
    arr = []
    for i in range(n):
        arr.append(func1(num_pack, loss))
    return arr

a = loop(10000, 100, 0.05)
plt.hist(a)
plt.show()