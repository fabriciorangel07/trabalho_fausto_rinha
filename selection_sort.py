comps = 0
passadas = 0
trocas = 0

def selection_sort(lista):

    global comps, passadas, trocas
    comps = 0
    passadas = 0
    trocas = 0

    for pos_sel in range(len(lista) - 1):
        passadas += 1

        pos_menor = pos_sel + 1

        for j in range(pos_sel + 2, len(lista)):
            comps += 1

            if lista[j] < lista[pos_menor]:
                pos_menor = j

        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

#####################################################################

"""

from data.emp10mil import empresas
from time import time
import tracemalloc

ini = time()
tracemalloc.start()

selection_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

# print(empresas)   # Para não ficar aparecendo as empresas no terminal
print(f"Tempo: {fim - ini}")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

############################################################################

"""

from data.emp25mil import empresas
from time import time
import tracemalloc

ini = time()
tracemalloc.start()

selection_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

# print(empresas)   # Para não ficar aparecendo as empresas no terminal
print(f"Tempo: {fim - ini}")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

##################################################################################

"""

from data.emp50mil import empresas
from time import time
import tracemalloc

ini = time()
tracemalloc.start()

selection_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

# print(empresas)   # Para não ficar aparecendo as empresas no terminal
print("50 mil empresas:")
print(f"Tempo: {fim - ini}")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

###############################################################################

from data.emp100mil import empresas
from time import time
import tracemalloc

ini = time()
tracemalloc.start()

selection_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

# print(empresas)   # Para não ficar aparecendo as empresas no terminal
print("100 mil empresas:")
print(f"Tempo: {fim - ini}")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()