import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np 
import sys





def plot(bend, xlabel, system):
    hist, bin_edges = np.histogram(bend, bins=360, range=[0,180], normed=True)
    print np.shape(hist)
    print np.shape(bin_edges[0:-1])

    plt.plot(bin_edges[0:-1],hist)
    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    plt.xlabel(r'%s' %(xlabel), size=12)
    plt.ylabel(r'Probability Distribution', size=12)
#    plt.xticks(np.arange(0,361,60))
    plt.xlim((0,180))
    plt.savefig('%s.bend.pdf' %(system))
    plt.close()


rtd = np.pi/180
names=["RADC","RVDC","RLDC","RIDC","RFDC"]
#names=["RADC","RFDC"]
colors = ['k','r','b','g','m']
for j,name in enumerate(names):
        print name
        fiber_rot=[]
        fiber_rot2=[]
        for i in range(1,4):
                fiber_rot.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/%s/bend_twist/%s.tot.fiber_rot_angle.dat" %(i,name,name)))
        fiber_rot = np.array(fiber_rot)


        fiber_num_col = len(fiber_rot[0])
        fiber_num_row = len(fiber_rot)
        fiber_tot_rot = []
        for col in range(fiber_num_col):
            for row in range(fiber_num_row):
                fiber_tot_rot.append(fiber_rot[row,col])
        fiber_tot_rot = np.array(fiber_tot_rot)

        hist, bin_edges = np.histogram(fiber_tot_rot, bins=360, range=[0,180], normed=True)
        plt.plot(bin_edges[0:-1],hist,label=name,color=colors[j])

plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
plt.xlabel(r'Rot Angle ($\degree$)', size=12)
plt.ylabel(r'Probability Distribution', size=12)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12),  shadow=True, ncol=5,fontsize = 'medium')
plt.xlim((0,180))
plt.ylim((0,0.016))
plt.savefig('fiber_neutral_rot.pdf')
plt.close()

names=["RADC","RVDC","RLDC","RIDC","RFDC"]
#names=["RADC","RFDC"]
colors = ['k','r','b','g','m']
for j,name in enumerate(names):
        print name
        fiber_rot=[]
        fiber_rot2=[]
        for i in range(1,4):
                fiber_rot.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/%sn/bend_twist/%sn.tot.fiber_rot_angle.dat" %(i,name,name)))
        fiber_rot = np.array(fiber_rot)


        fiber_num_col = len(fiber_rot[0])
        fiber_num_row = len(fiber_rot)
        fiber_tot_rot = []
        for col in range(fiber_num_col):
            for row in range(fiber_num_row):
                fiber_tot_rot.append(fiber_rot[row,col])
        fiber_tot_rot = np.array(fiber_tot_rot)

        hist, bin_edges = np.histogram(fiber_tot_rot, bins=360, range=[0,180], normed=True)
        plt.plot(bin_edges[0:-1],hist,label=name,color=colors[j])

plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
plt.xlabel(r'Rot Angle ($\degree$)', size=12)
plt.ylabel(r'Probability Distribution', size=12)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12),  shadow=True, ncol=5,fontsize = 'medium')
plt.xlim((0,180))
plt.ylim((0,0.016))
plt.savefig('fiber_acidic_rot.pdf')
plt.close()


rtd = np.pi/180
names=["RADC","RVDC","RLDC","RIDC","RFDC"]
#names=["RADC","RFDC"]
colors = ['k','r','b','g','m']
for j,name in enumerate(names):
        print name
        strand_rot=[]
        strand_rot2=[]
        for i in range(1,4):
                strand_rot.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/%s/bend_twist/%s.tot.strand_rot_angle.dat" %(i,name,name)))
        strand_rot = np.array(strand_rot)


        strand_num_col = len(strand_rot[0])
        strand_num_row = len(strand_rot)
        strand_tot_rot = []
        for col in range(strand_num_col):
            for row in range(strand_num_row):
                strand_tot_rot.append(strand_rot[row,col])
        strand_tot_rot = np.array(strand_tot_rot)

        hist, bin_edges = np.histogram(strand_tot_rot, bins=360, range=[0,180], normed=True)
        plt.plot(bin_edges[0:-1],hist,label=name,color=colors[j])

plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
plt.xlabel(r'Rot Angle ($\degree$)', size=12)
plt.ylabel(r'Probability Distribution', size=12)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12),  shadow=True, ncol=5,fontsize = 'medium')
plt.xlim((0,180))
plt.ylim((0,0.016))
plt.savefig('strand_neutral_rot.pdf')
plt.close()

names=["RADC","RVDC","RLDC","RIDC","RFDC"]
#names=["RADC","RFDC"]
colors = ['k','r','b','g','m']
for j,name in enumerate(names):
        print name
        strand_rot=[]
        strand_rot2=[]
        for i in range(1,4):
                strand_rot.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/%sn/bend_twist/%sn.tot.strand_rot_angle.dat" %(i,name,name)))
        strand_rot = np.array(strand_rot)


        strand_num_col = len(strand_rot[0])
        strand_num_row = len(strand_rot)
        strand_tot_rot = []
        for col in range(strand_num_col):
            for row in range(strand_num_row):
                strand_tot_rot.append(strand_rot[row,col])
        strand_tot_rot = np.array(strand_tot_rot)

        hist, bin_edges = np.histogram(strand_tot_rot, bins=360, range=[0,180], normed=True)
        plt.plot(bin_edges[0:-1],hist,label=name,color=colors[j])

plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
plt.xlabel(r'Rot Angle ($\degree$)', size=12)
plt.ylabel(r'Probability Distribution', size=12)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12),  shadow=True, ncol=5,fontsize = 'medium')
plt.xlim((0,180))
plt.ylim((0,0.016))
plt.savefig('strand_acidic_rot.pdf')
plt.close()

