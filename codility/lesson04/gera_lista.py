import random
def gera_lista_aleatoria(tamanho, min, max):
    lista = []
    for i in range(0, tamanho):
        lista.append(random.randint(min,max))
    return lista

def gera_lista_sequencial(tamanho):
    return list(range(1, tamanho+1))

gera_lista_aleatoria(30000, 1,5)