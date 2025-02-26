'''
Pseudocodigo:

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
from common_libs import datasets_parser
from part_I.greedy_coins_game import coins_game


def best_next_coin(i, j, gains_matrix, coins_list):
    if i+1 >j:
        return 0
    elif coins_list[i] >= coins_list[j]:
        return gains_matrix[i+1][j]
    else:
        return gains_matrix[i][j-1]

def reconstruct_solution(coins_list, gains_matrix):
    i = 0 
    j = len(coins_list) - 1
    choices_sophia = []  # Lista para almacenar el orden de elecciones de monedas
    choices_mateo = []

    while i <= j:
        left_option = coins_list[i] + best_next_coin(i+1, j, gains_matrix, coins_list)
        right_option = coins_list[j] + best_next_coin(i, j-1, gains_matrix, coins_list)
        
        if left_option >= right_option:
            choices_sophia.append(coins_list[i])
            i += 1
            if i > j: # No quedan mas monedas
                continue
            if coins_list[i] >= coins_list[j]:
                choices_mateo.append(coins_list[i])
                i += 1
            else:
                choices_mateo.append(coins_list[j])
                j-= 1
        else:
            choices_sophia.append(coins_list[j])
            j -= 1
            if i > j: #No quedan mas monedas
                continue
            if coins_list[i] >= coins_list[j]:
                choices_mateo.append(coins_list[i])
                i += 1
            else:
                choices_mateo.append(coins_list[j])
                j-= 1

    return choices_sophia, choices_mateo


def get_gains_matrix(coins_list):

    coins_list_len = len(coins_list)

    gains_matrix = [[0 for _ in range(coins_list_len)] for _ in range(coins_list_len)]

    for i in range(coins_list_len-1, 0, -1):

        for j in range(0, coins_list_len):

            if  i > j:
                gains_matrix[i][j] = 0
            else:
                gains_matrix[i][j] = max(coins_list[i] + best_next_coin(i+1, j, gains_matrix, coins_list),
                                 coins_list[j] + best_next_coin(i, j-1, gains_matrix, coins_list))

    # Esto se puede poner más lindo. El tema es que la iteración anterior llega hasta "i" igual a uno porque
    # el cero del primer for (el que itera i) es excluyente. Por eso se hace este for aparte
    for j in range(0, coins_list_len):
        i = 0
        gains_matrix[i][j] = max(coins_list[i] + best_next_coin(i + 1, j, gains_matrix, coins_list),
                            coins_list[j] + best_next_coin(i, j - 1, gains_matrix, coins_list))

    return gains_matrix

def start_game(dataset):
    gains_matrix =  get_gains_matrix(dataset)
    coins_sophia, coins_mateo = reconstruct_solution(dataset, gains_matrix)
#    for i in range(len(coins)):
#        if i % 2 == 0: # Siempre empieza Sophia agarrando la primera moneda
#            coins_sophia.append(coins[i])
#        else:
#            coins_mateo.append(coins[i])    

    return gains_matrix[0][len(dataset)-1], coins_sophia, coins_mateo

def run_use_case(dataset):
    sophia_gains, coins_sophia, coins_mateo = start_game(dataset)
    return sophia_gains, coins_sophia, coins_mateo

