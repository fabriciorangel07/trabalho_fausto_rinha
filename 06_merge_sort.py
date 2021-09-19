comps = 0
divisoes = 0
juncoes = 0

def merge_sort(lista):

    global comps, divisoes, juncoes

    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    lista_esq = lista[:meio]
    lista_dir = lista[meio:]
    
    divisoes += 1

    lista_esq = merge_sort(lista_esq)
    lista_dir = merge_sort(lista_dir)


    pos_esq = 0
    pos_dir = 0
    ordenada = []

    while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):

        if lista_esq[pos_esq] < lista_dir[pos_dir]:
            ordenada.append(lista_esq[pos_esq])
            pos_esq += 1
        else:
            ordenada.append(lista_dir[pos_dir])
            pos_dir += 1
        comps += 1

    sobra = None

    if pos_esq < pos_dir:
        sobra = lista_esq[pos_esq:] 
    else:
        sobra = lista_dir[pos_dir:] 

    juncoes += 1
    return ordenada + sobra

#################################################################

"""

from data.emp10mil import empresas
from time import time
import tracemalloc

comps = 0
divisoes = 0
juncoes = 0

ini = time()
tracemalloc.start()

merge_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(empresas)    # Para não ficar aparecendo as empresas no terminal

print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

#######################################################################################7

"""

from data.emp25mil import empresas
from time import time
import tracemalloc

comps = 0
divisoes = 0
juncoes = 0

ini = time()
tracemalloc.start()

merge_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(empresas)    # Para não ficar aparecendo as empresas no terminal

print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

################################################################################

"""

from data.emp50mil import empresas
from time import time
import tracemalloc

comps = 0
divisoes = 0
juncoes = 0

ini = time()
tracemalloc.start()

merge_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(empresas)    # Para não ficar aparecendo as empresas no terminal

print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

########################################################################################

from data.emp100mil import empresas
from time import time
import tracemalloc

comps = 0
divisoes = 0
juncoes = 0

ini = time()
tracemalloc.start()

merge_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(empresas)    # Para não ficar aparecendo as empresas no terminal
print("100 mil empresas:")

print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()