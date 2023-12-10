months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
import random
high=[random.randint(20,50) for i in range(12)]
low=[random.randint(10,30) for i in range(12)]

import matplotlib.pyplot as plt
import numpy as np

# fobj=plt.figure(figsize=(10,16),facecolor='green')
# figure=plt.subplot(1,1,1)
distance=np.arange(12)
plt.bar(distance,high,color='red',width=0.25)
plt.bar(distance+0.25,low,color='blue',width=0.25)
plt.xticks(distance ,months)

plt.xlabel("Months")
plt.legend(['High','Low'])
plt.show()