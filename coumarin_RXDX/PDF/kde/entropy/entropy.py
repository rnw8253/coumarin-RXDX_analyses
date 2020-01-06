import numpy as np
import sys
from numpy import inf
import matplotlib.pyplot as plt
from scipy import stats

names = ["RADC","RVDC","RLDC","RIDC","RFDC"]
#names = ["RIDC"]
out=open("relative_entropy.dat",'w')
deg_to_rad=np.pi/180.0

for name in names:
    data1 = np.loadtxt("../../plots/%s.beta_counts.dat" %(name))
    data2 = np.loadtxt("../../plots/%sn.beta_counts.dat" %(name))
    data3 = np.loadtxt("../%s.beta.dat" %(name))
    data4 = np.loadtxt("../%sn.beta.dat" %(name))

    data3[:,2] /= np.sum(data3[:,2])
    data4[:,2] /= np.sum(data4[:,2])


    data1.astype(int)
    data2.astype(int)
    data1[data1[:,2] == 0] = 1
    data2[data2[:,2] == 0] = 1

    tot1 = np.sum(data1[:,2])*3
    tot2 = np.sum(data2[:,2])*3

    err1 = np.sqrt(data1[:,2])/tot1
    err2 = np.sqrt(data2[:,2])/tot2


    print 1/tot2
    for i in range(len(data4[:,2])):
        if (1/data4[i,2]) == np.inf:
            data4[i,2] = 1/tot2

    S_beta=0
    S_error=0
    count = 0
    for i in range(len(data3)):
        if int(data3[i,1]) != 180 and int(data3[i,0]) != 80:
            a = data3[i,2]/data4[i,2]
            if a != 0.0:
                err_val = np.sqrt((1+np.log(a))**2*err1[count]*err1[count] + (a)**2*err2[count]*err2[count])
            else:
                err_val = err1[count]
            if err_val < 0.001:
                S_error += err_val*err_val
            val = data3[i,2]*np.log(data3[i,2]/data4[i,2])
            val = np.nan_to_num(val)
            S_beta += val
    S_error = np.sqrt(S_error)
    print S_beta, S_error

    out.write("  %s  %12.8e  %12.8e\n" %(name,S_beta,S_error))

out.close 
