C FILE pdf.f
      SUBROUTINE density(ARG_com,ASP_com,HYD_com,CA_pos,nFrames,nARG,
     &     nASP,nHYD,nRes,hist,hist_min,bin_size,num_bins)
      
      double precision hist(4,num_bins),bin_size,hist_min
      integer nARG,nASP,nHYD,nRes
      double precision ARG_com(nFrames,nARG),ASP_com(nFrames,nASP)
      double precision HYD_com(nFrames,nHYD),CA_pos(nFrames,nRes)
      integer nFrames,res,step,num_bins,bin
     
Cf2py intent(in) ARG_com,ASP_com,HYD_com,CA_pos,nFrames,bin_size,num_bins
Cf2py intent(in) hist_min,nARG,nASP,nHYD,nRes
Cf2py intent(out) hist

      do step=1,nFrames
         do res=1,nARG
            bin=int((ARG_com(step,res) - hist_min)/bin_size)+1
            hist(1,bin) = hist(1,bin) + 1
         enddo
         do res=1,nASP
            bin=int((ASP_com(step,res)-hist_min)/bin_size)+1
            hist(2,bin) = hist(2,bin) + 1
         enddo
         do res=1,nHYD
            bin = int((HYD_com(step,res)-hist_min)/bin_size)+1
            hist(3,bin) = hist(3,bin) + 1
         enddo
         do res=1,nRes
            bin = int((CA_pos(step,res)-hist_min)/bin_size)+1
            hist(4,bin) = hist(4,bin) + 1
         enddo
      enddo
      RETURN
      END
C END OF pdf.f 
