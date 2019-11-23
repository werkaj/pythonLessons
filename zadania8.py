import math
import random

#8.1
def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    return (-by-c)/a

#8.3
def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    t = 0
    p = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y** 2 < 1:
            t+=1
        else:
            p+= 1
    return t/p

print(calc_pi(10000))

#8.4
def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a > b + c or b > a + c or c > a + b:
        raise ValueError
    else:
        p = (a + b + c)/2
        return math.sqrt(p * (p-a) * (p-b) * (p-c))

print(heron(5,4,3))

#8.6
#wersja rekurencyjna
def rek_P(i, j):
    if i == 0:
        if j == 0:
            return 0.5
        return 1
    elif j == 0:
        return 0
    else:
         return 0.5*rek_P(i-1,j) + rek_P(i, j -1)

print(rek_P(5,6)) 

#wersja_dynamiczna
def dyn_P(i,j):
    P = {(0,0): 0.5}
    for n in range(1,i+1):
        P[(n,0)] = 0
    for m in range(1,j+1):
        P[(0,m)] = 1
    for n in range(1,i+1):
        for m in range(1,j+1):
            P[(n,m)] = 0.5*P[(n-1,m)] + P[(n,m-1)] 
    return P[(i,j)]

print(dyn_P(5,6))
