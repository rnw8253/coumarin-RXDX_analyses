import numpy as np
import sys
import matplotlib.pyplot as plt


names = ["RADC","RADCn","RVDC","RVDCn","RLDC","RLDCn","RIDC","RIDCn","RFDC","RFDCn"]
for name in names:
    data = np.loadtxt("../%s.dimer_angles.dat" %(name))
    dist = np.concatenate((data[:,0],data[:,0]))
    alpha = np.hstack((data[:,1],data[:,2]))

    hist, xedges, yedges = np.histogram2d(dist,alpha,range=[[0,80],[0,180]],bins=[80,60],normed=True)

#    fig = plt.figure(figsize=(7, 5))
#    ax = fig.add_subplot(111)
#    X, Y = np.meshgrid(xedges, yedges)
#    plt.imshow(hist.T, interpolation='nearest', origin='low',extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],cmap='hot_r',aspect=0.444,vmin=0,vmax=0.0045)
#    plt.xticks(np.arange(0,81,10))
#    plt.yticks(np.arange(0,181,15))
#    plt.colorbar(pad = 0.1)
#    plt.xlabel(r'Distance, R ($\AA$)', size=12)
#    plt.ylabel(r'$\alpha$ ($\degree$)', size=12)
#    plt.savefig("%s.alpha.pdf" %(name))
#    plt.close()

    out=open("%s.alpha_counts.dat" %(name),'w')
    for i in range(len(hist)):
        for j in range(len(hist[0])):
            out.write("  %10.5f   %10.5f   %12.8e\n" %(xedges[i], yedges[j], hist[i,j]))
    out.close

    hist, xedges, yedges = np.histogram2d(data[:,0],data[:,3],range=[[0,80],[0,180]],bins=[80,60],normed=False)
#    fig = plt.figure(figsize=(7, 5))
#    ax = fig.add_subplot(111)
#    X, Y = np.meshgrid(xedges, yedges)
#    plt.imshow(hist.T, interpolation='nearest', origin='low',extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],cmap='hot_r',aspect=0.444,vmin=0,vmax=0.0045)
#    plt.xticks(np.arange(0,81,10))
#    plt.yticks(np.arange(0,181,15))
#    plt.colorbar(pad = 0.1)
#    plt.xlabel(r'Distance, R ($\AA$)', size=12)
#    plt.ylabel(r'$\beta$ ($\degree$)', size=12)
#    plt.savefig("%s.beta.pdf" %(name))
#    plt.close()

    out=open("%s.beta_counts.dat" %(name),'w')
    for i in range(len(hist)):
        for j in range(len(hist[0])):
            out.write("  %10.5f   %10.5f   %12.8e\n" %(xedges[i], yedges[j], hist[i,j]))
    out.close
