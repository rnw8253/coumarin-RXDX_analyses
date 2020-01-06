import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

stdev = np.std
sqrt = np.sqrt
nullfmt = NullFormatter()

    
def plot(xdata1, ydata1, color1, label1, xdata2, ydata2, color2, label2, xdata3, ydata3, color3, label3, xdata4, ydata4, color4, label4, x_axis, y_axis):
        plt.plot(xdata1,  ydata1,  '%s' %(color1), label = label1)
        plt.plot(xdata2,  ydata2,  '%s' %(color2), label = label2)
        plt.plot(xdata3,  ydata3,  '%s' %(color3), label = label3)
        plt.plot(xdata4,  ydata4,  '%s' %(color4), label = label4)
        plt.xlim((-20,20))
#        plt.ylim((0, 1.0))
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12),  shadow=True, ncol=4,fontsize = 'medium')
        plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
        plt.xlabel(r'%s' %(x_axis), size=12)
        plt.ylabel(r'%s' %(y_axis), size=12)
        plt.savefig('density.pdf')
        plt.close()



data=np.loadtxt(sys.argv[1])

plot(data[:,0], data[:,1], 'b', "R", data[:,0], data[:,2], 'r', "D",data[:,0], data[:,3], 'g', "X",data[:,0], data[:,4], 'k', "CA ", "Z ($\AA$)", "Probability")

