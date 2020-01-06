
import numpy as np
import sys
import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator,FixedLocator,FixedFormatter)
import types
stdev = np.std
sqrt = np.sqrt
nullfmt = NullFormatter()

def plot_1d(xdata, ydata, xlabels, names, x_axis, y_axis, system):
	fig, ax = plt.subplots(1,1,figsize=(6,5))
	colors = ["grey","r","g","b","m"]
        for name_num,name in enumerate(names):
		plt.plot(xdata[name_num], ydata[name_num,:,0]*100, 'k', label=name,marker="o", mec = 'k', mfc = colors[name_num], lw=0.75, mew=0.75,ms=10.0,clip_on=False)
#		plt.plot(xdata[name_num], ydata[name_num,:,2]*100, 'k', label=name,marker="x", mec = 'k', mfc = colors[name_num], lw=0.75, mew=0.75,ms=10.0,clip_on=False,linestyle="--")
        #plt.plot(xdata, ydata[:,1]*100, 'k', label="$\\alpha$-helix",marker="o", mec = 'k', mfc = 'r', lw=0.75, mew=0.75,ms=10.0,clip_on=False)
        #plt.plot(xdata, ydata[:,2]*100, 'k', label="Turn/Bend",marker="o", mec = 'k', mfc = 'b', lw=0.75, mew=0.75,ms=10.0,clip_on=False)
        plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
        plt.xlabel(r'%s' %(x_axis), size=14)
        plt.ylabel(r'%s' %(y_axis), size=14)
	plt.xticks(np.arange(1,17))
	ax.set_xlabel(r'%s' %(x_axis), size=14)
	x_locator=FixedLocator([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16])
	x_formatter=FixedFormatter(xlabels)
	ax.xaxis.set_major_formatter(x_formatter)
	ax.xaxis.set_major_locator(x_locator)	
	SHIFT = 0.4 # Data coordinates
	for num,label in enumerate(ax.get_xmajorticklabels()):
		if (num-1)%2==0:
			label.set_rotation(315)
			label.customShiftValue = SHIFT
			label.set_x = types.MethodType( lambda self, x: matplotlib.text.Text.set_x(self, x+self.customShiftValue ), label, matplotlib.text.Text )
	ax.tick_params(pad=3.0)
	plt.xticks(fontsize=12)
	plt.yticks(fontsize=12)
	plt.ylim((0, 100.0))
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.13),  shadow=True, ncol=5,fontsize = 12)
	plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.20)
        plt.savefig('%s.combined.pdf' %(system))
        plt.close()



names1 = ["RADA","RVDV","RLDL","RIDI","RFDF"]
names2 = ["RADAn","RVDVn","RLDLn","RIDIn","RFDFn"]
hyd = ["Ala","Val","Leu","Ile","Phe"]
data = np.zeros((5,16,3),dtype=float)
xdata = np.zeros((5,16),dtype=float)	
for name_num,name in enumerate(names1):
	for rep in range(1,4):
		dat = np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/%s/DSSP2/sec_struc_count.dat" %(rep,name))


		count = 0
		for i in range(len(dat)):
			data[name_num,count,0] += dat[i,2]
			data[name_num,count,0] += dat[i,3]
			data[name_num,count,1] += dat[i,4]
			data[name_num,count,1] += dat[i,5]
			data[name_num,count,2] += dat[i,1]
			data[name_num,count,2] += dat[i,7]
			data[name_num,count,2] += dat[i,8]
			
			count += 1
			if count == 16:
				count = 0


	for i in range(16):
		data[name_num,i,:] /= np.sum(data[name_num,i,:])
		xdata[name_num,i] = i+1
	xlabels = ("1","\n N-Arg","2","\n X","3","\n Asp","4","\n X","5","\n Arg","6","\n X","7","\n Asp","8","\n X","9","\n Arg","10","\n X","11","\n Asp","12","\n X","13","\n Arg","14","\n X","15","\n Asp","16","\n C-X")

plot_1d(xdata, data, xlabels, hyd, "Residue Number and Name", "$\\beta$-Sheet Structure (%)","neutral")

data = np.zeros((5,16,3),dtype=float)
xdata = np.zeros((5,16),dtype=float)	
for name_num,name in enumerate(names2):
	for rep in range(1,4):
		dat = np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/%s/DSSP2/sec_struc_count.dat" %(rep,name))


		count = 0
		for i in range(len(dat)):
			data[name_num,count,0] += dat[i,2]
			data[name_num,count,0] += dat[i,3]
			data[name_num,count,1] += dat[i,4]
			data[name_num,count,1] += dat[i,5]
			data[name_num,count,2] += dat[i,1]
			data[name_num,count,2] += dat[i,7]
			data[name_num,count,2] += dat[i,8]
			
			count += 1
			if count == 16:
				count = 0


	for i in range(16):
		data[name_num,i,:] /= np.sum(data[name_num,i,:])
		xdata[name_num,i] = i+1
	xlabels = ("1","\n N-Arg","2","\n X","3","\n Asp","4","\n X","5","\n Arg","6","\n X","7","\n Asp","8","\n X","9","\n Arg","10","\n X","11","\n Asp","12","\n X","13","\n Arg","14","\n X","15","\n Asp","16","\n C-X")

plot_1d(xdata, data, xlabels, hyd, "Residue Number and Name", "$\\beta$-Sheet Structure (%)","acidic")
