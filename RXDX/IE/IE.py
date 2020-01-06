import numpy as np
import MDAnalysis as mda
import sys
import IE
import math 

print IE.__doc__

def readNBparams(top_file):
    global  atom_type_index,nb_parm_index,lj_a_coeff,lj_b_coeff,n_types,n_excl_atoms,excl_atoms,nnb
    param = open(top_file,'r')
    pointers = np.zeros(31,dtype=np.int)
    lines = param.readlines()
    for i in range(len(lines)):
        if lines[i][0:14] == '%FLAG POINTERS':
            for j in range(4):
                temp = lines[i+2+j].split()
                for k in range(len(temp)):
                    pointers[j*10+k] = int(temp[k])
            n_atoms = pointers[0]
            n_types = pointers[1]
            nbonh = pointers[2]
            nnb = pointers[10]
            nbona = pointers[12]
            ntheth = pointers[4]
            ntheta = pointers[13]
            nphih = pointers[6]
            nphia = pointers[14]
            numbnd = pointers[15]
            numang = pointers[16]
            numtra = pointers[17]
            n_type_lines = int(math.ceil(n_atoms/10.))
            n_name_lines = int(math.ceil(n_atoms/20.))
            n_exc_lines = int(math.ceil(nnb/10.))
            n_nb_parm_lines = int(math.ceil(n_types*n_types/10.))
            n_lj_param_lines = int(math.ceil((n_types*(n_types+1)/2)/5.))
            atom_type_index = np.zeros((n_atoms),dtype=int)
            nb_parm_index = np.zeros(n_types*n_types,dtype=int)
            lj_a_coeff = np.zeros((n_types*(n_types+1))/2,dtype=float)
            lj_b_coeff = np.zeros((n_types*(n_types+1))/2,dtype=float)
            n_excl_atoms = np.zeros(n_atoms,dtype=int)
            excl_atoms = np.zeros(nnb,dtype=int)

        if lines[i][0:21] == '%FLAG ATOM_TYPE_INDEX':
            for j in range(n_type_lines):
                temp = lines[i+2+j].split()
                for k in range(len(temp)):
                    atom_type_index[j*10+k] = float(temp[k])
        if lines[i][0:26] == '%FLAG NONBONDED_PARM_INDEX':
            for j in range(n_nb_parm_lines):
                temp = lines[i+2+j].split()
                for k in range(len(temp)):
                    nb_parm_index[j*10+k] = float(temp[k])
        if lines[i][0:25] == '%FLAG LENNARD_JONES_ACOEF':
            for j in range(n_lj_param_lines):
                temp = lines[i+2+j].split()
                for k in range(len(temp)):
                    lj_a_coeff[j*5+k] = float(temp[k])
        if lines[i][0:25] == '%FLAG LENNARD_JONES_BCOEF':
            for j in range(n_lj_param_lines):
                temp = lines[i+2+j].split()
                for k in range(len(temp)):
                    lj_b_coeff[j*5+k] = float(temp[k])
        if lines[i][0:27] == '%FLAG NUMBER_EXCLUDED_ATOMS':
            for j in range(n_type_lines):
                temp = lines[i+2+j].split()
                for k in range(len(temp)):
                    n_excl_atoms[j*10+k] = float(temp[k])
        if lines[i][0:25] == '%FLAG EXCLUDED_ATOMS_LIST':
            for j in range(n_exc_lines):
                temp = lines[i+2+j].split()
                for k in range(len(temp)):
                    excl_atoms[j*10+k] = float(temp[k])



top_file = sys.argv[1]
traj_file = sys.argv[2]
out_file = sys.argv[3]

u = mda.Universe(top_file,traj_file)

readNBparams(top_file)

nRes_per_mol = 16
nAtoms = len(u.atoms)
nFrames = len(u.trajectory)
#nFrames = 1

alj = np.zeros((nAtoms,nAtoms),dtype=float)
blj = np.zeros((nAtoms,nAtoms),dtype=float)

for atom1 in range(len(u.atoms)):
    atom1_type = atom_type_index[atom1]
    for atom2 in range(atom1+1,len(u.atoms)):
        atom2_type = atom_type_index[atom2]
        index = (n_types*(atom1_type-1) + atom2_type) - 1
        NBP_index = nb_parm_index[index] - 1
        alj[atom1,atom2] = lj_a_coeff[NBP_index]
        blj[atom1,atom2] = lj_b_coeff[NBP_index]
        

res_type = []
mol_num_list = []
mol_num=0
types=[]
atom_index=0
charges=[]
res_type_index=1
last_resid=100
sheet_type = []
resid_list = []
for atom in u.atoms:
    # create array filled with all atom charges
    charges.append(atom.charge)

    if atom.resid <= 160:
        sheet_type.append(1)
    else:
        sheet_type.append(2)

    resid_list.append(atom.resid)

    # Determine Residue Type Label
    type_flag = True
    for type in range(len(types)):
        if atom.residue.resname == types[type][0]:
            type_flag = False
            res_type.append(types[type][1])
            
    if type_flag == True:
        types.append([atom.residue.resname,res_type_index])
        res_type.append(res_type_index)
        res_type_index += 1


nTypes = np.amax(res_type)
x = np.zeros((nFrames,nAtoms,3),float)
lbox = np.zeros((nFrames,3),float)
hlbox = np.zeros((nFrames,3),float)
Ec = np.zeros((nFrames,nTypes,nTypes),dtype=float)
Elj = np.zeros((nFrames,nTypes,nTypes),dtype=float)

for ts in u.trajectory:
    if ts.frame < nFrames:
        x[ts.frame] = u.atoms.positions
        lbox[ts.frame] = u.dimensions[:3]
        hlbox[ts.frame] = u.dimensions[:3]/2.0

Ec,Elj = IE.forces(lbox,hlbox,x,resid_list,res_type,charges,alj,blj,nTypes,excl_atoms,n_excl_atoms,nAtoms,nFrames,nnb)


out = open("%s.IE_coul.dat" %(out_file),'w')
out2 = open("%s.IE_vdw.dat" %(out_file),'w')

for step in range(nFrames):
    out.write("  %10.5f" %(step))
    out2.write("  %10.5f" %(step))

    for j in range(nTypes):
        for k in range(j,nTypes):
            out.write("  %10.5f" %(Ec[step,j,k]*332.0636))
            out2.write("  %10.5f" %(Elj[step,j,k]))
    out.write("\n")
    out2.write("\n")
out.close
out2.close


Ec = np.zeros((nFrames,nTypes,nTypes),dtype=float)
Elj = np.zeros((nFrames,nTypes,nTypes),dtype=float)

Ec,Elj = IE.sheet_forces(lbox,hlbox,x,resid_list,res_type,charges,alj,blj,nTypes,excl_atoms,n_excl_atoms,sheet_type,nAtoms,nFrames,nnb)

out = open("%s.IE_coul.sheet.dat" %(out_file),'w')
out2 = open("%s.IE_vdw.sheet.dat" %(out_file),'w')

for step in range(nFrames):
    out.write("  %10.5f" %(step))
    out2.write("  %10.5f" %(step))

    for j in range(nTypes):
        for k in range(j,nTypes):
            out.write("  %12.5f" %(Ec[step,j,k]*332.0636))
            out2.write("  %12.5f" %(Elj[step,j,k]))
    out.write("\n")
    out2.write("\n")
out.close
out2.close

