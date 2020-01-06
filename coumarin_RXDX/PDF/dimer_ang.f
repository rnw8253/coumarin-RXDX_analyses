C FILE gofr_dist.f
      

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
      
      SUBROUTINE  computepbcdist2_vec(r1,r2,box,box_2,distance,vec)

      integer j
      double precision r1(3),r2(3),box(3),box_2(3),vec(3),distance
      double precision temp

Cf2py intent(in) r1,r2,box,box_2
Cf2py intent(out) distance,vec

      distance = 0
      do j=1,3
         temp = r1(j) - r2(j)
         if (temp.le.-box_2(j)) then
            temp = temp+box(j)
         endif
         if (temp.ge.box_2(j)) then
            temp = temp-box(j)
         endif
         distance=distance+temp*temp
         vec(j) = temp
      enddo
      distance=sqrt(distance)
      RETURN 
      
      END SUBROUTINE

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
C     calculate 3 angles for spectra calculation
      SUBROUTINE ComputeAngles(r1a,r1b,r2a,r2b,dist_vec,alpha1,alpha2
     &     ,beta)
      
      integer j
      double precision r1a(3),r1b(3),r2a(3),r2b(3)
      double precision vec1(3),vec2(3)
      double precision dist_vec(3),Dot
      double precision vec1_norm(3),vec2_norm(3)
      double precision dist_vec_norm(3),norm
      double precision alpha1,alpha2,beta
      double precision rad_to_degs
Cf2py intent(in) r1a,r2a,r1b,r2b,dist_vec
Cf2py intent(out) alpha1,alpha2,beta

      rad_to_degs = 180/3.14159265359
      do j=1,3
         vec1(j) = r1b(j) - r1a(j)
         vec2(j) = r2b(j) - r2a(j)
      enddo
C      write(6,*) vec2
      norm = sqrt(Dot(vec1,vec1))
      vec1_norm = vec1/norm
      norm = sqrt(Dot(vec2,vec2))
      vec2_norm = vec2/norm
      norm = sqrt(Dot(dist_vec,dist_vec))
      dist_vec_norm = dist_vec/norm
C      write(6,*) vec1_norm,vec2_norm,dist_vec_norm

      
      alpha1 = ACOS(Dot(vec1_norm,dist_vec_norm))*rad_to_degs
      alpha2 = ACOS(Dot(vec2_norm,dist_vec_norm))*rad_to_degs
      beta = ACOS(Dot(vec1_norm,vec2_norm))*rad_to_degs


      END SUBROUTINE


CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
      
      SUBROUTINE  Cross(A,B,C)
      integer j
      double precision A(3),B(3),C(3)

      do j=1,3
         C(j)=0
      enddo
      C(1) = A(2) * B(3) - A(3) * B(2)
      C(2) = A(3) * B(1) - A(1) * B(3)
      C(3) = A(1) * B(2) - A(2) * B(1)

      RETURN 

      END SUBROUTINE
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
      double precision FUNCTION  Dot(A,B)

      integer j
      double precision A(3),B(3)

      Dot=0
      do j=1,3
         Dot=Dot+A(j)*B(j)
      enddo

      END FUNCTION
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
