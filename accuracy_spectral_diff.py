'''
Spectral methods program 7: Compute the error (infinity norm) vs. N for four
different functions
accuracy of periodic spectral differentiation
'''
from scipy.linalg import toeplitz,norm
import matplotlib.pyplot as plt
import numpy as np

#compute derivatives for various values of N
Nmax=50
n=np.arange(6,Nmax+2,2)
E1=[];E2=[];E3=[];E4=[]
for N in np.arange(6,Nmax+2,2):
    h=2*np.pi/N
    column=np.zeros(N)
    x=h*np.arange(1,N+1)
    for c in range(1,N):
        column[c]=.5*(-1)**c*1/np.tan(c*h/2)
    D=toeplitz(column,-column)
    v1=abs(np.sin(x))**3
    v2=np.exp(-np.sin(x/2)**-2)
    v3=1/(1+np.sin(x/2)**2)
    v4=np.sin(10*x)
    v1prime=3*np.sin(x)*np.cos(x)*abs(np.sin(x)) #analytic derivative
    v2prime=.5*v2*np.sin(x)/np.sin(x/2)**4
    v3prime=-np.sin(x/2)*np.cos(x/2)*v3**2
    v4prime=10*np.cos(10*x)
    #infinity norm of difference
    E1.append(norm(np.matmul(D,v1)-v1prime,np.inf))
    E2.append(norm(np.matmul(D,v2)-v2prime,np.inf))
    E3.append(norm(np.matmul(D,v3)-v3prime,np.inf))
    E4.append(norm(np.matmul(D,v4)-v4prime,np.inf))
plt.xlim([0,50])
plt.ylim([-5,15])
f,axs=plt.subplots(2,2,sharex='all',sharey='all')
axs[0,0].plot(n,E1,'ko')
axs[0,0].plot(n,E1,color='purple')
axs[0,1].plot(n,E2,'ko')
axs[0,1].plot(n,E2,color='purple')
axs[1,0].plot(n,E3,'ko')
axs[1,0].plot(n,E3,color='purple')
axs[1,1].plot(n,E4,'ko')
axs[1,1].plot(n,E4,color='purple')

#set_title('Accuracy of Spectral Differentiation for 4 Different Functions')
plt.show()
