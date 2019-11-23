import copy

#9.2
class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def search(self, data): 
        self2 = copy.copy(self)
        while self2.head != None:
            if self2.head.data == data:
                return self2
            else:
                 self2.head = self2.head.next

    def find_min(self):
        self2 = copy.copy(self)
        wynik = self2.head
        while self2.head != None:
            if self2.head.data < wynik.data:
                wynik = self2.head
            self2.head = self2.head.next
        return wynik

    def find_max(self): 
        self2 = copy.copy(self)
        wynik = self2.head
        while self2.head != None:
            if self2.head.data > wynik.data:
                wynik = self2.head
            self2.head = self2.head.next
        return wynik  

    def reverse(self):
        self2 = SingleList()
        self3 = copy.copy(self)
        while(self3.head!=None):
            self2.insert_head(Node(self3.head.data))
            self3.head = self3.head.next
        return self2
    
    def print_list(self):
        self2 = copy.copy(self)
        while(self2.head!=None):
            print(self2.head.data)
            self2.head = self2.head.next

alist = SingleList()
alist.insert_head(Node(2))
alist.insert_head(Node(3))
alist.insert_tail(Node(4))
alist.insert_tail(Node(5))
alist.insert_tail(Node(6))


print(SingleList.search(alist,4).head.data)
print(SingleList.find_min(alist).data)
print("normalna")
SingleList.print_list(alist)
print("odwrocona")
print("dlugosc list ", SingleList.count(alist.reverse()))
SingleList.print_list(alist.reverse())

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if self.data < node.data:   
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        elif self.data > node.data:    
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            pass    

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None


class BinarySearchTree:
    """Klasa reprezentująca binarne drzewo poszukiwań."""

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root:
            self.root.insert(node)
        else:
            self.root = node

    def count(self):
        if self.root:
            return self.root.count()
        else:
            return 0

    def search(self, data):   # zwraca node lub None
        if self.root:
            return self.root.search(data)
        else:
            return None

#9.7

def bst_max(top, i = 0):
    if top == None:
        if i == 0:
            raise ValueError
        else:
            return -1
    wynik = top.data
    lwynik = bst_max(top.left,1)
    rwynik = bst_max(top.right,1)
    if lwynik > wynik:
        wynik = lwynik
    if rwynik > wynik:
        wynik = rwynik
    return wynik

def bst_min(top,i = 0):
    if top == None:
        if i == 0:
            raise ValueError
        else:
            return -1
    wynik = top.data
    lwynik = bst_max(top.left,1)
    rwynik = bst_max(top.right,1)
    if lwynik < wynik:
        wynik = lwynik
    if rwynik < wynik:
        wynik = rwynik
    return wynik

#sprawdzenie dzialania bst_max i bst_min na konkretnej implementacji drzewka
drzewko = BinarySearchTree()
drzewko2 = BinarySearchTree()
drzewko.insert(Node(2))
drzewko.insert(Node(3))
drzewko.insert(Node(11))
drzewko.insert(Node(1))

print("maksymalna: ", bst_max(drzewko.root))
print("minimalna: ", bst_min(drzewko.root))
#print("puste (raise ValueError)", bst_max(drzewko2.root))