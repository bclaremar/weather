#!/bin/bash
t=($(./ma.sh |  awk '{print $2}'))
c1=($(./ma.sh |  awk '{print $(NF-2)}'))
c2=$(./ma.sh |  awk '{print $(NF-3)}')
c3=$(./ma.sh |  awk '{print $(NF-4)}')
#c4=$(./ma.sh |  awk '{print $(NF-5)}')
#c5=$(./ma.sh |  awk '{print $(NF-6)}')
#c6=$(./ma.sh |  awk '{print $(NF-7)}')

j=0
for i in ${c1[@]}
do
	if [[ "$i" == "NCD" || $i == "CAVOK" ]];then
		i="nan"
	fi
#	echo $t[$j]
	printf "%s\t%s\t%s\n" $t[j] $i $c2[j]
	j=(expr $j+1)
done


