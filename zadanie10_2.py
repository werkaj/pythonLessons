#10.2
class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if Stack.is_full(self):
            raise ValueError
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if Stack.is_empty(self):
            raise ValueError
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

import unittest

stos = Stack(1)
stos.push(2)

class TestStack(unittest.TestCase):
    def test_is_empty(self):
        self.assertTrue(Stack.is_empty(Stack()))
    
    def test_is_full(self):
        self.assertTrue(Stack.is_full(stos))
    
    def test_pop(self):
        self.assertRaises(ValueError, Stack.pop, Stack())
    
    def test_push(self):
        self.assertRaises(ValueError, Stack.push, stos, 3)

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy