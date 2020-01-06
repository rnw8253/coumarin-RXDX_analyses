import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from scipy import stats

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
       rects1 = ax.bar(ind+width/2.0, data[:,1], width, yerr=data[:,2], color='b',edgecolor='k', capsize=6)
       rects2 = ax.bar(ind+width*3/2.0, data[:,3], width, yerr=data[:,4], color='r',edgecolor='k',capsize=6)

       ax.set_ylabel(r'Coumarin SASA ($\AA^{2}$)')
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
#       plt.yticks(np.arange(0,1.1,0.1))
#       plt.ylim((0,1))
       plt.grid(b=True, which='major', axis='y', color='#808080', linestyle='--')
       plt.savefig('SASA_bar.pdf')
       plt.close()




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
       data1.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RADC/SASA/SASA.dat" %(i)))
       data1n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RADCn/SASA/SASA.dat" %(i)))
       data2.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RVDC/SASA/SASA.dat" %(i)))
       data2n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RVDCn/SASA/SASA.dat" %(i)))
       data4.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RIDC/SASA/SASA.dat" %(i)))
       data4n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RIDCn/SASA/SASA.dat" %(i)))
       data3.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RLDC/SASA/SASA.dat" %(i)))
       data3n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RLDCn/SASA/SASA.dat" %(i)))
       data5.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RFDC/SASA/SASA.dat" %(i)))
       data5n.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate%s/RFDCn/SASA/SASA.dat" %(i)))

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

data[0,1] = np.average(data1[:,2])
data[1,1] = np.average(data2[:,2])
data[2,1] = np.average(data3[:,2])
data[3,1] = np.average(data4[:,2])
data[4,1] = np.average(data5[:,2])

data[0,2] = stats.sem(data1[:,2])
data[1,2] = stats.sem(data2[:,2])
data[2,2] = stats.sem(data3[:,2])
data[3,2] = stats.sem(data4[:,2])
data[4,2] = stats.sem(data5[:,2])

#data[0,2] = np.std(data1[:,2])/np.sqrt(len(data1))
#data[1,2] = np.std(data2[:,2])/np.sqrt(len(data2))
#data[2,2] = np.std(data3[:,2])/np.sqrt(len(data3))
#data[3,2] = np.std(data4[:,2])/np.sqrt(len(data4))
#data[4,2] = np.std(data5[:,2])/np.sqrt(len(data5))

data[0,3] = np.average(data1n[:,2])
data[1,3] = np.average(data2n[:,2])
data[2,3] = np.average(data3n[:,2])
data[3,3] = np.average(data4n[:,2])
data[4,3] = np.average(data5n[:,2])

data[0,4] = stats.sem(data1n[:,2])
data[1,4] = stats.sem(data2n[:,2])
data[2,4] = stats.sem(data3n[:,2])
data[3,4] = stats.sem(data4n[:,2])
data[4,4] = stats.sem(data5n[:,2])

#data[0,4] = np.std(data1n[:,2])/np.sqrt(len(data1n))
#data[1,4] = np.std(data2n[:,2])/np.sqrt(len(data2n))
#data[2,4] = np.std(data3n[:,2])/np.sqrt(len(data3n))
#data[3,4] = np.std(data4n[:,2])/np.sqrt(len(data4n))
#data[4,4] = np.std(data5n[:,2])/np.sqrt(len(data5n))

plot(data,labels)
