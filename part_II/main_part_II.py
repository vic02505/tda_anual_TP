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

def coins_game_partII(coins_list):

    coins_list_len = len(coins_list)

    sophia_gains = [0]*(coins_list_len//2)
    mateo_gains = [0]*(coins_list_len//2)

    sophia_gains[0] = max(coins_list[0], coins_list[-1])
    mateo_gains[0] = min(coins_list[0], coins_list[-1])




    i = 0
    j = coins_list_len - 1

    for n in range(1, coins_list_len):
        #OPT(n) = max(OPT(n-1) + min(M(i), M(j))  , No OPT(n-1) + max(M(i), M(j)) )
        sophia_gains.append(max(sophia_gains[n-1] + min(coins_list[i], coins_list[j]), 3))


