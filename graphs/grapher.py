from part_I.greedy_coins_game import coins_game
from util import time_algorithm
from part_I.libs.datasets_parser import get_coins_list

from random import seed
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

seed(12345)
np.random.seed(12345)
sns.set_theme()

# Genera una lista numeros aleatorios entre a y b (se puede saber el rango de valores viendo el return).
def get_random_array(size: int):
    return np.random.randint(1, 10000, size, dtype=np.int32)

# Genera una lista de valores enteros equiespaciados que van desde "start" hasta "stop". "num" indica
# la cantidad de valores que se generan.
x = np.linspace(20,20_000, 20).astype(int)


# Mide el tiempo de ejecucion de un algoritmo para cada tamaño de la lista "x" . La función lambda se usa para
# generar una lista de números aleatorios de tamaño "s" para cada valor de "x" Lo que hace la función es
# evaluar el algoritmo con listas de distintos tamaños y devolver los tiempos de ejecución de cada lista.
results = time_algorithm(coins_game, x, lambda s: [get_random_array(s)])

ax: plt.Axes
fig, ax = plt.subplots()
ax.plot(x, [results[i] for i in x], label="Medición")
ax.set_title('Tiempo de ejecución de sorted')
ax.set_xlabel('Tamaño del array')
ax.set_ylabel('Tiempo de ejecución (s)')
plt.show()