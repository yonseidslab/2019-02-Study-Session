#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# In[2]:


x1 = np.linspace(0.2,0.2,145)
y1 = np.linspace(0.7,0.41,145)
x2 =np.linspace(0.12,0.5,190) 
y2 =np.linspace(0.286,0.286,190)
x3 =np.linspace(0.5,0.45,25)
y3 =np.linspace(0.554,0.554,25)
theta1 = np.linspace(-0.56*np.pi,np.pi,245)
theta2 = np.linspace(np.pi*0.5,np.pi*1.5,120)
theta3 = np.linspace(np.pi*-0.5,np.pi*0.5,100)
theta4 = np.linspace(np.pi*-0.5,np.pi*-2,130)
x = np.concatenate((x1,np.cos(theta1)/10+0.22,np.cos(theta2)/13+0.12,x2,np.cos(theta3)/15+0.5,x3,np.cos(theta4)/18+0.45),axis=0)
y= np.concatenate((y1,np.sin(theta1)/5+0.6,np.sin(theta2)/6.5+0.44,y2,np.sin(theta3)/7.5+0.42,y3,np.sin(theta4)/9+0.665),axis=0)


# In[7]:


fig = plt.figure(figsize=(14,10))
ax = plt.axes(xlim=(0,0.7),ylim=(0,1))
line, = ax.plot([], [], lw=2,linewidth=25)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1500, interval=0.1, blit=True,repeat=False)

plt.show()


# In[ ]:




