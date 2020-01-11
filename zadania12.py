import quicksort_cmp

#zadania 12.1
import random

def find_all(n,k):
    lista = []
    for i in range(n):
        lista.append(random.randint(0,k))
    y = random.randint(0,k)
    lista_y = []
    for i in range(n):
        if lista[i]==y:
            lista_y.append(i)
    return lista_y

print(find_all(100,10))

print(quicksort_cmp.lista_random2)

#zadania 12.2
def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if left > right:
        return
    k = (left + right)//2
    if L[k]==y:
        return k
    elif y >L[k]:
        left = k + 1
    else:
        right = k - 1
    return binarne_rek(L, left, right , y)

def binary_search(L, left, right, y):
    """Wyszukiwanie binarne w wersji iteracyjnej."""
    while left <= right:
        k = (left+right)//2
        if y == L[k]:
            return k
        if y > L[k]:
            left = k+1
        else:
            right = k-1
    return None

print(binarne_rek(quicksort_cmp.lista_random2,0,len(quicksort_cmp.lista_random2),
     quicksort_cmp.lista_random2[8]))

