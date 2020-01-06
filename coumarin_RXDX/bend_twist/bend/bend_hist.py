import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np 
import sys


def plot(xdata, ydata, xlabel, ylabel, system):
    plt.plot(xdata,ydata) 
    plt.xlabel(r"%s" %(xlabel), size=12)
    plt.ylabel(r"%s" %(ylabel), size=12)    
    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    plt.xlim((0,90))
    plt.savefig("%s.bend.pdf" %(system))
    plt.close()


rtd = np.pi/180
strand_bend_sheet1 = []
strand_bend_sheet2 = []
hist_min = 0
hist_max = 90
bin_size = 0.5
num_bins = int((hist_max-hist_min)/bin_size)
hist = np.zeros((2,num_bins),dtype=float)
x = np.zeros(num_bins,dtype=float)

for num in range(30,50):
#    fiber_bend = np.loadtxt("RADC.run%s.fiber_bend_angle.dat" %(num))
    strand_bend = np.loadtxt("RADC.run%s.strand_bend_angle.dat" %(num))

    
    for row in range(len(strand_bend)):
        for col in range(int(len(strand_bend[0]))):
            if col < (len(strand_bend[0])/2.0):
                bin = int((strand_bend[row,col]-hist_min)/bin_size)
                if 0 <= bin < num_bins:
                    hist[0,bin] += 1
            else:
                bin = int((strand_bend[row,col]-hist_min)/bin_size)
                if 0 <= bin < num_bins:
                    hist[1,bin] += 1


hist[0,:] /=  np.sum(hist[0,:])
hist[1,:] /=  np.sum(hist[1,:])

for i in range(num_bins):
    x[i] = (i+0.5)*bin_size + hist_min
    jacobian = np.sin(((i+0.5)*bin_size + hist_min)*rtd)
    hist[0,i] /= jacobian
    hist[1,i] /= jacobian


plot(x, hist[0,:], "Bend Angle ($\degree$)", "Probability", "RADC.strand.sheet1")
plot(x, hist[1,:], "Bend Angle ($\degree$)", "Probability", "RADC.strand.sheet2")

