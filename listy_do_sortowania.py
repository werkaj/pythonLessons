import random

# (a) różne liczby int od 0 do N-1 w kolejności losowej,
def random_diff_list(lenght, max_int):
    return random.sample(range(max_int), lenght)

# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
def random_diff_almost_sorted(lenght, max_int):
    lista = random.sample(range(max_int), lenght)
    for i in range(lenght//2):
        swap_if_more(lista, i, i + random.randint(1,lenght//2))
    return lista

# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
def random_diff_almost_sorted_wrong(lenght, max_int):
    lista = random.sample(range(max_int), lenght)
    for i in range(lenght//2):
        swap_if_less(lista,i, i + random.randint(1,lenght//2))
    return lista


# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
import numpy as np

def random_gauss_distribution(lenght):
    return np.random.randn(lenght)

# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).
def random_list(lenght, max_int):
    list = []
    for i in range(lenght):
        list.append(random.randint(0,max_int))
    return list

def swap_if_more(lista,first, second):
    if lista[first] >= lista[second]:
        pass
    else:
         lista[first], lista[second] = lista[second],lista[first]

def swap_if_less(lista,first, second):
    if lista[first] >= lista[second]:
        pass
    else:
         lista[first], lista[second] = lista[second],lista[first]
