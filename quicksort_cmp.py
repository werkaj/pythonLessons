import listy_do_sortowania

#zadanie 11.3
def quicksort(L, left, right, cmpfunc):
    if left >= right:
        return
    swap(L, left, (left + right) // 2) 
    pivot = left                
    for i in range(left + 1, right + 1):   
        if cmpfunc(L[i],L[left]) < 0:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)     
    quicksort(L, left, pivot - 1, cmpfunc)
    quicksort(L, pivot + 1, right, cmpfunc)

def swap(L, left, right):
    L[left], L[right] = L[right], L[left]

def compare(first, second):
    if first < second:
        return -1
    elif first > second:
        return 1
    else:
        return 0

lista_random = listy_do_sortowania.random_list(20, 30)
lista_diff_random = listy_do_sortowania.random_diff_list(20,30)
lista_diff_almost_sorted_list = listy_do_sortowania.random_diff_almost_sorted(20,30)
lista_diff_almost_sorted_list_wrong = listy_do_sortowania.random_diff_almost_sorted_wrong(20,30)
lista_gauss = listy_do_sortowania.random_gauss_distribution(20)

quicksort(lista_random, 0, len(lista_random)-1, compare)
quicksort(lista_diff_random, 0, len(lista_diff_random)-1, compare)
quicksort(lista_diff_almost_sorted_list, 0, len(lista_diff_almost_sorted_list)-1, compare)
quicksort(lista_diff_almost_sorted_list_wrong, 0, len(lista_diff_almost_sorted_list_wrong)-1, compare)
quicksort(lista_gauss, 0, len(lista_gauss)-1, compare)

print(lista_random)
print(lista_diff_random)
print(lista_diff_almost_sorted_list)
print(lista_diff_almost_sorted_list_wrong)
print(lista_gauss)

lista_random2 = listy_do_sortowania.random_list(40, 50)
quicksort(lista_random2, 0, len(lista_random2)-1, compare)
