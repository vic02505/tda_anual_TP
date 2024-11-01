# Imports necesarios para el notebook
from random import seed
from matplotlib import pyplot as plt

from part_I.main_part_I import coins_game
from util import time_algorithm

from part_I.libs.datasets_parser import get_coins_list

import seaborn as sns
import numpy as np
import scipy as sp

seed(12345)
np.random.seed(12345)
sns.set_theme()

# La variable x van a ser los valores del eje x de los gráficos en todo el notebook
# Tamaño mínimo=100, tamaño máximo=10kk, cantidad de puntos=20
x = np.linspace(100, 10_000_000, 20000).astype(int)


results = time_algorithm(coins_game, x, lambda s: [get_coins_list("20000.txt")])


ax: plt.Axes
fig, ax = plt.subplots()
ax.plot(x, [results[i] for i in x], label="Medición")
ax.set_title('Tiempo de ejecución de sorted')
ax.set_xlabel('Tamaño del array')
ax.set_ylabel('Tiempo de ejecución (s)')
plt.show()