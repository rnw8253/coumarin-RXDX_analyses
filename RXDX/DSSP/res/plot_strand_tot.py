
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

def plot_1d(xdata, ydata, x_axis, y_axis, system):
	fig, ax = plt.subplots(1,1,figsize=(6,5))
	colors = ["grey","b","g","r","m"]
	for sheet in range(2):
		plt.plot(xdata, ydata[sheet,:,0]*100,label="Sheet %s" %(sheet+1),color=colors[sheet],clip_on=False,marker="o",mec = 'k')

        plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
        plt.xlabel(r'%s' %(x_axis), size=14)
        plt.ylabel(r'%s' %(y_axis), size=14)
	plt.xticks(np.arange(1,11))
	ax.set_xlabel(r'%s' %(x_axis), size=14)
#	x_locator=FixedLocator([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16])
#	x_formatter=FixedFormatter(xlabels)
#	ax.xaxis.set_major_formatter(x_formatter)
#	ax.xaxis.set_major_locator(x_locator)	
#	SHIFT = 0.4 # Data coordinates
#	for num,label in enumerate(ax.get_xmajorticklabels()):
#		if (num-1)%2==0:
#			label.set_rotation(315)
#			label.customShiftValue = SHIFT
#			label.set_x = types.MethodType( lambda self, x: matplotlib.text.Text.set_x(self, x+self.customShiftValue ), label, matplotlib.text.Text )
#	ax.tick_params(pad=3.0)
#	plt.xticks(fontsize=12)
	plt.yticks(fontsize=12)
	plt.ylim((0, 100.0))
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),  shadow=True, ncol=5,fontsize = 12)
	plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.20)
        plt.savefig('%s.strand_tot.pdf' %(system))
        plt.close()


names = ["RADA","RADAn","RVDV","RVDVn","RLDL","RLDLn","RIDI","RIDIn","RFDF","RFDFn"]
hydro = ["Ala","Ala","Val","Val","Leu","Leu","Ile","Ile","Phe","Phe"]

for name_num,name in enumerate(names):
	data = np.zeros((2,10,3),dtype=float)
	xdata = np.zeros(10,dtype=float)
	for rep in range(1,4):
                dat = np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate%s/%s/DSSP2/sec_struc_count.dat" %(rep,name))
		for sheet in range(2):
			for strand in range(10):
				for res in range(16):
					data[sheet,strand,0] += dat[sheet*10*16+strand*16+res,2]
					data[sheet,strand,0] += dat[sheet*10*16+strand*16+res,3]
					data[sheet,strand,1] += dat[sheet*10*16+strand*16+res,4]
					data[sheet,strand,1] += dat[sheet*10*16+strand*16+res,5]
					data[sheet,strand,2] += dat[sheet*10*16+strand*16+res,1]
					data[sheet,strand,2] += dat[sheet*10*16+strand*16+res,7]
					data[sheet,strand,2] += dat[sheet*10*16+strand*16+res,8]

	for strand in range(10):
		data[0,strand,:] /= np.sum(data[0,strand,:])
		data[1,strand,:] /= np.sum(data[1,strand,:])
		xdata[strand] = strand+1

	plot_1d(xdata, data, "Strand", "$\\beta$-Sheet Structure (%)", name)
