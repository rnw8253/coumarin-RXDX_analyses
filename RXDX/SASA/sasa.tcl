package require pbctools
mol new ../stripped/RADA8.stripped.prmtop
mol addfile ../stripped/RADA8.runXX.stripped.dcd first 0 step 1 waitfor all
set outfile [open sasa.runXX.dat w]
set nf [molinfo top get numframes]

set all   [atomselect top "protein"]
set sel1  [atomselect top "resid 1 to 160"]
set sel2  [atomselect top "resid 161 to 320"]

for {set i 0} {$i < $nf} {incr i} {
    $all frame $i
    $all update
    $sel1 frame $i
    $sel1 update
    $sel2 frame $i
    $sel2 update
    set sasa   [measure sasa 1.4 $all]
    set sasab  [measure sasa 1.4 $sel1]
    set sasac  [measure sasa 1.4 $sel2]
    puts $outfile [format "  %10.5f  %10.5f" $sasa $sasab $sasac ]

}
close $outfile

quit
