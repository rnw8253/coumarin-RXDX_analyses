C FILE gofr_dist.f
      
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
C     Calculate three "principal axes" for each molecule for the given frame 
      SUBROUTINE ComputeBaseAxes(positions,nRes,axes)
      integer res, nRes, j
      double precision positions(nRes,3,3)
      double precision r1(3),r2(3),r3(3),t1(3)
      double precision Dot,norm,axes(nRes,3,3)

Cf2py intent(in) nRes, positions
Cf2py intent(out) axes


C     Determine axes using the 3 selections provides in positions
      do res=1,nRes
         do j = 1,3
            r1(j) = positions(res,2,j) - positions(res,1,j)
         enddo
         norm = sqrt(Dot(r1,r1))
         r1 = r1/norm
         do j = 1,3
            t1(j) = positions(res,3,j) - positions(res,1,j)
         enddo
         norm = sqrt(Dot(t1,t1))
         t1 = t1/norm
         call Cross(r1,t1,r3)
         norm = sqrt(Dot(r3,r3))
         r3 = r3/norm
         call Cross(r3,r1,r2)
         norm = sqrt(Dot(r2,r2))
         r2 = r2/norm
         
C     Save the axes for each molecule
         do j =1,3
            axes(res,1,j) = r1(j)
            axes(res,2,j) = r2(j)
            axes(res,3,j) = r3(j)
         enddo
      enddo
      
      RETURN
      
      END SUBROUTINE
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
      SUBROUTINE computeRotationMatrix(R, v, theta_2)
       double precision R(3,3), theta_2, v(3)

Cf2py intent(in) v, theta_2
Cf2py intent(out) R
 
       R(1,1)=cos(theta_2)+v(1)*v(1)*(1-cos(theta_2))
       R(1,2)=v(1)*v(2)*(1-cos(theta_2))-v(3)*sin(theta_2)
       R(1,3)=v(1)*v(3)*(1-cos(theta_2))+v(2)*sin(theta_2)
       R(2,1)=v(2)*v(1)*(1-cos(theta_2)) + v(3)*sin(theta_2)
       R(2,2)=cos(theta_2) + v(2)*v(2)*(1-cos(theta_2))
       R(2,3)=v(2)*v(3)*(1-cos(theta_2)) - v(1)*sin(theta_2)
       R(3,1)=v(3)*v(1)*(1-cos(theta_2)) - v(2)*sin(theta_2)
       R(3,2)=v(3)*v(2)*(1-cos(theta_2))+v(1)*sin(theta_2)
       R(3,3)=cos(theta_2)+v(3)*v(3)*(1-cos(theta_2))

       RETURN 
       
       END SUBROUTINE

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
      SUBROUTINE CalculateHelicalParams(pair_axes,dist_vec,rise,shift,
     &     slide,roll,tilt,twist)
       integer j
       double precision pair_axes(2,3,3),dist_vec(3),Dot,r3p(3)
       double precision radians_to_degrees,sin_roll,cos_roll
       double precision sin_tilt,cos_tilt,sin_twist,cos_twist
       double precision slide,shift,rise,roll,tilt,twist
       double precision temp(3),temp1(3),temp2(3),temp3(3)
       double precision norm

Cf2py intent(in) pair_axes,dist_vec
Cf2py intent(out) rise,shift,slide,roll,tilt,twist 
 
       radians_to_degrees = 180.0/3.1415926535
       do j=1,3
          temp(j) = pair_axes(1,1,j)
       enddo
       slide = Dot(dist_vec,temp)
       do j=1,3
          temp(j) = pair_axes(1,2,j)
       enddo
       shift = Dot(dist_vec,temp)
       do j=1,3
          temp(j) = pair_axes(1,3,j)
       enddo
       rise  = Dot(dist_vec,temp)

C     Calculate Roll
       do j=1,3
          temp1(j)= pair_axes(2,3,j)
          temp2(j)= pair_axes(1,2,j)
          temp3(j)= pair_axes(1,3,j)
       enddo
       do j=1,3
          r3p(j) = Dot(temp1,temp2)*pair_axes(1,2,j)+
     &         Dot(temp1,temp3)*pair_axes(1,3,j)
       enddo
       norm = sqrt(Dot(r3p,r3p))
       r3p = r3p/norm
       cos_roll = Dot(r3p,temp3)
       sin_roll = Dot(r3p,temp2)
       roll = ATAN2(sin_roll,cos_roll)*radians_to_degrees
C     Calculate Tilt
       do j=1,3
          temp1(j)= pair_axes(2,3,j)
          temp2(j)= pair_axes(1,1,j)
          temp3(j)= pair_axes(1,3,j)
       enddo
       do j=1,3
          r3p(j) = Dot(temp1,temp2)*pair_axes(1,1,j)+
     &         Dot(temp1,temp3)*pair_axes(1,3,j)
       enddo
       norm = sqrt(Dot(r3p,r3p))
       r3p = r3p/norm
       cos_tilt = Dot(r3p,temp3)
       sin_tilt = Dot(r3p,temp2)
       tilt = ATAN2(sin_tilt,cos_tilt)*radians_to_degrees

C     Calculate Twist
       do j=1,3
          temp1(j)= pair_axes(2,2,j)
          temp2(j)= pair_axes(1,1,j)
          temp3(j)= pair_axes(1,2,j)
       enddo
       do j=1,3
          r3p(j) = Dot(temp1,temp2)*pair_axes(1,1,j)+
     &         Dot(temp1,temp3)*pair_axes(1,2,j)
       enddo
       norm = sqrt(Dot(r3p,r3p))
       r3p = r3p/norm
       cos_twist = Dot(r3p,temp3)
       sin_twist = Dot(r3p,temp2)
       twist = ATAN2(sin_twist,cos_twist)*radians_to_degrees


       RETURN

       END SUBROUTINE

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
