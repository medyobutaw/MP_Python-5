import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,200)
x = eval(input('Test x(n):'))
y = []

def python5(n):
    
    if n == 0:
        
        return -1.5*x[n] + 2*x[n+1] - 0.5*x[n+2]
    
    elif (n > 0) and (n <= 198):
        
        return 0.5*x[n+1] - 0.5*x[n-1]
    
    elif n == 199:
        
        return 1.5*x[n] - 2*x[n-1] + 0.5*x[n-2]

for k in np.arange(0,200):
    y.append(python5(k))
    
plt.plot(n,x,color = 'b', label = 'x(n)')
plt.plot(n,y,color = 'r', label = 'y(n)')
plt.grid()
plt.xlabel('n')
plt.ylabel('x(n) and y(n)')
plt.show()