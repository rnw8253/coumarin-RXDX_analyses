import MDAnalysis as mda
import numpy as np
import sys
import math
from MDAnalysis.analysis.align import *
import dimer_ang

print dimer_ang.__doc__

#############################################################

top_file = sys.argv[1]
traj_file = sys.argv[2]
out_file = sys.argv[3]

cutoff = 7.5
radians_to_degrees = 180/np.pi
u = mda.Universe(top_file,traj_file)

res_sel = u.select_atoms("resname COU")
nRes = len(res_sel.residues)
nSteps = len(u.trajectory)
sel = []
sel2 = []

for res in res_sel.residues:
    temp = []
    temp.append(u.select_atoms("resid %s and (name CE1 or name CD1)" %(res.resid)))
    temp.append(u.select_atoms("resid %s and (name CH2 or name CZ3)" %(res.resid)))
    temp.append(u.select_atoms("resid %s and name CD2" %(res.resid)))
    sel.append(temp)
    sel2.append(u.select_atoms("resid %s and not (name C or name O or name CA or name N or name H or name HA or name CB or name HB2 or name HB3)" %(res.resid)))

out = open("%s.dimer_angles.dat" %(out_file) ,'w')
for ts in u.trajectory:
    print "step %s" %(ts.frame+1)
    box = u.dimensions[:3]
    box_2 = box/2.0
    positions = np.zeros((nRes,3,3),dtype=float)
    coms = np.zeros((nRes,3),dtype=float)
    frame = ts.frame
    for res in range(nRes):
        for i in range(3):
            positions[res][i] = sel[res][i].center_of_mass()
        coms[res] = sel2[res].center_of_mass()

    for res1 in range(nRes):
        for res2 in range(res1+1,nRes):
            distance,dist_vec = dimer_ang.computepbcdist2_vec(coms[res1],coms[res2],box,box_2)
            if distance <= cutoff:
                alpha1,alpha2,beta = dimer_ang.computeangles(positions[res1][0],positions[res1][1],positions[res2][0],positions[res2][1],dist_vec)
                out.write("%10.5f %10.5f %10.5f %10.5f\n" %(distance,alpha1,alpha2,beta))
out.close
