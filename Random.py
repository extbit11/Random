#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class Random:
    def __init__(self,n,seeda,seedb):
        self.amount=n
        self.minRange=seeda
        self.maxRange=seedb

    def myfunc(self):
        numbers = []
        for i in range(self.amount):
            a = random.randint(self.minRange, self.maxRange)
            numbers.append(a)
        print(numbers)
x = Random(5,10,30)
x.myfunc()


# In[ ]:




