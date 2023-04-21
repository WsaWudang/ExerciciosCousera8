#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, 
#verifica se tal lista possui elementos repetidos e os remove. 
#A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. 
#A lista devolvida deve estar ordenada.

def remove_repetidos(lista):
    conjunto_sem_repeticao = set(lista)
    lista_sem_repeticao = sorted(list(conjunto_sem_repeticao))
    print(lista_sem_repeticao)

remove_repetidos(lista)