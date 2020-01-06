import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np 
import sys





def plot(bend, rot, xlabel, ylabel, system, max):
    cm="hot_r"
#    plt.hist2d(rot,bend,bins=200,normed=True,range=[[0,360],[0,90]],cmap="hot_r")
    plt.hist2d(rot,bend,bins=200,normed=True,range=[[0,360],[0,90]],cmap="hot_r",vmin=0.0,vmax=max)
    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    plt.xlabel(r'%s' %(xlabel), size=12)
    plt.ylabel(r'%s' %(ylabel), size=12)
    plt.xticks(np.arange(0,361,60))
    plt.yticks(np.arange(0,91,15))
    plt.colorbar(pad = 0.1)
    plt.savefig('%s.bend.pdf' %(system))
    plt.close()

#def plot2(bend,rot,xlabel,ylabel,system):
#    cm="hot_r"
#    hist, y,x = np.histogram2d(bend,rot,range=[[0,90],[0,360]],bins=200,normed=True)
#    for i in range(len(y)-1):
#        hist[i,:] /= np.sin(y[i]*rtd)
#    plt.pcolormesh(x,y,hist,cmap=cm,edgecolors='face')
#    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
#    plt.xlabel(r'%s' %(xlabel), size=12)
#    plt.ylabel(r'%s' %(ylabel), size=12)
#    plt.xticks(np.arange(0,361,60))
#    plt.yticks(np.arange(0,91,15))
#    plt.colorbar(pad = 0.1)
#    plt.savefig('%s.bend.pdf' %(system))
#    plt.close()

rtd = np.pi/180
names=["RADC","RADCn","RVDC","RVDCn","RLDC","RLDCn","RIDC","RIDCn","RFDC","RFDCn"]
#names=["RADC"]
for name in names:
        print name
        fiber_bend=[]
        fiber_rot=[]
        strand_bend=[]
        strand_rot=[]
        for i in range(1,4):
                fiber_bend.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/%s/bend_twist/%s.tot.fiber_bend_angle.dat" %(i,name,name)))
        #        fiber_rot.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/%s/bend_twist/%s.tot.fiber_rot_angle.dat" %(i,name,name)))
        #        strand_bend.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/%s/bend_twist/%s.tot.strand_bend_angle.dat" %(i,name,name)))
        #        strand_rot.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/%s/bend_twist/%s.tot.strand_rot_angle.dat" %(i,name,name)))
        fiber_bend = np.array(fiber_bend)
        #fiber_rot = np.array(fiber_rot)
        #strand_bend = np.array(strand_bend)
        #strand_rot = np.array(strand_rot)


        fiber_num_col = len(fiber_bend[0])
        fiber_num_row = len(fiber_bend)
        fiber_tot_bend = []
        #fiber_tot_rot = []
        for col in range(fiber_num_col):
            for row in range(fiber_num_row):
                fiber_tot_bend.append(fiber_bend[row,col])
        #        fiber_tot_rot.append(fiber_rot[row,col])

        fiber_tot_bend = np.array(fiber_tot_bend)
        #fiber_tot_rot = np.array(fiber_tot_rot)

        #strand_num_col = len(strand_bend[0])
        #strand_num_row = len(strand_bend)
        #strand_tot_bend = []
        #strand_tot_rot = []
        #for col in range(strand_num_col):
        #    for row in range(strand_num_row):
        #        strand_tot_bend.append(strand_bend[row,col])
        #        strand_tot_rot.append(strand_rot[row,col])
        #
        #strand_tot_bend = np.array(strand_tot_bend)
        #strand_tot_rot = np.array(strand_tot_rot)


        print np.average(fiber_tot_bend)
        print np.std(fiber_tot_bend)

