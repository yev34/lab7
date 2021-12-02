
from numpy import *
import matplotlib.pyplot as plt
import pylab

x = linspace(0, 5, 51)
y = (-5*cos(10*x)*sin(3*x)/(x**x))
plt.plot(x, y, 'g--', label='(-5*cos(10*x)*sin(3*x)/(x^x))')

plt.axis([0, 5 , -2, 2])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік')
plt.legend()

plt.show
pylab.show()
