#3.3
for i in range(31):
    if(i%3!=0):
        print(i)

#3.4
while True:
    try:
        n = input("Podaj float: ")
        if(n=="stop"):
            break
        n = float(n)
    except ValueError:
        print("Podaj float!") 
        continue
    print(n, n**3)

#3.5
for i in range(12):
    print("|....", end = "")
print("|")
for i in range(13):
    if i==0:
        print(i, end = "")
    elif i < 10:
        print("   ",i, end = "")
    else:
        print("  ",i, end = "")
print("\n")

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
print(string)

#3.6
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

prostokat = ""
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
print(prostokat)

#3.8
seq1 = "mielonka"
seq2 = "biedronka"
alist = []
for item in seq1:
    if item in seq2:   
        alist.append(item)
print(alist)      

seq1 = "mielonka"
seq2 = "biedronka"
alist = []
for item in seq1:
    if item not in alist:   
        alist.append(item)
for item in seq2:
    if item not in alist:   
        alist.append(item)
print(alist)  

#3.9
listaSekwencji = [[1,2],(2,2,1,1),(),[1],[],[2,2,1,2,4,4]]
listaDlugosci = [len(item) for item in listaSekwencji]
print(listaDlugosci)

#3.10
slownik = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
print(slownik['V'])

keys = ['I', 'V', 'X','L', 'C', 'D', 'M']
values = [1,5,10,50,100,500,1000]
slownik2 = dict(zip(keys, values))
print(slownik['L'])

