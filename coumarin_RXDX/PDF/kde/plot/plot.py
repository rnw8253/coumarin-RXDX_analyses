import numpy as np
import sys
import matplotlib.pyplot as plt

deg_to_rad = np.pi/180.0
#names = ["RADC","RADCn","RVDC","RVDCn","RLDC","RLDCn","RIDC","RIDCn","RFDC","RFDCn"]
names = ["RADC","RADCn","RFDC","RFDCn"]
for name in names:
    print name
    data = np.loadtxt("../%s.beta.dat" %(name))
    
    x_step = 1
    y_step = 3
    x_max = 80
    y_max = 180
    x_bins = int(x_max/x_step)+1
    y_bins = int(y_max/y_step)+1
    hist = np.zeros((x_bins,y_bins),dtype=float)

    for i in range(len(data)):
        xbin = int(data[i,0]/x_step)
        ybin = int(data[i,1]/y_step)
        print np.sin(data[i,1]*deg_to_rad)
        hist[xbin,ybin] = data[i,2]/np.sin(data[i,1]*deg_to_rad)#*(data[i,0]*data[i,0])

#    plt.imshow(hist.T, interpolation='nearest', origin='low',extent=[0, x_max, 0, y_max],cmap='hot_r',aspect=0.444,vmin=0,vmax=0.002)
    plt.imshow(hist.T, interpolation='nearest', origin='low',extent=[0, x_max, 0, y_max],cmap='hot_r',aspect=0.444)
    plt.xticks(np.arange(0,81,10))
    plt.yticks(np.arange(0,181,15))
    plt.colorbar(pad = 0.1)
    plt.xlabel(r'Distance, R ($\AA$)', size=12)
    plt.ylabel(r'$\beta$ ($\degree$)', size=12)
    plt.savefig("%s.beta.pdf" %(name))
    plt.close()
