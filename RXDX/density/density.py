import MDAnalysis as mda
import numpy as np
import sys
from MDAnalysis.analysis.align import *
import density

print density.__doc__

top_file = sys.argv[1]
traj_file = sys.argv[2]


u = mda.Universe(top_file,traj_file)

nAtoms = len(u.atoms)
nFrames = len(u.trajectory)
#nFrames = 50

align_sel = u.select_atoms("all")

u.atoms.translate(-align_sel.center_of_mass())
u.atoms.rotate(align_sel.atoms.principal_axes())
align_sel.write("align.pdb")

ref = mda.Universe("align.pdb")

CA_sel = u.select_atoms("name CA")

ARG_list = []
ASP_list = []
HYD_list = []

for i in range(20):
    ARG_list.append(i*16+1)
    HYD_list.append(i*16+2)
    ASP_list.append(i*16+3)
    HYD_list.append(i*16+4)
    ARG_list.append(i*16+5)
    HYD_list.append(i*16+6)
    ASP_list.append(i*16+7)
    HYD_list.append(i*16+8)
    ARG_list.append(i*16+9)
    HYD_list.append(i*16+10)
    ASP_list.append(i*16+11)
    HYD_list.append(i*16+12)
    ARG_list.append(i*16+13)
    HYD_list.append(i*16+14)
    ASP_list.append(i*16+15)
    HYD_list.append(i*16+16)

ARG_sel = []
for res in ARG_list:
    ARG_sel.append(u.select_atoms("resid %s and not (name C or name O or name CA or name HA or name N or name H)" %(res)))
ASP_sel = []
for res in ASP_list:
    ASP_sel.append(u.select_atoms("resid %s and not (name C or name O or name CA or name HA or name N or name H)" %(res)))
HYD_sel = []
for res in HYD_list:
    HYD_sel.append(u.select_atoms("resid %s and not (name C or name O or name CA or name HA or name N or name H)" %(res)))

nARG = len(ARG_sel)
nASP = len(ASP_sel)
nHYD = len(HYD_sel)
nRes = len(u.residues)

ARG_com = np.zeros((nFrames,nARG),dtype=float)
ASP_com = np.zeros((nFrames,nASP),dtype=float)
HYD_com = np.zeros((nFrames,nHYD),dtype=float)
CA_pos = np.zeros((nFrames,nRes),dtype=float)
box = u.dimensions[:3]


for ts in u.trajectory:
    if ts.frame < nFrames:
        print ts.frame
        u.atoms.translate(-align_sel.center_of_mass())
        R, d = rotation_matrix(u.atoms.positions,ref.atoms.positions)
        u.atoms.rotate(R)
        for res in range(nARG):
            ARG_com[ts.frame,res] = ARG_sel[res].atoms.center_of_mass()[0]
        for res in range(nASP):
            ASP_com[ts.frame,res] = ASP_sel[res].atoms.center_of_mass()[0]
        for res in range(nHYD):
            HYD_com[ts.frame,res] = HYD_sel[res].atoms.center_of_mass()[0]
        for ind,atom in enumerate(CA_sel.atoms):
            CA_pos[ts.frame,ind] = atom.position[0]

hist_min = -box[0]/2.0
hist_max = box[0]/2.0
bin_size = 0.2
num_bins = int((hist_max-hist_min)/bin_size)
hist = np.zeros((4,num_bins),dtype=float)

hist = density.density(ARG_com,ASP_com,HYD_com,CA_pos,hist_min,bin_size,num_bins,nFrames,nARG,nASP,nHYD,nRes)


out = open("out.dat",'w')
for bin in range(len(hist[0])):
    out.write("  %10.5f  %10.5f  %10.5f  %10.5f  %10.5f\n" %((bin+0.5)*bin_size+hist_min,hist[0,bin],hist[1,bin],hist[2,bin],hist[3,bin]))
out.close
