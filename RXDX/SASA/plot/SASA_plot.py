import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from scipy import stats

nullfmt = NullFormatter()

def plot(data,data2,labels):

       N = 5
       ind = np.arange(N)  # the x locations for the groups
       width = 0.35       # the width of the bars
       
       fig = plt.figure()
       ax = fig.add_subplot(111)
       
       rects1 = ax.bar(ind+width/2.0, data[:,0], width, yerr=data[:,1], color='b',edgecolor='k', capsize=6)
       rects2 = ax.bar(ind+width*3/2.0, data2[:,0], width, yerr=data2[:,1], color='r',edgecolor='k', capsize=6)

       ax.set_ylabel(r'Hydrophobic $\Delta$SASA ($\AA^{2}$)')
       ax.set_xticks(ind+width)

#       lab=["Ala","Val","Leu","Ile","Phe"]
       lab=["(RADA)$_{4}$","(RVDV)$_{4}$","(RLDL)$_{4}$","(RIDI)$_{4}$","(RFDF)$_{4}$"]
       ax.set_xticklabels(lab[:])

       ax.legend( (rects1[0], rects2[0]), (labels[:]), loc='upper center', bbox_to_anchor=(0.5, 1.12),  shadow=True, ncol=2,fontsize = 'medium' )

#       def autolabel(rects):
#           for rect in rects:
#               h = rect.get_height()
#               ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
#                       ha='center', va='bottom')

#       autolabel(rects1)
#       autolabel(rects2)

       ax.set_axisbelow(True)
#       plt.yticks(np.arange(0,1.1,0.1))
#       plt.ylim((0,1))
       plt.grid(b=True, which='major', axis='y', color='#808080', linestyle='--')
       plt.savefig('SASA_initial.pdf')
       plt.close()


data1=[]
data2=[]
data3=[]
data4=[]
data5=[]
data6=[]
data7=[]
data8=[]
data9=[]
data10=[]
data1n=[]
data2n=[]
data3n=[]
data4n=[]
data5n=[]
data6n=[]
data7n=[]
data8n=[]
data9n=[]
data10n=[]

for i in range(1,4):
       print i
       data1.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RADA/SASA/sasa.run00.dat" %(i)))
       data2.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RVDV/SASA/sasa.run00.dat" %(i)))
       data3.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RLDL/SASA/sasa.run00.dat" %(i)))
       data4.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RIDI/SASA/sasa.run00.dat" %(i)))
       data5.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RFDF/SASA/sasa.run00.dat" %(i)))
       data6.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RADAn/SASA/sasa.run00.dat" %(i)))
       data7.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RVDVn/SASA/sasa.run00.dat" %(i)))
       data8.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RLDLn/SASA/sasa.run00.dat" %(i)))
       data9.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RIDIn/SASA/sasa.run00.dat" %(i)))
       data10.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/RFDFn/SASA/sasa.run00.dat" %(i)))

for i in range(2,4):
       data1n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RADA/SASA/sasa.total.dat" %(i)))
       data2n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RVDV/SASA/sasa.total.dat" %(i)))
       data3n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RLDL/SASA/sasa.total.dat" %(i)))
       data4n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RIDI/SASA/sasa.total.dat" %(i)))
       data5n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RFDF/SASA/sasa.total.dat" %(i)))
       data6n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RADAn/SASA/sasa.total.dat" %(i)))
       data7n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RVDVn/SASA/sasa.total.dat" %(i)))
       data8n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RLDLn/SASA/sasa.total.dat" %(i)))
       data9n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RIDIn/SASA/sasa.total.dat" %(i)))
       data10n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/replicate%s/RFDFn/SASA/sasa.total.dat" %(i)))

data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)
data4 = np.array(data4)
data5 = np.array(data5)
data6 = np.array(data6)
data7 = np.array(data7)
data8 = np.array(data8)
data9 = np.array(data9)
data10 = np.array(data10)

data1n = np.array(data1n)
data2n = np.array(data2n)
data3n = np.array(data3n)
data4n = np.array(data4n)
data5n = np.array(data5n)
data6n = np.array(data6n)
data7n = np.array(data7n)
data8n = np.array(data8n)
data9n = np.array(data9n)
data10n = np.array(data10n)

data = np.zeros((5,2),dtype=float)
data2 = np.zeros((5,2),dtype=float)
labels = ["Neutral","Acidic"]

print np.average(data1n[:,1]),np.average(data6n[:,1]), 
print np.average(data2n[:,1]),np.average(data7n[:,1]), 
print np.average(data3n[:,1]),np.average(data8n[:,1]), 
print np.average(data4n[:,1]),np.average(data9n[:,1]), 
print np.average(data5n[:,1]),np.average(data10n[:,1]), 


data[0,0] = 20*np.average(data1n[:,1]) - np.average(data1[:,1])
data[1,0] = 20*np.average(data2n[:,1]) - np.average(data2[:,1])
data[2,0] = 20*np.average(data3n[:,1]) - np.average(data3[:,1])
data[3,0] = 20*np.average(data4n[:,1]) - np.average(data4[:,1])
data[4,0] = 20*np.average(data5n[:,1]) - np.average(data5[:,1])

data[0,1] =  np.sqrt(stats.sem(data1n[:,1])**2 + stats.sem(data1[:,1])**2)
data[1,1] =  np.sqrt(stats.sem(data2n[:,1])**2 + stats.sem(data2[:,1])**2)
data[2,1] =  np.sqrt(stats.sem(data3n[:,1])**2 + stats.sem(data3[:,1])**2)
data[3,1] =  np.sqrt(stats.sem(data4n[:,1])**2 + stats.sem(data4[:,1])**2)
data[4,1] =  np.sqrt(stats.sem(data5n[:,1])**2 + stats.sem(data5[:,1])**2)

data2[0,0] = 20*np.average(data6n[:,1]) - np.average(data6[:,1])
data2[1,0] = 20*np.average(data7n[:,1]) - np.average(data7[:,1])
data2[2,0] = 20*np.average(data8n[:,1]) - np.average(data8[:,1])
data2[3,0] = 20*np.average(data9n[:,1]) - np.average(data9[:,1])
data2[4,0] = 20*np.average(data10n[:,1]) - np.average(data10[:,1])

data2[0,1] =  np.sqrt(stats.sem(data6n[:,1])**2 + stats.sem(data6[:,1])**2)
data2[1,1] =  np.sqrt(stats.sem(data7n[:,1])**2 + stats.sem(data7[:,1])**2)
data2[2,1] =  np.sqrt(stats.sem(data8n[:,1])**2 + stats.sem(data8[:,1])**2)
data2[3,1] =  np.sqrt(stats.sem(data9n[:,1])**2 + stats.sem(data9[:,1])**2)
data2[4,1] =  np.sqrt(stats.sem(data10n[:,1])**2 + stats.sem(data10[:,1])**2)

plot(data,data2,labels)
