#!/usr/bin/env python
# coding: utf-8

# In[13]:


import math


def mysqrt(x,a): 
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x
print("a\t\t\tmysqrt(a)\t\t\tmath.sqrt(a)")
print("-\t\t\t-------------\t\t\t----------------")
for i in range(9):
    n = i + 1
    print("{}\t\t\t{}\t\t{}".format(float(n),mysqrt(3,n),math.sqrt(n)))

