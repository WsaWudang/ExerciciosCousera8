#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, 
#verifica se tal lista possui elementos repetidos e os remove. 
#A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. 
#A lista devolvida deve estar ordenada.

def remove_repetidos(lista):
    lista_sem_repetidos = list(set(lista))
    lista_sem_repetidos.sort()
    return lista_sem_repetidos