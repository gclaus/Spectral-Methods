'''
Band-limited interpolation for three discrete functions: Kronecker delta,
square wave, and hat function
'''
import numpy as np
import matplotlib.pyplot as plt

h=1 #computational grid spacing
xmax=10
x=np.arange(-xmax,xmax,h) #computational grid
xx=np.arange(-xmax-h/20,xmax+h/20,h/10) #plotting grid
v1=[];v2=[];v3=[]
#delta function
for i in x:
    if i==0:
        v1.append(1.)
    else:
        v1.append(0.)

#square wave
for i in x:
    if abs(i)<=3:
        v2.append(1.)
    else:
        v2.append(0.)

#hat function
for i in x:
    v3.append(max(0,1-abs(i)/3))
    
p1=np.zeros(len(xx));p2=np.zeros(len(xx));p3=np.zeros(len(xx))
for i in range(0,len(x)):
    p1+=v1[i]*np.sin(np.pi*(xx-x[i])/h)/(np.pi*(xx-x[i])/h)
    p2+=v2[i]*np.sin(np.pi*(xx-x[i])/h)/(np.pi*(xx-x[i])/h)
    p3+=v3[i]*np.sin(np.pi*(xx-x[i])/h)/(np.pi*(xx-x[i])/h)

f,(ax1,ax2,ax3)=plt.subplots(3,1,sharey=True)
ax1.plot(x,v1,'ko')
ax1.plot(xx,p1)
ax1.set_title('Band-limited Interpolation for Three Different Functions')
ax2.plot(x,v2,'ko')
ax2.plot(xx,p2)
ax3.plot(x,v3,'ko')
ax3.plot(xx,p3)
ax3.set_xlabel('x')
plt.show()
'''    
plt.plot(xx,p)
plt.xlim([-xmax,xmax])
plt.ylim([-.5,1.5])
plt.show()
'''
