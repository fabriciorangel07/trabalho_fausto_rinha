passadas = 0
comps = 0
trocas = 0

def quick_sort(lista, ini = 0, fim = None):
    
    if fim is None:
        fim = len(lista) - 1


    if fim <= ini:
        return

    global passadas, comps, trocas

    passadas += 1

    pivot = fim
    div = ini - 1

    for i in range(ini, fim):
        comps += 1
        if lista[i] < lista[pivot]:
            div += 1 

            if div != i:
                lista[div], lista[i] = lista[i], lista[div]
                trocas += 1

    div += 1

    comps += 1
    if lista[pivot] < lista[div] and pivot != div:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1

    quick_sort(lista, ini, div - 1)

    quick_sort(lista, div + 1, fim)

#####################################################################

"""

from data.emp10mil import empresas
from time import time
import tracemalloc

passadas = 0
comps = 0
trocas = 0

ini = time()
tracemalloc.start()

quick_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(empresas)    # Para não ficar aparecendo as empresas no terminal

print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

##############################################################################

"""

from data.emp25mil import empresas
from time import time
import tracemalloc

passadas = 0
comps = 0
trocas = 0

ini = time()
tracemalloc.start()

quick_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(empresas)    # Para não ficar aparecendo as empresas no terminal

print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

########################################################################################

"""

from data.emp50mil import empresas
from time import time
import tracemalloc

passadas = 0
comps = 0
trocas = 0

ini = time()
tracemalloc.start()

quick_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(empresas)    # Para não ficar aparecendo as empresas no terminal

print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

##################################################################################

from data.emp100mil import empresas
from time import time
import tracemalloc

passadas = 0
comps = 0
trocas = 0

ini = time()
tracemalloc.start()

quick_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(empresas)    # Para não ficar aparecendo as empresas no terminal
print("100 mil empresas:")
print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()