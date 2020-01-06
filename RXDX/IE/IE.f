CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
      SUBROUTINE forces(nAtoms,lbox,hlbox,x,resid_list,
     &     res_type,charges,alj,blj,Ec,Elj,nFrames,nTypes,excl_atoms,
     &     nnb,n_excl_atoms)

        double precision Ec(nFrames,nTypes,nTypes)
        double precision Elj(nFrames,nTypes,nTypes)
        double precision x(nFrames,nAtoms,3)
        double precision lbox(nFrames,3),hlbox(nFrames,3)
        integer nAtoms,nFrames, resid_list(nAtoms),res_type(nAtoms)
        double precision charges(nAtoms)
        double precision alj(nAtoms,nAtoms),blj(nAtoms,nAtoms)
        integer step,nnb,nTypes,iex,atom_excl_count
        double precision pos1(3),pos2(3)
        double precision excl_atoms(nnb)
        double precision dx,r2,r6,Ecoul,Evdw
        double precision n_excl_atoms(nAtoms)

Cf2py intent(in) nAtoms,nFrames,lbox,hlbox,x,resid_list,res_type
Cf2py intent(in) charges,alj,blj,excl_atoms,nnb,nTypes,n_excl_atoms
Cf2py intent(out) Ec, Elj
        
        do step=1,nFrames
           iex = 1
           do i=1,nAtoms
              atom_excl_count = 0
              if(i.le.110) then
              endif
              do j=i+1,nAtoms
                 if (excl_atoms(iex).ne.j) then
                    if (resid_list(i).ne.resid_list(j)) then
                       r2=0.d0
                       do k=1,3
                          dx=x(step,i,k)-x(step,j,k)
                          pos1(k) = x(step,i,k)
                          pos2(k) = x(step,j,k)
                          if (dx.gt.hlbox(step,k)) then
                             dx=dx-lbox(step,k)
                          endif
                          if (dx.lt.-hlbox(step,k)) then
                             dx=dx+lbox(step,k)
                          endif
                          r2=r2+dx*dx
                       enddo
                       if(r2.lt.144) then
                          r6=r2**(-3)
                          Evdw=r6*(alj(i,j)*r6 - blj(i,j))
                          Ecoul=charges(i)*charges(j)/(dsqrt(r2))
                          if (Evdw.gt.1000) then
                             write(6,*) i,j,Evdw
                          endif
                          Ec(step,res_type(i),res_type(j))=Ec(
     &                         step,res_type(i),res_type(j))+Ecoul
                          Elj(step,res_type(i),res_type(j))=Elj(
     &                         step,res_type(i),res_type(j))+Evdw
                          if(res_type(i).ne.res_type(j)) then
                             Ec(step,res_type(j),res_type(i))=Ec(
     &                            step,res_type(j),res_type(i))+Ecoul                          
                             Elj(step,res_type(j),res_type(i))=Elj(
     &                            step,res_type(j),res_type(i))+Evdw                             
                          endif
                       endif
                    endif
                 else
                    atom_excl_count = atom_excl_count + 1
                    if(atom_excl_count.ne.n_excl_atoms(i)) then
                       iex=iex+1
                    endif
                 endif
              enddo
              iex=iex+1
           enddo
           write(6,*)  step
        enddo
       
        END SUBROUTINE


CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
      SUBROUTINE sheet_forces(nAtoms,lbox,hlbox,x,resid_list,
     &     res_type,charges,alj,blj,Ec,Elj,nFrames,nTypes,excl_atoms,
     &     nnb,n_excl_atoms,sheet_type)

        double precision Ec(nFrames,nTypes,nTypes)
        double precision Elj(nFrames,nTypes,nTypes)
        double precision x(nFrames,nAtoms,3)
        double precision lbox(nFrames,3),hlbox(nFrames,3)
        integer nAtoms,nFrames, resid_list(nAtoms),res_type(nAtoms)
        double precision charges(nAtoms)
        double precision alj(nAtoms,nAtoms),blj(nAtoms,nAtoms)
        integer step,nnb,nTypes,iex,atom_excl_count
        double precision pos1(3),pos2(3)
        double precision excl_atoms(nnb)
        double precision dx,r2,r6,Ecoul,Evdw
        double precision n_excl_atoms(nAtoms)
        double precision sheet_type(nAtoms)

Cf2py intent(in) nAtoms,nFrames,lbox,hlbox,x,resid_list,res_type,sheet_type
Cf2py intent(in) charges,alj,blj,excl_atoms,nnb,nTypes,n_excl_atoms
Cf2py intent(out) Ec, Elj
        
        do step=1,nFrames
           iex = 1
           do i=1,nAtoms
              atom_excl_count = 0
              do j=i+1,nAtoms
                 if (excl_atoms(iex).ne.j) then
                    if(sheet_type(i).ne.sheet_type(j)) then
                       if (resid_list(i).ne.resid_list(j)) then
                          r2=0.d0
                          do k=1,3
                             dx=x(step,i,k)-x(step,j,k)
                             pos1(k) = x(step,i,k)
                             pos2(k) = x(step,j,k)
                             if (dx.gt.hlbox(step,k)) then
                                dx=dx-lbox(step,k)
                             endif
                             if (dx.lt.-hlbox(step,k)) then
                                dx=dx+lbox(step,k)
                             endif
                             r2=r2+dx*dx
                          enddo
                          if(r2.lt.144) then
                             r6=r2**(-3)
                             Evdw=r6*(alj(i,j)*r6 - blj(i,j))
                             Ecoul=charges(i)*charges(j)/(dsqrt(r2))
                             Ec(step,res_type(i),res_type(j))=Ec(
     &                            step,res_type(i),res_type(j))+Ecoul
                             Elj(step,res_type(i),res_type(j))=Elj(
     &                            step,res_type(i),res_type(j))+Evdw
                             if(res_type(i).ne.res_type(j)) then
                                Ec(step,res_type(j),res_type(i))=Ec(
     &                               step,res_type(j),res_type(i))+Ecoul                          
                                Elj(step,res_type(j),res_type(i))=Elj(
     &                               step,res_type(j),res_type(i))+Evdw                             
                             endif
                          endif
                       endif
                    endif
                 else
                    atom_excl_count = atom_excl_count + 1
                    if(atom_excl_count.ne.n_excl_atoms(i)) then
                       iex=iex+1
                    endif
                 endif
              enddo
              iex=iex+1
           enddo
           write(6,*)  step
        enddo
       
        END SUBROUTINE

