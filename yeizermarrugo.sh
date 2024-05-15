#!/bin/bash

# Función para generar los primeros n números de la serie de Fibonacci
fibonacci() {
    local n=$1
    local a=0
    local b=1
    local i=0

    echo -n "Los primeros $n números de la serie de Fibonacci son: "

    while [ $i -lt $n ]; do
        echo -n "$a "
        fn=$((a + b))
        a=$b
        b=$fn
        i=$((i + 1))
    done
    echo
}

# Función para verificar si un número es primo
es_primo() {
    local num=$1
    if [ $num -lt 2 ]; then
        return 1
    fi
    for ((i = 2; i <= num / 2; i++)); do
        if [ $((num % i)) -eq 0 ]; then
            return 1
        fi
    done
    return 0
}

# Función para generar los primeros n números primos
primeros_primos() {
    local n=$1
    local count=0
    local num=2

    echo -n "Los primeros $n números primos son: "

    while [ $count -lt $n ]; do
        if es_primo $num; then
            echo -n "$num "
            count=$((count + 1))
        fi
        num=$((num + 1))
    done
    echo
}

# Función para verificar si un número es perfecto
es_perfecto() {
    local num=$1
    local suma=0

    for ((i = 1; i < num; i++)); do
        if [ $((num % i)) -eq 0 ]; then
            suma=$((suma + i))
        fi
    done

    if [ $suma -eq $num ]; then
        return 0
    else
        return 1
    fi
}

# Función para generar los primeros n números perfectos
primeros_perfectos() {
    local n=$1
    local count=0
    local num=2

    echo -n "Los primeros $n números perfectos son: "

    while [ $count -lt $n ]; do
        if es_perfecto $num; then
            echo -n "$num "
            count=$((count + 1))
        fi
        num=$((num + 1))
    done
    echo
}

# Llamada a las funciones
fibonacci 15
primeros_primos 15
primeros_perfectos 5
