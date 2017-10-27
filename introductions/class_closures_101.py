# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:17:33 2017

@author: Admin
"""

def multiply(x, factor):
    return x * factor

multiply(3,2)

# %%
def make_multiplier(factor):
    def multiply(x, factor=factor):
        return x * factor
    return multiply
# %%
m2 = make_multiplier(2)
m3 = make_multiplier(3)

print(m3(2))
print(m2(2))

#%%
class multiplier(object):
    
    def __init__(self, factor):
        self.factor = factor
        
    def multiply(self, x):
        return x * self.factor
    
    def set_factor(self, factor):
        self.factor = factor
# %%
m2 = multiplier(2)
m3 = multiplier(3)        
print(m3.multiply(2))
print(m2.multiply(2))

# %%
class global_multiplier:
    factor = 1
    
    def multiply(self, x):
        return x * self.factor
    
    def set_factor(self, factor):
        self.factor = factor
# %%
m = global_multiplier()
print(m.multiply(2))
m.set_factor(2)      
print(m.multiply(2))

# %%
class mathy(multiplier, ):
    def __init__(self, factor, summand):
        super().__init__(factor)
        self.summand = summand
    
    def sum(self, x):
        return x + self.summand
    
m = mathy(3,2)
m.sum(6)
m.multiply(32)