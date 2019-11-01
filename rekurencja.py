def factorial(n):
    wynik = 1
    for i in range(n):
        wynik*=(i+1)
    return wynik

# print(factorial(4))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp1 = 1
        temp2 = 1
        for i in range(n-2):
            temp3 = temp2
            temp2 = temp2 + temp1
            temp1 = temp3
        return temp2

# for i in range(10):
#     print(fibonacci(i), end= ",")
# print("\n")