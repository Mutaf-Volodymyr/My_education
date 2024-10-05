#!/bin/bash
set -e

for d in {1..10}
do
	date +"%H:%M:%S"
	ps -ef | wc -l
        sleep 1
	
done

cd /opt/290724-ptm/Mutaf/HW_15/
res="result.txt"

cat /proc/cpuinfo > $res
cat /etc/os-release | grep -w "NAME" >> $res
cat /etc/os-release | grep -w "NAME" | awk -F'"' '{print $2}' | awk '{print $1}' >> $res

for j in {50..100}
do 
	>> $j.txt
done

