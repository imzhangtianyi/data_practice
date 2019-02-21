import random

def gen01(n):
    """
    generate random int from 0 to n
    :param n: right limit int
    :return: int
    """
    val = n + 1
    m = 0
    two = 2
    while two ** m < n:
        m += 1

    while val >= n:
        num = ''
        for _ in range(m):
            num = num + str(random.randint(0, 1))
        val = int(num, 2)
    return val

def rand6(n):
    """
    generate n from 6
    :param n: int
    :return: int
    """
    lim = n // 6 # e.g. n = 7, lim = 2, generate 0-12
    val = n + 1
    while val > n:
        val = random.randint(1, 6)
        for _ in range(lim):
            val += random.randint(1, 6) % 2 * 6# generate 1-12
    return val


import numpy as np
import matplotlib.pyplot as plt
arr = []
for _ in range(10000):
    arr.append(rand6(10))
plt.hist(arr)
plt.show()
