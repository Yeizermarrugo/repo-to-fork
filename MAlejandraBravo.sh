#!/bin/bash
max=15
n_2=1
n_1=1
echo "Los primeros 15 numeros de Fibonacci son:"
echo 1 - ${n_2}
echo 2 - ${n_1}
i=3
while [ ${i} -le ${max} ]; do
n=$((${n_2} + ${n_1}))
n_2=${n_1}
n_1=${n}
echo ${i} - ${n}
i=$((${i}+1))
done

echo "Los primeros 15 numeros primos son:"
array=(2 3 5 7 11 13 17 19 23 29 31 37 41 43 53)
for i in ${array[@]}
do
        echo $i
done

