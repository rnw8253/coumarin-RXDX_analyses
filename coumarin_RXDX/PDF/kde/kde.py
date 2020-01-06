import numpy as np
import sys
from scipy import stats
import matplotlib.pyplot as plt

names = ["RIDC","RIDCn"]
for name in names:
    data = np.loadtxt("../%s.dimer_angles.dat" %(name))

    dat = np.vstack([data[:,0],data[:,3]])
    k = stats.gaussian_kde(dat,0.01)
    x = np.arange(0,81,1.0)
    y = np.arange(0,181,3.0)

    out = open("%s.beta.dat" %(name),'w')
    dat = np.zeros((len(x),len(y)),dtype=float)
    for i in range(len(x)):
        for j in range(len(y)):
            dat[i,j] = k.evaluate((x[i],y[j]))
            out.write("  %10.5f   %10.5f   %12.8e\n" %(x[i],y[j],dat[i,j]))
    out.close

    plt.imshow(dat.T, interpolation='nearest', origin='low',extent=[0, 80, 0, 180],cmap='hot_r',aspect=0.4444,vmin=0,vmax=0.002)
    plt.xticks(np.arange(0,81,10))
    plt.yticks(np.arange(0,181,15))
    plt.colorbar(pad = 0.1)
    plt.xlabel(r'Distance, R ($\AA$)', size=12)
    plt.ylabel(r'$\beta$ ($\degree$)', size=12)
    plt.savefig("%s.beta.pdf" %(name))
    plt.close()


#    temp1 = np.vstack([data[:,0],data[:,1]])
#    temp2 = np.vstack([data[:,0],data[:,2]])
#    dat = np.hstack([temp1,temp2])
#    k = stats.gaussian_kde(dat,0.01)
#    x = np.arange(0,81,1.0)
#    y = np.arange(0,181,3.0)
#
#    out = open("%s.alpha.dat" %(name),'w')
#    dat = np.zeros((len(x),len(y)),dtype=float)
#    for i in range(len(x)):
#        for j in range(len(y)):
#            dat[i,j] = k.evaluate((x[i],y[j]))
#            out.write("  %10.5f   %10.5f   %12.8e\n" %(x[i],y[j],dat[i,j]))
#    out.close
#
#    plt.imshow(dat.T, interpolation='nearest', origin='low',extent=[0, 80, 0, 180],cmap='hot_r',aspect=0.4444)
#    plt.xticks(np.arange(0,81,10))
#    plt.yticks(np.arange(0,181,15))
#    plt.colorbar(pad = 0.1)
#    plt.xlabel(r'Distance, R ($\AA$)', size=12)
#    plt.ylabel(r'$\alpha$ ($\degree$)', size=12)
#    plt.savefig("%s.alpha.pdf" %(name))
#    plt.close()




