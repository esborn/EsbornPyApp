
import matplotlib.pyplot as plt
import numpy as np
fig= plt.figure(facecolor='y')
chart1 = fig.add_subplot(1,1,1, facecolor='r')
chart1.tick_params(axis='x', color='w')
chart1.tick_params(axis='y', color='w')
for spine in chart1.spines:
    chart1.spines[spine].set_color('w')

#chart2 = fig.add_subplot(3,1,2)
#chart3 = fig.add_subplot(3,1,3)

x= np.arange(1,5)
chart1.plot(x ,x,'b--o', label='one')
#chart2.plot(x,x/2,'-.', label='Two', color='y') 
#chart3.plot(x,x*2, 'k-p',label='Three') 
#plt.legend(loc='best')
#plt.xlabel('this is the X axis')
#plt.ylabel('this is the Y axis')
chart1.grid(True)
plt.axis([0,5,0,9])
plt.show()