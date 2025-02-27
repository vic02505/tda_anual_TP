''' 
Demostracion de complejidad de cada funcion que se utiliza para verificar polinomialmente
el problema de la batalla naval
'''

def validar_adyacencia_abajo(tablero, i, j):
    """
    Complejidad: O(1)
    """
    
    if j+1 < len(tablero[0]) and tablero[i][j+1]:
        return False

    if j-1 >= 0 and tablero[i][j-1]:
        return False

    return validar_diagonal(tablero, i, j)

def validar_adyacencia_derecha(tablero, i, j):
    """
    Complejidad: O(1)
    """
    
    if i+1 < len(tablero) and tablero[i+1][j]:
        return False
    
    if i-1 >= 0 and tablero[i-1][j]:
        return False

    return validar_diagonal(tablero, i, j)

def validar_diagonal(tablero, i, j):
    """
    Complejidad: O(1)
    """

    if i+1 < len(tablero) and j+1 < len(tablero[0]):
        if tablero[i+1][j+1]:
            return False

    if i+1 < len(tablero) and j-1 >= 0:
        if tablero[i+1][j-1]:
            return False

    if i-1 >= 0 and j+1 < len(tablero[0]):
        if tablero[i-1][j+1]:
            return False
        
    if i-1 >= 0 and j-1 >= 0:
        if tablero[i-1][j-1]:
            return False

    return True

def buscar_barco_a_la_derecha(tablero, i, j, tamanio_barco):
    """
    Complejidad: O(m)
    """
    for k in range(j, len(tablero[0])):   # O(m)
        if not tablero[i][k]:
            break
        
        if not validar_adyacencia_derecha(tablero, i, k):
            return False

        tablero[i][k] = 0
        tamanio_barco[0] += 1

    return True

def buscar_barco_para_abajo(tablero, i, j, tamanio_barco):
    """
    Complejidad: O(n)
    """
    for k in range(i, len(tablero)):  # O(n)
        if not tablero[k][j]:
            break

        if not validar_adyacencia_abajo(tablero, k, j):
            return False

        tablero[k][j] = 0
        tamanio_barco[0] += 1

    return True

def validar_posicion_barco(tablero, barcos, i, j):
    """
    Complejidad: O(max(m, n) + k), porque se puede llamar a buscar_barco_a_la_derecha o 
    buscar_barco_para_abajo, pero no a ambos.
    """
    tamanio_barco = [1]
    tablero[i][j] = 0
    if j+1 < len(tablero[0]) and tablero[i][j+1]:
        if not buscar_barco_a_la_derecha(tablero, i, j, tamanio_barco):  # O(m)
            return False

    if i+1 < len(tablero) and tablero[i+1][j]:
        if not buscar_barco_para_abajo(tablero, i, j, tamanio_barco): # O(n)
            return False

    if tamanio_barco == 1:
        if not validar_diagonal(tablero, i, j):  # O(1)
            return False
    
    if tamanio_barco[0] in barcos:
        barcos.remove(tamanio_barco[0])  # O(k)
        return True
    
    
    return False

def validar_restricciones(tablero, barcos, restriccion_filas, restriccion_columnas):
    """
    Complejidad: O(m x n) + O(m x n) + O(m x n) = O(m x n)
    """
    
    # Verificar restricciones de filas
    for i in range(len(tablero)): # O(n)
        if sum(tablero[i]) != restriccion_filas[i]:    # O(m)
            print('Fila ' + str(i) + ' no cumple con la restricción')
            return False  

    # Verificar restricciones de columnas
    for j in range(len(tablero[0])):  # O(m)
        columna_ocupada = sum(tablero[i][j] for i in range(len(tablero)))  # O(n)
        if columna_ocupada != restriccion_columnas[j]:
            print('Columna ' + str(j) + ' no cumple con la restricción') 
            return False 

    #verificar que hay cantidad correcta de casilleros ocupados
    celdas_ocupadas = sum(sum(fila) for fila in tablero) # O(m x n)
    if celdas_ocupadas != sum(barcos):
        print('Cantidad de casilleros ocupados incorrecta')
        return False

    return True

def verificador_batalla_naval(tablero, restriccion_filas, restriccion_columnas, barcos):
    if (len(tablero) == 0) or len(tablero[0] == 0) or (len(barcos) == 0):
        return False
    
    # Si no hay lugar para insertar todos los barcos que hay
    if (len(tablero)*len(tablero[0])) < sum(barcos):
        return False
    
    # Validar que las rescricciones sean posiblesl
    if not validar_restricciones(restriccion_filas, restriccion_columnas, barcos):
        return False


    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 1: # La casilla esta ocupada

                # Analiza que no haya barcos adyacentes
                if not validar_posicion_barco(tablero, barcos, i, j): #(O(m*n) + k)
                    return False

    if len(barcos) > 0:
        return False

    return True