#10.4
class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if Queue.is_full(self):
            raise ValueError
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if Queue.is_empty(self):
            raise ValueError
        data = self.items[self.head]
        self.items[self.head] = None     
        self.head = (self.head + 1) % self.n
        return data

queue = Queue(1)
queue.put(4)

import unittest
    
class TestQueue(unittest.TestCase):
    def test_is_empty(self):
        self.assertTrue(Queue.is_empty(Queue()))
    
    def test_is_full(self):
        self.assertTrue(Queue.is_full(queue))
    
    def test_get(self):
        self.assertRaises(ValueError, Queue.get, Queue())
    
    def test_put(self):
        self.assertRaises(ValueError, Queue.put, queue, 5)

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy