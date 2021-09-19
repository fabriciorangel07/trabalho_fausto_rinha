comps = 0
passadas = 0
trocas = 0

def bubble_sort(lista):

    global comps, passadas, trocas
    comps = 0       # Número de comparações
    passadas = 0    # Número de passadas
    trocas = 0      # Número de trocas

    while True:     # Loop eterno
        passadas += 1
        trocou = False
        # Loop na lista até o PENÚLTIMO elemento: len(lista) - 2 -> range(len(lista) - 1)
        # Ex. em uma lista de 10 elementos, len(lista) == 10
        # A última posição estará em len(lista) - 1, ou seja, 9 -> range(len(lista))
        # A penúltima posição estará em len(lista) - 2, ou seja, 8 -> range(len(lista) - 1)
        for i in range(len(lista) - 1):     # Inicia nova passada
            comps += 1
            if lista[i + 1] < lista[i]:     # É necessário trocar
                lista[i + 1], lista[i] = lista[i], lista[i + 1]  # Faz a troca
                trocas += 1
                trocou = True

        # Se houve troca, a lista está ordenada e podemos interromper
        # o loop while
        if not trocou:  # trocou == False
            break   # Interrompe o while

###################################################################################3

"""
from data.emp10mil import empresas
from time import time
import tracemalloc

ini = time()

tracemalloc.start()

bubble_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(empresas)    # Para não ficar aparecendo as empresas no terminal
print("10mil empresas:")
print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB") 

tracemalloc.stop()

"""
#################################################################################

"""
from data.emp25mil import empresas
from time import time
import tracemalloc

ini = time()

tracemalloc.start()

bubble_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

# print(empresas)        # Para não ficar aparecendo as empresas no terminal
print("25mil empresas:")
print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

"""

############################################################################


from data.emp50mil import empresas
from time import time
import tracemalloc

ini = time()

tracemalloc.start()

bubble_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

# print(empresas)    # Para não ficar aparecendo as empresas no terminal
print("50mil empresas:")
print(f"Tempo: {fim - ini}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()

###############################################################################
