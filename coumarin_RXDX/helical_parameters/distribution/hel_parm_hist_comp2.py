import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

stdev = np.std
sqrt = np.sqrt
nullfmt = NullFormatter()

def hist1d(data1, x_axis, num_b, system, norm):

        events, edges, patches = plt.hist(data1, bins=num_b, histtype = 'step', normed=norm, color='k', linewidth=2.0)
        plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
        plt.xlabel(r'%s' %(x_axis), size=12)
	if norm == True:
                plt.ylabel('Probability Density')
                plt.savefig('%s.png' %(system))
        else:
                plt.ylabel('Frequency', size=12)
                plt.savefig('%s.png' %(system))

        plt.close()
        events = []
        edges = []
        patches = []

def hist1d2(data1, x_axis, num_b, system, norm):

        events, edges, patches = plt.hist(data1, bins=num_b, histtype = 'step', normed=norm, color='k', linewidth=2.0)
        plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
        plt.xlabel(r'%s' %(x_axis), size=12)
	plt.xlim((-180,180))
	if norm == True:
                plt.ylabel('Probability Density')
                plt.savefig('%s.png' %(system))
        else:
                plt.ylabel('Frequency', size=12)
                plt.savefig('%s.png' %(system))

        plt.close()
        events = []
        edges = []
        patches = []




data1=[]
data2=[]
data3=[]
data4=[]
data5=[]
data1n=[]
data2n=[]
data3n=[]
data4n=[]
data5n=[]

for i in range(1,4):
	data1.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RADC/helical_param/RADC.heli_parm.dat" %(i)))
	data1n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RADCn/helical_param/RADCn.heli_parm.dat" %(i)))
	data2.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RVDC/helical_param/RVDC.heli_parm.dat" %(i)))
	data2n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RVDCn/helical_param/RVDCn.heli_parm.dat" %(i)))
	data3.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RLDC/helical_param/RLDC.heli_parm.dat" %(i)))
	data3n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RLDCn/helical_param/RLDCn.heli_parm.dat" %(i)))
	data4.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RIDC/helical_param/RIDC.heli_parm.dat" %(i)))
	data4n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RIDCn/helical_param/RIDCn.heli_parm.dat" %(i)))
	data5.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RFDC/helical_param/RFDC.heli_parm.dat" %(i)))
	data5n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RFDCn/helical_param/RFDCn.heli_parm.dat" %(i)))


data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)
data4 = np.array(data4)
data5 = np.array(data5)
data1n = np.array(data1n)
data2n = np.array(data2n)
data3n = np.array(data3n)
data4n = np.array(data4n)
data5n = np.array(data5n)

name = ["RADC","RADCn","RVDC","RVDCn","RLDC","RLDCn","RIDC","RIDCn","RFDC","RFDCn"]
data = [data1,data1n,data2,data2n,data3,data3n,data4,data4n,data5,data5n]

for i in range(len(data)):
	hist1d(data[i][:,0], "Slide", 200, "%s.slide" %(name[i]), True)
	hist1d(data[i][:,1], "Shift", 200, "%s.shift" %(name[i]), True)
	hist1d(data[i][:,2],  "Rise", 200,  "%s.rise" %(name[i]), True)
	hist1d2(data[i][:,3],  "Roll", 360,  "%s.roll" %(name[i]), True)
	hist1d2(data[i][:,4],  "Tilt", 360,  "%s.tilt" %(name[i]), True)
	hist1d2(data[i][:,5], "Twist", 360, "%s.twist" %(name[i]), True)
