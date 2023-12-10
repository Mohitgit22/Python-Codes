seats=[114,15,4,3]
seats2=[99,77,13,4]
label=['Congress','BJP','Independent','Others']


import matplotlib.pyplot as plt

# Create a figure and an axes
fig=plt.figure(figsize=(10,10),facecolor='0.5')

fig1=plt.subplot(2,2,1)
fig2=plt.subplot(2,2,2)
fig3=plt.subplot(2,2,3)
explode=[0.2,0,0,0]
fig1.pie(seats,labels=label,explode=explode)
fig2.pie(seats2,labels=label,explode=explode)
import numpy as np
distance=np.arange(4)
fig3.bar(distance,seats,width=0.25)
fig3.bar(distance+0.25,seats2,width=0.25)
fig3.set_xticks(distance+0.25, label)

plt.show()

