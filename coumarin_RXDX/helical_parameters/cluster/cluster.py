import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import Axes3D

def plot_1d(xdata, ydata, color, x_axis, y_axis, system):
        plt.scatter(xdata, ydata, '%s' %(color))
        plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
        plt.xlabel(r'%s' %(x_axis), size=12)
        plt.ylabel(r'%s' %(y_axis), size=12)
        #    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12),  shadow=True, ncol=1, fontsize = 'medium')                                                                                       
        plt.xlim((0,200))
        plt.ylim((1.5, 3.0))
        plt.savefig('%s.png' %(system))
        plt.close()


def scatter_3d_density(x,y,z,axis_labels,axis_ranges,alpha=0.01,marker='.',bins=200,levels=10,linewidths=0.1,system="system"):
        fig = plt.figure(figsize=(12,12),dpi=600,facecolor='w',edgecolor='k')
        ax = fig.gca(projection='3d')
        ax.scatter(x,y,z,alpha=alpha,marker=marker)

        ax.set_xlabel(axis_labels[0])
        ax.set_xlim(axis_ranges[0])
        ax.set_ylabel(axis_labels[1])
        ax.set_ylim(axis_ranges[1])
        ax.set_zlabel(axis_labels[2])
        ax.set_zlim(axis_ranges[2])

        xy, xedges, yedges = np.histogram2d(x,y,bins=bins,range=(axis_ranges[0],axis_ranges[1]),normed=True)
        xcenters = (xedges[:-1] + xedges[1:])/2.
        ycenters = (yedges[:-1] + yedges[1:])/2.
        xmat = np.zeros((ycenters.shape[0],xcenters.shape[0]))
        ymat = np.zeros((ycenters.shape[0],xcenters.shape[0]))
        for i in range(ycenters.shape[0]):
                for j in range(xcenters.shape[0]):
                        xmat[i,j] = xcenters[j]
                        ymat[i,j] = ycenters[i]

        ax.contour(xmat,ymat,xy.T,levels,offset=axis_ranges[2][0],cmap=cm.coolwarm,linewidths=linewidths)

        xz, xedges, zedges = np.histogram2d(x,z,bins=bins,range=(axis_ranges[0],axis_ranges[2]),normed=True)
        xcenters = (xedges[:-1] + xedges[1:])/2.
        zcenters = (zedges[:-1] + zedges[1:])/2.
        xmat = np.zeros((zcenters.shape[0],xcenters.shape[0]))
        zmat = np.zeros((zcenters.shape[0],xcenters.shape[0]))
        for i in range(zcenters.shape[0]):
                for j in range(xcenters.shape[0]):
                        xmat[i,j] = xcenters[j]
                        zmat[i,j] = zcenters[i]

        ax.contour(xmat,xz.T,zmat,levels,offset=axis_ranges[1][1],zdir='y',cmap=cm.coolwarm,linewidths=linewidths)

        yz, yedges, zedges = np.histogram2d(y,z,bins=bins,range=(axis_ranges[1],axis_ranges[2]),normed=True)
        ycenters = (yedges[:-1] + yedges[1:])/2.
        zcenters = (zedges[:-1] + zedges[1:])/2.
        ymat = np.zeros((zcenters.shape[0],ycenters.shape[0]))
        zmat = np.zeros((zcenters.shape[0],ycenters.shape[0]))
        for i in range(zcenters.shape[0]):
                for j in range(ycenters.shape[0]):
                        ymat[i,j] = ycenters[j]
                        zmat[i,j] = zcenters[i]

        ax.contour(yz.T,ymat,zmat,levels,offset=axis_ranges[0][0],zdir='x',cmap=cm.coolwarm,linewidths=linewidths)

        plt.savefig('%s.png' %(system),dpi=600,transparent=True)
        plt.close()

def scatter_3d_density_cluster(x,y,z,cluster,centers,center_points,axis_labels,axis_ranges,alpha=0.01,marker='.',bins=200,levels=10,linewidths=0.1,system="system"):
        fig = plt.figure(figsize=(12,12),dpi=600,facecolor='w',edgecolor='k')
        ax = fig.gca(projection='3d')

	ax.scatter(centers[:,0],centers[:,1],centers[:,2],marker='s',s=60)
	ax.scatter(center_points[:][0],center_points[:][1],center_points[:][2],marker='s',s=60,c='k')
        ax.scatter(x,y,z,c=cluster,alpha=alpha,marker=marker,cmap='gist_rainbow')

        ax.set_xlabel(axis_labels[0])
        ax.set_xlim(axis_ranges[0])
        ax.set_ylabel(axis_labels[1])
        ax.set_ylim(axis_ranges[1])
        ax.set_zlabel(axis_labels[2])
        ax.set_zlim(axis_ranges[2])

        xy, xedges, yedges = np.histogram2d(x,y,bins=bins,range=(axis_ranges[0],axis_ranges[1]),normed=True)
        xcenters = (xedges[:-1] + xedges[1:])/2.
        ycenters = (yedges[:-1] + yedges[1:])/2.
        xmat = np.zeros((ycenters.shape[0],xcenters.shape[0]))
        ymat = np.zeros((ycenters.shape[0],xcenters.shape[0]))
        for i in range(ycenters.shape[0]):
                for j in range(xcenters.shape[0]):
                        xmat[i,j] = xcenters[j]
                        ymat[i,j] = ycenters[i]

        ax.contour(xmat,ymat,xy.T,levels,offset=axis_ranges[2][0],cmap=cm.coolwarm,linewidths=linewidths)

        xz, xedges, zedges = np.histogram2d(x,z,bins=bins,range=(axis_ranges[0],axis_ranges[2]),normed=True)
        xcenters = (xedges[:-1] + xedges[1:])/2.
        zcenters = (zedges[:-1] + zedges[1:])/2.
        xmat = np.zeros((zcenters.shape[0],xcenters.shape[0]))
        zmat = np.zeros((zcenters.shape[0],xcenters.shape[0]))
        for i in range(zcenters.shape[0]):
                for j in range(xcenters.shape[0]):
                        xmat[i,j] = xcenters[j]
                        zmat[i,j] = zcenters[i]

        ax.contour(xmat,xz.T,zmat,levels,offset=axis_ranges[1][1],zdir='y',cmap=cm.coolwarm,linewidths=linewidths)

        yz, yedges, zedges = np.histogram2d(y,z,bins=bins,range=(axis_ranges[1],axis_ranges[2]),normed=True)
        ycenters = (yedges[:-1] + yedges[1:])/2.
        zcenters = (zedges[:-1] + zedges[1:])/2.
        ymat = np.zeros((zcenters.shape[0],ycenters.shape[0]))
        zmat = np.zeros((zcenters.shape[0],ycenters.shape[0]))
        for i in range(zcenters.shape[0]):
                for j in range(ycenters.shape[0]):
                        ymat[i,j] = ycenters[j]
                        zmat[i,j] = zcenters[i]

        ax.contour(yz.T,ymat,zmat,levels,offset=axis_ranges[0][0],zdir='x',cmap=cm.coolwarm,linewidths=linewidths)

        plt.savefig('%s.png' %(system),dpi=600,transparent=True)
        plt.close()


name = "RADC"
nClusts = 100

file_name = "/Users/Ryan/Desktop/coumarin/coumarin_sandwich/simulated_annealing/replicate1/RADC/helical_param/%s.heli_parm.dat" %(name)
data1 = np.genfromtxt(file_name, usecols=(0,1,2,3,4,5))
data1 = np.array(data1)

km = KMeans(n_clusters=nClusts,random_state=0).fit(data1)
dist = km.transform(data1)

label = km.labels_
centers = km.cluster_centers_
center_points = []
index = []
pop = []

for i in range(nClusts):
	min = np.argmin(dist[:,i])
	center_points.append(data1[min])	
	index.append(min)
	pop.append(len(label[label==i]))

center_points = np.array(center_points)

xlim = (-10.0,10.0)
ylim = (-10.0,10.0)
zlim = (-10.0,10.0) 
axis_ranges = [xlim,ylim,zlim]
scatter_3d_density_cluster(data1[:,0],data1[:,1],data1[:,2],label,centers[:,0:3],center_points[:][0:3],("Slide","Shift","Rise"),axis_ranges,alpha=0.01,marker='.',bins=200,levels=10,linewidths=2.0,system="distances")
xlim = (-180.0,180.0)
ylim = (-180.0,180.0)
zlim = (-180.0,180.0) 
axis_ranges = [xlim,ylim,zlim]
scatter_3d_density_cluster(data1[:,3],data1[:,4],data1[:,5],label,centers[:,3:6],center_points[:,3:6],("Roll","Tilt","Twist"),axis_ranges,alpha=0.01,marker='.',bins=200,levels=10,linewidths=2.0,system="angles")

file = open(file_name,'r')
lines = file.readlines()

out = open("%s.cluster_centers.dat" %(name),'w')
for i,ind in enumerate(index):
	out.write("%10i   %s" %(pop[i],lines[ind]))

