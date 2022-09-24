## Infinite square well

import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
a=2*pi*1.0
xvals=np.linspace(0,a,100) # evaluating psi at this x values
A=(2/a)**(1/2)  # Normalization constant
def psi(n,x):
    wf=A*np.sin(n*pi*x/a)  # Defining the wave function
    return wf
def psiSq(n,x):
    wf=(A)**2*(np.sin(n*pi*x/a))**2
    return wf

yvals1=psi(1,xvals)
yvals2=psi(2,xvals)
yvals_2=psiSq(2,xvals)
yvals3=psi(3,xvals)
yvals4=psi(4,xvals)
yvals5=psi(5,xvals)
plt.plot(xvals,yvals1,'b',linewidth=2.0,label='n=1')
plt.plot(xvals,yvals2,'r',linewidth=2.7,label='n=2')
plt.plot(xvals,yvals_2,'y',linewidth=2.0,label='n=3')
plt.plot(xvals,yvals3,'k',linewidth=1.7,label='n=4')
plt.plot(xvals,yvals4,'mo',linewidth=0.7,label='n=5')
plt.plot(xvals,yvals5,'g',linewidth=1.8,label='n=6')
plt.legend()
plt.title("wave function for inf sq well")
plt.xlabel("x values")
plt.ylabel("$\psi^2$(x)")
plt.grid()
plt.show()
    


