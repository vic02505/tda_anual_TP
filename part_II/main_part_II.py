'''
Pseudocodigo:

n = nro de tiro

OPT (i,j) = max(valor de moneda izq + OPT(i+1,j),valor de moneda der + OPT (i, j-1))


Es lo mismo que poner:

OPT (i,j) = max(monedas[i] + mejor_moneda_siguiente(i+1,j), monedas[j] + mejor_moneda_siguiente(i, j-1))

i = inicio de la lista de monedas, va variando segun la moneda que se seleccione
j = fin de la lista, va variando segun la moneda que se seleccione

monedas[i] = valor de moneda en la posicion i 
monedas[j] = valor de moneda en la posicion j



teniendo:
                   { 0            , si i+1 > j  // Osea si ya no le quedan monedas a sofia para agarrar
mejor_moneda_sig = { OPT(i+1, j)  , si monedas[i] >= monedas[j] // Mateo toma la moneda del lado izquierdo. Si es lo mismo, toma la de la izquierda  
                   { OPT(i, j-1)  , si moendas[i] < monedas[j] // Mateo toma la moneda del lado derecho

Se tiene una matriz de optimos M, siendo i las filas y j las columnas
Ejemplo de una matriz:

    0| 1| 2| 3| 4| 5
 0| 0| 0| 0| 0| 0| 0
 1| 0| 0| 0| 0| 0| 0
 2| 0| 0| 0| 0| 0| 0
 3| 0| 0| 0| 0| 0| 0
 4| 0| 0| 0| 0| 0| 0
 5| 0| 0| 0| 0| 0| 0


La matriz define el optimo de esa posicion en particular. Se rellena todo en 0 y se va actualizando.

La posicion de la fila 0 y ultima columna es donde se va a encontrar el optimo del ejercicio. Se parte de
esa posicion y se va calculando hacia atras hasta generar todos los calculos    

En el ejemplo de la matriz anterios, se empieza calculando el OPT(0,5) = M(0,5)

'''

import datasets_parser


def best_next_coin(ini, fin, gains_matrix, coins_list):
    if ini+1 > fin:
        return 0
    elif coins_list[ini] >= coins_list[fin]:
        return play_coins_game_partII(coins_list, gains_matrix, ini+1, fin)
    else:
        return play_coins_game_partII(coins_list, gains_matrix, ini, fin-1)
            




def play_coins_game_partII(coins_list, gains_matrix, i, j):

    if gains_matrix[i][j] == 0:
        gains_matrix[i][j] = max(coins_list[i] + best_next_coin(i+1, j, gains_matrix, coins_list), coins_list[j] + best_next_coin(i+1, j, gains_matrix, coins_list))
        return gains_matrix[i][j]
    else:
        return gains_matrix[i][j]



def coins_game_partII(coins_list):
    
    coins_list_len = len(coins_list)
        
    gains_matrix = [[0 for _ in range(coins_list_len)] for _ in range(coins_list_len)]

    play_coins_game_partII(coins_list, gains_matrix, 0, coins_list_len-1)
    
    print(gains_matrix)


def start_game():
    name_dataset = "5.txt"
    print("a")
    coins_list = datasets_parser("/datasets_part_II" + "/" + name_dataset)
    coins_game_partII(coins_list)


start_game()

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

# def coins_game_partII(coins_list):

#     coins_list_len = len(coins_list)

#     sophia_gains = [0]*(coins_list_len//2)
#     mateo_gains = [0]*(coins_list_len//2)

#     sophia_gains[0] = max(coins_list[0], coins_list[-1])
#     mateo_gains[0] = min(coins_list[0], coins_list[-1])




#     i = 0
#     j = coins_list_len - 1

#     for n in range(1, coins_list_len):
#         #OPT(n) = max(OPT(n-1) + min(M(i), M(j))  , No OPT(n-1) + max(M(i), M(j)) )
#         sophia_gains.append(max(sophia_gains[n-1] + min(coins_list[i], coins_list[j]), 3))

