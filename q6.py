import matplotlib.pyplot as plt

# Create a figure and an axes
fig=plt.figure(figsize=(10,10),facecolor='0.5')

fig1=plt.subplot(1,1,1)


# Create the data
import random
# Generate current values with randomness
current = [round(random.uniform(0.1, 0.5), 2) for _ in range(10)]

# Generate corresponding voltage values with randomness
volt = [round(random.uniform(1.0, 5.0), 2) for _ in range(10)]
volt.sort()
current.sort()
print(volt)
print(current)

# Generate current values with randomness
current2 = [round(random.uniform(0.1, 0.5), 2) for _ in range(10)]

# Generate corresponding voltage values with randomness
volt2 = [round(random.uniform(1.0, 5.0), 2) for _ in range(10)]
volt2.sort()
current2.sort()

fig1.plot(volt,current,color='red',linestyle='--',marker='o')

fig1.plot(volt2,current2,color='blue',linestyle=':',marker='*')
plt.xlabel('Volt')
plt.ylabel('Current')
plt.title('Current vs volt')
plt.legend(['diagram1','diagram2'],loc='upper left')
plt.show()