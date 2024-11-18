'''
Pseudocodigo:

n = nro de tiro

OPT(n) = max(OPT(n-1) + minimo entre los 2 extremos  , No OPT(n-1) + maximo entre los 2 extremos )

El no OPT(n-1) es la ganancia acumulada de mateo.

Es lo mismo que poner:

OPT(n) = max(OPT(n-1) + min(M(i), M(j))  , No OPT(n-1) + max(M(i), M(j)) )

i = inicio de la lista de monedas
j = fin de la lista 

M(i) = valor de moneda en la posicion i 
M(j) = valor de moneda en la posicion j

'''