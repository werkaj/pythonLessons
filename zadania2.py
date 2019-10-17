#2.10
slowo = """nananan nanan n
    nqnqnqn
ssksks"""
lista = slowo.split()
print("liczba wyrazow: ", len(lista))

#2.11
word = 'nananna annnana na nanana nan nanan'
wyraz = '_'.join(word)
print(wyraz)

#2.12
line = 'lsls la d ahdd hhdh'
lineLista = line.split()
pierwszeLitery = ''
ostatnieLitery = ''

for wyraz in lineLista:
    pierwszeLitery += wyraz[0]
    ostatnieLitery += wyraz[-1]
    
print("pierwszeLitery ", pierwszeLitery, "\nostatnieLitery ", ostatnieLitery)

#2.13
lacznaDlugosc = 0
for wyraz in lineLista:
    lacznaDlugosc+=len(wyraz)
print("laczna dlugosc napisow: ", lacznaDlugosc)

#2.14
slowo2 = 'nananan nanan nn nana n'.split()
print(max(slowo2, key = len))
print(len(max(slowo2, key = len)))    

#2.15
liczby = [1,2,3,4]
napis = ''
i = 0
while i < len(liczby):
    napis = napis + str(liczby[i])
    i+=1
    
print(napis)

#2.16
line = "bababab GvR naananna"
line = line.replace("GvR", "Guido van Rossum")
print(line)

#2.17
line = "kot pies mysz kon kucyk chomik szynszyla"
sortAlfabetyczny = sorted(line.split())
sortDlugosci = sorted(line.split(), key = len)
print("Posortowane alfabetycznie: ", sortAlfabetyczny, "\nPosortowane wg dlugosci: ", sortDlugosci)
        
#2.18
liczba = 9202000000000000000000000011010
print(str(liczba).count('0'))

#2.19
listaLiczb = [1,2,12,3,34,111,222,3,88]
lista_dop = [str(x).zfill(3) for x in listaLiczb]
for num in lista_dop:
    print(num, end=", ")