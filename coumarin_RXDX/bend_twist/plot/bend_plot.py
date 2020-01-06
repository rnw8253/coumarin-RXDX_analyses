import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np 
import sys


def plot_polar(bend, rotdeg, rotrad, xlabel, ylabel, system):
    cm="hot_r"
    max = np.amax(bend)
    max = round(max,-1)
    bend_edges = np.linspace(0,90,50)
    rotrad_edges = np.linspace(0,2*np.pi,100)
    z, _, _ = np.histogram2d(bend,rotrad,[bend_edges,rotrad_edges],normed=True)
    Theta, R = np.meshgrid(rotrad_edges,bend_edges,sparse=False) 
    ax = plt.subplot(111,projection='polar')
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    plt.pcolormesh(Theta, R, z, cmap=cm,edgecolors="face")
    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    ax.set_rlabel_position(0)
    ax.set_rticks(np.arange(0,90,30))
    plt.xlabel(r"%s" %(xlabel), size=12)
    plt.ylabel(r"%s" %(ylabel), size=12, labelpad = 30)    
    plt.colorbar(pad = 0.1)
    #plt.savefig("polar_bend.%02d.pdf" %(index))
    plt.savefig("%s.polar.bend.pdf" %(system))
    plt.close()

    

    bend_edges = np.linspace(0,max,50)
    rotdeg_edges = np.linspace(0,360,50)
    z, _, _ = np.histogram2d(bend,rotdeg,[bend_edges,rotdeg_edges],normed=True)
    Theta, R = np.meshgrid(rotdeg_edges,bend_edges,sparse=False) 
    plt.pcolormesh(Theta,R,z,cmap=cm,edgecolors="face")
    plt.xlabel(r"%s" %(xlabel), size=12)
    plt.ylabel(r"%s" %(ylabel), size=12)    
    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    plt.xticks(np.arange(0,360,45))
    plt.colorbar()
#    plt.savefig("rect_bend.%02d.pdf" %(index))
    plt.savefig("%s.rect.bend.pdf" %(system))
    plt.close()

fiber_bend   = np.loadtxt("RADC.run49.fiber_bend_angle.dat")
fiber_rot    = np.loadtxt("RADC.run49.fiber_rot_angle.dat")
fiber_twist  = np.loadtxt("RADC.run49.fiber_twist_angle.dat")
strand_bend  = np.loadtxt("RADC.run49.strand_bend_angle.dat")
strand_rot   = np.loadtxt("RADC.run49.strand_rot_angle.dat")
strand_twist = np.loadtxt("RADC.run49.strand_twist_angle.dat")

rtd = np.pi/180

fiber_num_col = len(fiber_bend[0])
fiber_num_row = len(fiber_bend)
fiber_tot_bend = []
fiber_tot_rot = []
fiber_tot_twist = []
for col in range(fiber_num_col):
    for row in range(fiber_num_row):
        fiber_tot_bend.append(fiber_bend[row,col])
        fiber_tot_rot.append(fiber_rot[row,col])
        fiber_tot_twist.append(fiber_twist[row,col])

fiber_tot_bend = np.array(fiber_tot_bend)
fiber_tot_rot = np.array(fiber_tot_rot)
fiber_tot_twist = np.array(fiber_tot_twist)

strand_num_col = len(strand_bend[0])
strand_num_row = len(strand_bend)
strand_tot_bend = []
strand_tot_rot = []
strand_tot_twist = []
for col in range(strand_num_col):
    for row in range(strand_num_row):
        strand_tot_bend.append(strand_bend[row,col])
        strand_tot_rot.append(strand_rot[row,col])
        strand_tot_twist.append(strand_twist[row,col])

strand_tot_bend = np.array(strand_tot_bend)
strand_tot_rot = np.array(strand_tot_rot)
strand_tot_twist = np.array(strand_tot_twist)


#for i in range(len(rot[0])):
#    plot_polar(bend[:,i],rot[:,i],rot[:,i]*rtd,i)

#i=5
plot_polar(fiber_tot_bend[:],fiber_tot_rot[:],fiber_tot_rot[:]*rtd,"Rotation Angle ($\degree$)","Bend Angle ($\degree$)","RADC_fiber")
plot_polar(strand_tot_bend[:],strand_tot_rot[:],strand_tot_rot[:]*rtd,"Rotation Angle ($\degree$)","Bend Angle ($\degree$)","RADC_strand")

plot_polar(fiber_tot_bend[:],fiber_tot_twist[:]+180,fiber_tot_twist[:]*rtd+np.pi,"Twist Angle ($\degree$)","Bend Angle ($\degree$)","RADC_fiber.twist")
plot_polar(strand_tot_bend[:],strand_tot_twist[:]+180,strand_tot_twist[:]*rtd+np.pi,"Twist Angle ($\degree$)","Bend Angle ($\degree$)","RADC_strand.twist")

