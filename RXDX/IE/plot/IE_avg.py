import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from scipy import stats

def plot(data,data2,labels,interaction):
       N = 5
       ind = np.arange(N)  # the x locations for the groups
       width = 0.35       # the width of the bars
       fig = plt.figure()
       ax = fig.add_subplot(111)
       rects1 = ax.bar(ind+width/2.0, data[:,0], width, yerr=data[:,1], color='b',edgecolor='k', capsize=6)
       rects2 = ax.bar(ind+width*3/2.0, data2[:,0], width, yerr=data2[:,1], color='r',edgecolor='k',capsize=6)

       ax.set_ylabel(r'Interaction Energy $(kcal \ mol^{-1})$',fontsize='medium')
       ax.set_xticks(ind+width)

       lab=["Ala","Val","Leu","Ile","Phe"]

       ax.set_xticklabels(lab[:])
       ax.legend( (rects1[0],rects2[0]), (labels[:]), loc='upper center', bbox_to_anchor=(0.5, 1.16),  shadow=True, ncol=2,fontsize = 'medium' )

       def autolabel(rects):
           for rect in rects:
               h = rect.get_height()
               ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                       ha='center', va='bottom',fontsize='medium')
       ax.set_axisbelow(True)
       plt.grid(b=True, which='major', axis='y', color='#808080', linestyle='--')
       plt.gcf().subplots_adjust(left=0.15)
       plt.savefig('%s.IE.bar.pdf' %(interaction))
       plt.close()

def plot2(data,data2,labels,interaction,name):
       N = len(interaction)
       ind = np.arange(N)  # the x locations for the groups                                                                                                                                                                           
       width = 0.35       # the width of the bars                                                                                                                                                                                     
       fig = plt.figure()
       ax = fig.add_subplot(111)
#       print data[sys,:,0]
       rects1 = ax.bar(ind+width/2.0, data[:,0], width, yerr=data[:,1], color='b',edgecolor='k', capsize=6)
       rects2 = ax.bar(ind+width*3/2.0, data2[:,0], width, yerr=data2[:,1], color='r',edgecolor='k',capsize=6)

       ax.set_ylabel(r'Interaction Energy $(kcal \ mol^{-1})$',fontsize='medium')
       ax.set_xticks(ind+width)


       ax.set_xticklabels(interaction[:])
       ax.legend( (rects1[0],rects2[0]), (labels[:]), loc='upper center', bbox_to_anchor=(0.5, 1.16),  shadow=True, ncol=2,fontsize = 'medium' )

       def autolabel(rects):
           for rect in rects:
               h = rect.get_height()
               ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                       ha='center', va='bottom',fontsize='medium')
       ax.set_axisbelow(True)
       plt.grid(b=True, which='major', axis='y', color='#808080', linestyle='--')
       plt.gcf().subplots_adjust(left=0.15)
       plt.savefig('%s.IE.bar.pdf' %(name))
       plt.close()



stdev = np.std
sqrt = np.sqrt
nullfmt = NullFormatter()

colors = ['k','r','b','g','m']
labels = ["Neutral","Acidic"]
interaction = ["ARG-ARG","ARG-X","ARG-ASP","X-X","X-ASP","ASP-ASP","Total"]
time = 10


data_c = np.zeros((len(interaction),5,2),dtype=float)
data_res = np.zeros((5,len(interaction),2),dtype=float)
names=["RADA","RVDV","RLDL","RIDI","RFDF"] 
for j,name in enumerate(names):
        print name
        data=[]
        for i in range(1,4):
               data.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/%s/IE2/%s.run00.IE_coul.dat" %(i,name,name))) 
	data = np.array(data)
        for col in range(1,7):
               data_c[col-1,j,0] = np.average(data[:int(time*500),col])
               data_c[col-1,j,1] = stats.sem(data[:int(time*500),col])
               data_res[j,col-1,0] = np.average(data[:int(time*500),col])
               data_res[j,col-1,1] = stats.sem(data[:int(time*500),col])
               data_c[6,j,0] += np.average(data[:int(time*500),col])
               data_c[6,j,1] += stats.sem(data[:int(time*500),col])**2
               data_res[j,6,0] += np.average(data[:int(time*500),col])
               data_res[j,6,1] += stats.sem(data[:int(time*500),col])
               
#        data_c[6,j,0] /= len(interaction)
        data_c[6,j,1] = np.sqrt(data_c[6,j,1])
        data_res[j,6,1] = np.sqrt(data_res[j,6,1])

data2_c = np.zeros((len(interaction),5,2),dtype=float)
data2_res = np.zeros((5,len(interaction),2),dtype=float)
names=["RADAn","RVDVn","RLDLn","RIDIn","RFDFn"] 
for j,name in enumerate(names):
        print name
        data2=[]
        for i in range(1,4):
               data2.extend(np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/%s/IE2/%s.run00.IE_coul.dat" %(i,name,name))) 
	data2 = np.array(data2)
        for col in range(1,7):		
               data2_c[col-1,j,0] = np.average(data2[:int(time*500),col])
               data2_c[col-1,j,1] = stats.sem(data2[:int(time*500),col])
               data2_res[j,col-1,0] = np.average(data2[:int(time*500),col])
               data2_res[j,col-1,1] = stats.sem(data2[:int(time*500),col])
               data2_c[6,j,0] += np.average(data2[:int(time*500),col])
               data2_c[6,j,1] += stats.sem(data2[:int(time*500),col])**2
               data2_res[j,6,0] += np.average(data2[:int(time*500),col])
               data2_res[j,6,1] += stats.sem(data2[:int(time*500),col])

#        data2_c[6,j,0] /= len(interaction)
        data2_c[6,j,1] = np.sqrt(data2_c[6,j,1])
        data2_res[j,6,1] = np.sqrt(data2_res[j,6,1])

for i in range(len(interaction)):
       plot(data_c[i],data2_c[i],labels,interaction[i])
       print data_res[i],data2_res[i],names[i]

names=["RADA","RVDV","RLDL","RIDI","RFDF"]        
for i in range(len(names)):
       plot2(data_res[i],data2_res[i],labels,interaction,names[i])

