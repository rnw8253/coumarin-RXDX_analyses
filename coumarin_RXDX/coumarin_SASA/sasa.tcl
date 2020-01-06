package require pbctools
mol new ../stripped/RADC.stripped.prmtop
mol addfile ../stripped/RADC.runXX.stripped.dcd first 0 step 1 waitfor all
set outfile [open sasa.runXX.dat w]
set nf [molinfo top get numframes]

set all   [atomselect top "protein"]
set sel1  [atomselect top "resname ALA"]
set sel2  [atomselect top "resname COU"]

for {set i 0} {$i < $nf} {incr i} {
    $all frame $i
    $all update
    $sel1 frame $i
    $sel1 update
    $sel2 frame $i
    $sel2 update
    set sasa   [measure sasa 1.4 $all]
    set sasab  [measure sasa 1.4 $all -restrict $sel1]
    set sasac  [measure sasa 1.4 $all -restrict $sel2]
    puts $outfile [format "  %10.5f  %10.5f  %10.5f" $sasa $sasab $sasac ]

}
close $outfile

quit

