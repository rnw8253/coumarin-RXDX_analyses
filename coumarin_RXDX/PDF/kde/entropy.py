import numpy as np
import sys
from numpy import inf
import matplotlib.pyplot as plt


#names = ["RADC"]
names = ["RADC","RVDC","RLDC","RIDC","RFDC"]
out=open("relative_entropy.dat",'w')
for name in names:
    data1 = np.loadtxt("../%s.alpha.dat" %(name))
    data2 = np.loadtxt("../%sn.alpha.dat" %(name))
    data3 = np.loadtxt("../%s.beta.dat" %(name))
    data4 = np.loadtxt("../%sn.beta.dat" %(name))

#    data1[data1[:,2] == 0] == 1**(-100)
    S_alpha=0
    for i in range(len(data1)):    
        val = data1[i,2]*np.log(data1[i,2]/data2[i,2])
        val = np.nan_to_num(val)
        if abs(val) < 10000:
            S_alpha += val

    S_beta=0
    for i in range(len(data3)):
        val = data3[i,2]*np.log(data3[i,2]/data4[i,2])
        val = np.nan_to_num(val)
        if abs(val) < 10000:
            S_beta += val
    print S_alpha,S_beta
    out.write("  %s  %12.8e  %12.8e\n" %(name,S_alpha,S_beta))

out.close 
