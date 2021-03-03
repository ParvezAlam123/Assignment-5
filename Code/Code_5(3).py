import numpy as np
import matplotlib.pyplot as plt
b=np.random.binomial(6,0.5,1000)
c=0
for i in range(1000):
    if b[i]<=5 :
        c=c+1
prob=c/1000
plt.scatter(5,prob,color='red',label='experimental result')
plt.scatter(5,0.984375,color='green', label='theortical result')
plt.xlabel('X_1')
plt.ylabel('probability')
plt.legend()
plt.title('simulation')
plt.show()



