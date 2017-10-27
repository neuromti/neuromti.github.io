# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
def my_plotter(ax,x,y,title = 'Line'):
    ax.plot(x,y)
    ax.grid()
    ax.set_title(title)
    
def just_plot():
    x = np.arange(-101,101,1)
    y = x ** 2
    z = 10+(x/2)
    y = np.power(x,2)

    fig, ax = plt.subplots(1, 2, figsize = (6,3), dpi = 100)
    my_plotter(ax[0],x,y,'Power')
    my_plotter(ax[1],x,z)
    fig.show()
    
def _printStuff(txt = 'WTF'):
    print(txt)
# %% 
if __name__ == '__main__':
    just_plot()
    input('Wait for Buttonpress to close')