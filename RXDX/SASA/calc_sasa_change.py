import numpy as np
import sys



mon_sasa = np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/monomer/RADA/SASA/sasa.total.dat")
agg_sasa = np.loadtxt("/Users/Ryan/Desktop/coumarin/sandwich/sim_annealing/replicate1/RADA/SASA/sasa.run00.dat")


mon_hyd_avg = np.average(mon_sasa[:,1])
mon_hyd_std = np.std(mon_sasa[:,1])
mon_tot_avg = np.average(mon_sasa[:,0])
mon_tot_std = np.std(mon_sasa[:,0])

print mon_hyd_avg*20,mon_hyd_std*20
print mon_tot_avg*20,mon_tot_std*20


agg_hyd_avg = np.average(agg_sasa[:,1])
agg_hyd_std = np.std(agg_sasa[:,1])
agg_tot_avg = np.average(agg_sasa[:,0])
agg_tot_std = np.std(agg_sasa[:,0])

print agg_hyd_avg,agg_hyd_std
print agg_tot_avg,agg_tot_std



hyd_diff = agg_hyd_avg - mon_hyd_avg*20
tot_diff = agg_tot_avg - mon_tot_avg*20 

hyd_diff_std = np.sqrt((20*mon_hyd_std)**2 + agg_hyd_std*agg_hyd_std) 
tot_diff_std = np.sqrt((20*mon_tot_std)**2 + agg_tot_std*agg_tot_std) 

print hyd_diff, hyd_diff_std

print tot_diff, tot_diff_std
