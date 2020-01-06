
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

def plot_1d(xdata, ydata, xlabels, x_axis, y_axis, system):
	fig, ax = plt.subplots(1,1,figsize=(6,5))
	colors = ["grey","b","g","r","m"]
	for j in range(len(ydata)):
		type = len(ydata)-j-1
		plt.plot(xdata, ydata[type,:,0]*100, label=j,color=colors[j],clip_on=False,marker="o",mec = 'k')
		#plt.plot(xdata, ydata[type,:,0]*100, 'k', label=type,marker="o", mec = 'k', mfc = colors[type], lw=0.75, mew=0.75,ms=10.0,clip_on=False)
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
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),  shadow=True, ncol=5,fontsize = 12)
	plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.20)
        plt.savefig('%s.strand.pdf' %(system))
        plt.close()


kind = ((1,10,11,20),(2,9,12,19),(3,8,13,18),(4,7,14,17),(5,6,15,16))
		
names = ["RADA","RADAn","RVDV","RVDVn","RLDL","RLDLn","RIDI","RIDIn","RFDF","RFDFn"]
hydro = ["Ala","Ala","Val","Val","Leu","Leu","Ile","Ile","Phe","Phe"]

for name_num,name in enumerate(names):
	data = np.zeros((5,16,3),dtype=float)
	xdata = np.zeros(16,dtype=float)
	for rep in range(1,4):
		dat = np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/%s/DSSP2/sec_struc_count.dat" %(rep,name))
		
		for type in range(len(kind)):
			for strand in range(len(kind[type])):
				for res in range(16):
					data[type,res,0] += dat[(kind[type][strand]-1)*16+res,2]
					data[type,res,0] += dat[(kind[type][strand]-1)*16+res,3]
					data[type,res,1] += dat[(kind[type][strand]-1)*16+res,4]
					data[type,res,1] += dat[(kind[type][strand]-1)*16+res,5]
					data[type,res,2] += dat[(kind[type][strand]-1)*16+res,1]
					data[type,res,2] += dat[(kind[type][strand]-1)*16+res,7]
					data[type,res,2] += dat[(kind[type][strand]-1)*16+res,8]

	for j in range(5):
		for i in range(16):
			data[j,i,:] /= np.sum(data[j,i,:])
			xdata[i] = i+1

        xlabels = ("1","\n N-Arg","2","\n %s" %(hydro[name_num]),"3","\n Asp","4","\n %s" %(hydro[name_num]),"5","\n Arg","6","\n %s" %(hydro[name_num]),"7","\n Asp","8","\n %s" %(hydro[name_num]),"9","\n Arg","10","\n %s" %(hydro[name_num]),"11","\n Asp","12","\n %s" %(hydro[name_num]),"13","\n Arg","14","\n %s" %(hydro[name_num]),"15","\n Asp","16","\n C-Ala")

	plot_1d(xdata, data, xlabels, "Residue Number and Name", "$\\beta$-Sheet Structure (%)", name)
