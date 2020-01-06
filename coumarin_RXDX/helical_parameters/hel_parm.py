import MDAnalysis as mda
import numpy as np
import sys
import math
from MDAnalysis.analysis.align import *
import heli_parm_funcs

print heli_parm_funcs.__doc__

def computePrincipalAxes(selection,nRes):
    axes = np.zeros((nRes,3,3),dtype=float)
    for res in range(nRes):
        axes[res] = selection.residues[res].atoms.principal_axes()
        
    return axes

def computeHalfRotAxes(axes,res1,res2):
    pair_axes = np.zeros((2,3,3),dtype=float)
    v = np.zeros(3,dtype=float)
    R = np.zeros((3,3),dtype=float)
    R_full = np.zeros((3,3),dtype=float)

    rot_mat, RMSD=rotation_matrix(axes[res1],axes[res2])
    values, vectors = np.linalg.eig(rot_mat)
    idx = values.argsort()[::-1]
    values = values[idx]

    vectors = vectors[:,idx]

    v[0] = vectors[0,0]
    v[1] = vectors[1,0]
    v[2] = vectors[2,0]

    theta = np.arccos((np.matrix.trace(rot_mat) - 1)/2.0)
    theta_2 = -theta
    R_full = heli_parm_funcs.computerotationmatrix(v, theta_2)
    if np.allclose(R_full,rot_mat):
        theta_2 = -theta/2.0
        R = heli_parm_funcs.computerotationmatrix(v, theta_2)
    else:
        theta_2 = theta
        R_full = heli_parm_funcs.computerotationmatrix(v, theta_2)
        if np.allclose(R_full,rot_mat):
            theta_2 = theta/2.0
            R = heli_parm_funcs.computerotationmatrix(v, theta_2)
        else:
            print error
            quit()
    pair_axes[1] = axes[res2]
    pair_axes[0] = np.dot(R,axes[res1].T).T

    return pair_axes

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

res_num = []
for res in res_sel.residues:
    res_num.append(res.resid)
    temp = []
    temp.append(u.select_atoms("resid %s and (name CE1 or name CD1)" %(res.resid)))
    temp.append(u.select_atoms("resid %s and (name CH2 or name CZ3)" %(res.resid)))
    temp.append(u.select_atoms("resid %s and name CD2" %(res.resid)))
    sel.append(temp)
    sel2.append(u.select_atoms("resid %s and not (name C or name O or name CA or name N or name H or name HA or name CB or name HB2 or name HB3)" %(res.resid)))

rise=0
roll=0
shift=0
slide=0
tilt=0
twist=0
out = open("%s.heli_param2.dat" %(out_file) ,'w')
base_axes = np.zeros((nRes,3,3))
count = 0
for ts in u.trajectory:
    print "step %s" %(ts.frame+1)
    base_axes = np.zeros((nRes,3,3),dtype=float)
    base_axes[0,0,1] = 5.0
    box = u.dimensions[:3]
    box_2 = box/2.0
    positions = np.zeros((nRes,3,3),dtype=float)
    coms = np.zeros((nRes,3),dtype=float)
    frame = ts.frame
    for res in range(nRes):
        for i in range(3):
            positions[res][i] = sel[res][i].center_of_mass()
            coms[res] = sel2[res].center_of_mass()
    base_axes = heli_parm_funcs.computebaseaxes(positions,nRes)
    for res1 in range(nRes):
        for res2 in range(res1+1,nRes):
            distance,dist_vec = heli_parm_funcs.computepbcdist2_vec(coms[res1],coms[res2],box,box_2)
            if distance <= cutoff:

                pair_axes = np.zeros((2,3,3),dtype=float)
                pair_axes[0] = base_axes[res1]
                pair_axes[1] = base_axes[res2]

                rise, shift, slide, roll, tilt, twist = heli_parm_funcs.calculatehelicalparams(pair_axes,dist_vec)
                out.write("%8.3f %8.3f %8.3f %8.3f %8.3f  %8.3f  %s  %8i  %8i  %8i\n" %(slide,shift,rise,roll,tilt,twist,out_file,ts.frame,res_num[res1],res_num[res2]))
                count += 1
out.close
