import numpy as np
import matplotlib.pyplot as plt
#100 values in x from 0 to 10
#linspace gives the no between the given value
x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)
print(x)
print(y)
print(z)
plt.plot(x,y)
plt.show()

#for cosine
#plt.plot(x,z)
#plt.show()

#adding title for x and y labels
plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sine value')
plt.title('sine wave')
plt.show()

#for parabola
x=np.linspace(-5,5,20)
y=x**2
plt.plot(x,y)
plt.show()

#r represents red color and + prints the parabola as a + sign
plt.plot(x,y,'r+')
plt.show()

#plotting in the same graph
x=np.linspace(-5,5,50)
plt.plot(x,np.sin(x),'r.')
plt.plot(x,np.cos(x),'g-')
plt.show()