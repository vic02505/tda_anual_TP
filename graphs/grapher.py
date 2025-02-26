from part_I.greedy_coins_game import coins_game
from util import time_algorithm
from part_II.dynamic_coins_game import start_game

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
x = np.linspace(100,4_000, 20).astype(int)


# Mide el tiempo de ejecucion de un algoritmo para cada tamaño de la lista "x" . La función lambda se usa para
# generar una lista de números aleatorios de tamaño "s" para cada valor de "x" Lo que hace la función es
# evaluar el algoritmo con listas de distintos tamaños y devolver los tiempos de ejecución de cada lista.
results = time_algorithm(start_game, x, lambda s: [get_random_array(s)])

ax: plt.Axes
fig, ax = plt.subplots()
ax.plot(x, [results[i] for i in x], label="Medición")
ax.set_title('Tiempo de ejecución de monedas programacion dinamica')
ax.set_xlabel('Tamaño del array')
ax.set_ylabel('Tiempo de ejecución (s)')
None

# Ajuste de curva por mínimos cuadrados
# La función que ajustamos es c1 * x + c2
# donde c1 y c2 son los coeficientes que queremos encontrar

f = lambda x, c1, c2: c1 * x**2 + c2

c, pcov = sp.optimize.curve_fit(f, x, [results[n] for n in x])

print(f"c_1 = {c[0]}, c_2 = {c[1]}")
r = np.sum((c[0] * x * x + c[1] - [results[n] for n in x])**2)
print(f"Error cuadrático total: {r}")

ax.plot(x, [c[0] * n **2 + c[1] for n in x], 'r--', label="Ajuste")
ax.legend()
fig
plt.savefig("part_II/mediciones.png")


# Graficamos el error de ajuste

ax: plt.Axes
fig, ax = plt.subplots()
errors = [np.abs(c[0] * n ** 2 + c[1] - results[n]) for n in x]
ax.plot(x, errors)
ax.set_title('Error de ajuste')
ax.set_xlabel('Tamaño del array')
ax.set_ylabel('Error absoluto (s)')
plt.savefig("part_II/error_ajuste.png")
None