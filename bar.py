import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
language=['nepali','hindi','english','french','spanish']
people=[100,60,70,30,20]
ax.bar(language,people)
ax.set_xlabel('LANGUAGE')
ax.set_ylabel('PEOPLE')
ax.set_title("BAR GRAPH")
plt.tight_layout()
plt.show()

#pie chart
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
language=['nepali','hindi','english','french','spanish']
people=[100,60,70,30,20]
ax.pie(people,labels=language,autopct='%1.1f%%')
plt.show()

#scatter plot
x=np.linspace(0,10,30)
y=np.sin(x)
z=np.cos(x)
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.scatter(x,y,color='g')
ax.scatter(x,z,color='r')
plt.show()