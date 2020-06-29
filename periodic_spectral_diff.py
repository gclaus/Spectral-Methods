'''
Spectral methods program 4: periodic spectral differentiation for the hat
function (non-smooth) and e^sin(x) (smooth) function
'''
from scipy.linalg import toeplitz
import matplotlib.pyplot as plt
import numpy as np

#grid and differentiation matrix
N=24
h=2*np.pi/N
x=np.arange(1,N+1,1)
x=h*x
column=np.zeros(N)
for c in range(1,N):
    column[c]=.5*(-1)**c*1/np.tan(c*h/2)
D=toeplitz(column,-column)

#differentiation of e^sin(x)
v=np.zeros(N)
v=np.exp(np.sin(x))
vprime=np.zeros(N)
vprime=np.cos(x)*v
#for i in range(1,N+1):
    #v[i-1]=np.exp(np.sin(i))
    #vprime[i-1]=np.cos(i)*v[i-1]
plt.plot(x,v,color='black')
plt.plot(x,v,'ko')
plt.title('e^sin(x)')
plt.show()
plt.plot(x,np.matmul(D,v),color='black')
plt.plot(x,np.matmul(D,v),'ko')
plt.title('Spectral differentiation of e^sin(x)')
plt.show()
