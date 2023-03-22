#!/bin/bash
cd /clusterfs/Documents/weather
j=1;
#while [ j==1 ]
#        do
        curl -s http://celsius.met.uu.se/data/obs_Marsta.htm |
        awk 'NR==1 {gsub("-"," ",$4);gsub(":"," ",$5);printf("%10s%6s",$4,$5)} NR>1 {gsub(">"," ",$0);gsub("<"," ",$0)} /right/ {printf("%7s", $3)} END{ printf("\n")}'>> vaderM
#        sleep 600
#done

