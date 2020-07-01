#! /bin/bash
START_IDX=7800
MAX_IDX=10000
ITER=$(seq $START_IDX $MAX_IDX)
LANG=ko

for i in $ITER
do
{	
res=$(curl -w '%{http_code}' -s -o /dev/null "https://cdn.intra.42.fr/pdf/pdf/$i/$LANG.subject.pdf") 
if [ $res -ne 404 ]
then
	echo "https://cdn.intra.42.fr/pdf/pdf/$i/$LANG.subject.pdf"
fi
} &
done

wait
