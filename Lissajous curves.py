"""
@emayaml

This code is for the lissajous curves in a course of Physics 3
in the University of Envigado in Colombia.
If do you want contact me, please write me at:
    Twitter: @emayaml
    Instagram: @emayaml
    Blog: emmanuelmayaml.blogspot.com
    Git: @emayaml

and remember to give me a star in Github, and be happy!
"""


#Code number 1
import matplotlib.pyplot as plt
import math
import time

def draw_line():
    x_number_list = list();
    y_number_list = list();

    for i in range(0,315):
      t = i * 0.02;
      x = math.cos(t * 3)
      y = math.sin(t * 2)
      x_number_list.append(x)
      y_number_list.append(y)
      if abs(x - x_number_list[0]) + abs(y - y_number_list[0]) < 0.01 and i > 1:
        print("Lissajous curves draw  " + str(i) + " pixels")
        break

    plt.plot(1, 1, linewidth=33)
    plt.title("Lissajous Curve", fontsize=14)
    plt.plot(y_number_list, x_number_list, linewidth = 0.5, c="red")
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_aspect('equal', adjustable='box')
    # Display the plot in the matplotlib's viewer.
    plt.show()    
    plt.savefig('lissajous.png', bbox_inches='tight')


if __name__ == '__main__':
    draw_line()



#code number 2
import numpy as np
import matplotlib.pyplot as plt



def lissajous(a,b,t,f,phi):
    """
    Genera una figura de lissajous con los parametros dados
    """
    x = a*np.sin(2*np.pi*f*t + phi)
    y = b*np.sin(2*np.pi*f*t)
    return x,y


def lissajous_fig(a,b,t,f,phi):
    """
    Genera una figura de lissajous con los parametros dados
    """
    x = a*np.sin(2*np.pi*f*t + phi)
    y = b*np.sin(2*np.pi*f*t)
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_aspect('equal')
    return fig, ax


def lissajous_fig_ax(ax,a,b,t,f,phi):
    """
    Genera una figura de lissajous con los parametros dados
    """
    x = a*np.sin(2*np.pi*f*t + phi)
    y = b*np.sin(2*np.pi*f*t)
    ax.plot(x,y)
    ax.set_aspect('equal')
    return ax


#Code number 3
from numpy import sin,pi,linspace
from pylab import plot,show,subplot
import matplotlib.pyplot as plt
import math
import time

a = [1,3,5,3] # plotting the curves for
b = [1,5,7,4] # different values of a/b

#d is: 0 pi pi/4 pi/2  3*pi/4 pi 5*pi/4 3*pi/2 7*pi/4
#d = 7*pi/4

d = float(input("value of d: "))
t = linspace(-pi,pi,300)

for i in range(0,1):
 x = sin(a[i] * t + d)
 y = sin(b[i] * t)
 print('lissajous curves with his algebra')
 subplot(2,2,i+1)
 plot(x,y)

show()
