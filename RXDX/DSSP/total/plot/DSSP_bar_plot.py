import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

stdev = np.std
sqrt = np.sqrt
nullfmt = NullFormatter()

def plot(data,labels):

       N = 5
       ind = np.arange(N)  # the x locations for the groups
       width = 0.35       # the width of the bars
       
       fig = plt.figure()
       ax = fig.add_subplot(111)
       
#       rects1 = ax.bar(ind+width/2.0, data[:,1], width, yerr=data[:,2], color='dimgrey',edgecolor='k', capsize=6)
#       rects2 = ax.bar(ind+width*3/2.0, data[:,3], width, yerr=data[:,4], color='lightgrey',edgecolor='k', capsize=6)
       rects1 = ax.bar(ind+width/2.0, data[:,1]*100, width, yerr=data[:,2], color='b',edgecolor='k', capsize=6)
       rects2 = ax.bar(ind+width*3/2.0, data[:,3]*100, width, yerr=data[:,4], color='r',edgecolor='k',capsize=6)

       ax.set_ylabel(r'$\beta$-Sheet Content (%)')
       ax.set_xticks(ind+width)

#       lab=["Ala","Val","Leu","Ile","Phe"]
       lab=["(RADA)$_{4}$","(RVDV)$_{4}$","(RLDL)$_{4}$","(RIDI)$_{4}$","(RFDF)$_{4}$"]

       ax.set_xticklabels(lab[:])
#       ax.set_xticklabels(data[:,0])

       ax.legend( (rects1[0], rects2[0]), (labels[:]), loc='upper center', bbox_to_anchor=(0.5, 1.12),  shadow=True, ncol=2,fontsize = 'medium' )

       def autolabel(rects):
           for rect in rects:
               h = rect.get_height()
               ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                       ha='center', va='bottom')

#       autolabel(rects1)
#       autolabel(rects2)

#       plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12),  shadow=True, ncol=5,fontsize = 'medium')
       ax.set_axisbelow(True)
#       plt.gca().yaxis.grid(True)
       plt.yticks(np.arange(0,101,10))
       plt.ylim((0,100))
       plt.grid(b=True, which='major', axis='y', color='#808080', linestyle='--')
       plt.savefig('DSSP_bar.pdf')
       plt.close()


time = 200
skip = 100


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
       test = np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RADA/DSSP/DSSP.dat" %(i))
       tot_rows = len(test)
       skip_rows = int(tot_rows - time*500) + 1

       test2 = np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RLDLn/DSSP/DSSP.dat" %(i))
       tot_rows2 = len(test2)
       skip_rows2 = int(tot_rows2 - time*500) + 1

       data1.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RADA/DSSP/DSSP.dat" %(i), skiprows=skip_rows))
       data1n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RADAn/DSSP/DSSP.dat" %(i), skiprows=skip_rows))
       data2.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RVDV/DSSP/DSSP.dat" %(i), skiprows=skip_rows))
       data2n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RVDVn/DSSP/DSSP.dat" %(i), skiprows=skip_rows))
       data4.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RIDI/DSSP/DSSP.dat" %(i), skiprows=skip_rows))
       data4n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RIDIn/DSSP/DSSP.dat" %(i), skiprows=skip_rows))
       data3.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RLDL/DSSP/DSSP.dat" %(i), skiprows=skip_rows))
       data3n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RLDLn/DSSP/DSSP.dat" %(i), skiprows=skip_rows2))
       data5.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RFDF/DSSP/DSSP.dat" %(i), skiprows=skip_rows))
       data5n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RFDFn/DSSP/DSSP.dat" %(i), skiprows=skip_rows))

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
       
data = np.zeros((5,5),dtype=float)
labels = ["Neutral","Acidic"]

data[0,1] = np.average(data1[::skip,1])
data[1,1] = np.average(data2[::skip,1])
data[2,1] = np.average(data3[::skip,1])
data[3,1] = np.average(data4[::skip,1])
data[4,1] = np.average(data5[::skip,1])

data[0,2] = np.std(data1[::skip,1])
data[1,2] = np.std(data2[::skip,1])
data[2,2] = np.std(data3[::skip,1])
data[3,2] = np.std(data4[::skip,1])
data[4,2] = np.std(data5[::skip,1])

data[0,3] = np.average(data1n[::skip,1])
data[1,3] = np.average(data2n[::skip,1])
data[2,3] = np.average(data3n[::skip,1])
data[3,3] = np.average(data4n[::skip,1])
data[4,3] = np.average(data5n[::skip,1])

data[0,4] = np.std(data1n[::skip,1])
data[1,4] = np.std(data2n[::skip,1])
data[2,4] = np.std(data3n[::skip,1])
data[3,4] = np.std(data4n[::skip,1])
data[4,4] = np.std(data5n[::skip,1])

plot(data,labels)
