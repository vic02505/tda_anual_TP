# TDA (curso anual, Buchwald, Genender) - Trabajo Práctico Integrador

Repositorio del trabajo práctico integrador de la materia teoría de algoritmos, Facultad de Ingeniería, Universidad de
Buenos Aires.

| Integrante                | Padrón   | Mail                 |
|---------------------------|----------|----------------------|
| Juan Francisco Cuevas     | 107963   | jcuevas@fi.uba.ar    |
| Mateo Lardiez             | 107992   | mlardiez@fi.uba.ar   |
| Tomás Vainstein Aranguren | 109043   | tvainstein@fi.uba.ar |
| Julián Gorge              | 104286   | jgorge@fi.uba.ar     |
| Víctor Zacarías           | 107080   | vzacarias@fi.uba.ar  |


# Descripción del trabajo

El trabajo consta de tres partes, cada una evaluando temas centrales de la materia. 

1. Algoritmos greedy.
2. Programación dinámica.
3. Reducciones, Backtracking y aproximciones.

# Ejecución del proyecto

Desde la carpeta raíz del proyecto, ejecutar el siguiente comando:

```bash
python3 main.py <flag_obligatorio> <flag_opcional>
```
- <flag_obligatorio>:
   - **"-a"** para ejecutar todos los algoritmos con los datasets locales.
   - **"-g"** para ejecutar el algoritmo greedy con los datasets locales.
   - **"-d"** para ejecutar el algoritmo de programación dinámica con los datasets locales.
   - **"-b"** para ejecutar el algoritmo de backtracking con los datasets locales.

- <flag_opcional>:

    - **"-e"**: Colocar únicamente después de **"-g"**, **"-d"** o **"-b"** para los casos de uso externos.
  
**IMPORTANTE:** Para ejecutar los algoritmos con los datasets externos, es necesarios incluir dichos datasets
en las carpetas correspondientes.

1. Algoritmos greedy: **part_I/extern_datasets** (path desde la carpeta raíz del proyecto).
2. Programación dinámica: **part_II/extern_datasets** (path desde la carpeta raíz del proyecto).
3. Backtracking: **part_III/extern_datasets** (path desde la carpeta raíz del proyecto).

# Salidas del proyecto

Todas las salidas del proyecto son generadas en el directorio **algorithms_output** del directorio raíz. Por 
defecto el directorio viene con contenido de los datasets locales. Volver a ejecutar el proyecto únicamente
sobreescribirá los archivos existentes, y en caso de correr con los datasets externos, generará los archivos
correspondientes.
Los dataset locales se guardaran como "local_{tipo de algoritmo}_{nombre_de_archivo}". Por ejemplo si se ejecuta
el archiv "20.txt", se va a guardar como "local_greedy_20.txt"
Los dataset externos se guardaran como "extern_{tipo de algoritmo}_{nombre_de_archivo}". Por ejemplo si se ejecuta
el archiv "test1.txt", se va a guardar como "extern_greedy_test1.txt"
