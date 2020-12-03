echo "Alan Grosso contribution"

nmax = 15
for x in range(2, nmax):
    for i in range(2, x):
        if x%i != 0:
            #i no es divisor de x, x puede ser primo
            continue
        else:
            #i es divisor de x, x no es primo
            break #No es necesario buscar más divisores
    else:
        #El bucle for ha terminado con normalidad
        #El número que estábamos comprobando es primo
        print ('%d es primo'%x)