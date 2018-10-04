gpio mode 0 out
gpio write 0 1

gpio mode 1 out
gpio write 1 1

#1/bin/bash

counter=1
gpio mode 0 out
gpio mode 1 out
while [ $counter -le 20 ]

do
 gpio write 0 1
 sleep 1
 ((counter ++))
 gpio write 0 0
 sleep 1

 gpio write 1 1
 sleep 1
 ((counter ++))
 gpio write 1 0
 sleep 1

done

echo "hi"
