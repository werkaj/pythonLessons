#4.2
def printMiarka():
    string = ''
    for i in range(12):
        string += "|...."
    string += "|\n"
    for i in range(13):
        if i==0:
            string += str(i)
        elif i < 10:
            string += "    " + str(i)
        else:
            string += "   " + str(i)
    return string

print(printMiarka())

def printProstokat():
    while True:
        try:
            x = int(input("Podaj wymiar x: "))
            y = int(input("Podaj wymiar y: "))
        except ValueError:
            print("Wymiary w intach!") 
            continue
        if x == 0 or y == 0:
            print("Wymiar musi byc wiekszy od 0")
            continue 
        break

    prostokat = ''
    for j in range(y):
        for i in range(x):
            prostokat += "+---"
        prostokat += "+\n"
        for i in range(x):
            prostokat += "|   "
        prostokat += "|\n"
    for i in range(x):
        prostokat += "+---"
    prostokat += "+"
    return prostokat

print(printProstokat())

#4.3
def factorial(n):
    wynik = 1
    for i in range(n):
        wynik*=(i+1)
    return wynik

print(factorial(4))

#4.4
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
for i in range(10):
    print(fibonacci(i), end= ",")
print("\n")

#4.5
def odwracanie(L, left, right):
    for i in range(right - left - 1):
        temp = L[left]
        L[left]=L[right]
        L[right] = temp
        left+=1
        right-=1
    return L

L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(odwracanie(L,2,6))

#4.6
def sum_seq(sequence, wynik = 0):
    for item in sequence:
        if isinstance(item, (list, tuple)):
            wynik = sum_seq(item,wynik)
        else:
            wynik += item
    return wynik

sequence = [(2,1,1),3,[1,4,1]]
print(sum_seq(sequence))

#4.7
def flatten(sequence,flat_list=[]):
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flatten(item,flat_list)
        else:
           flat_list.append(item)
    return flat_list

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print(flatten(seq))

