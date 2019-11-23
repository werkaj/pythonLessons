#10.8
from random import randint

class RandomQueue:

    def __init__(self,size=10):
        self.n = size + 1         
        self.items = self.n * [None] 
        self.head = 0           
        self.tail = 0           

    def insert(self, item):
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.n

    def remove(self):
        if RandomQueue.is_empty(self):
            raise ValueError
        spot = randint(self.head, self.tail)
        data = self.items[spot]
        for i in range(spot,self.tail+1):
            self.items[i] = self.items[i+1]
        self.tail-=1
        return data 

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def clear(self):
        self.items = self.n * [None] 
        self.tail = self.head    
    
    def print_random_queue(self):
        if RandomQueue.is_empty(self):
            print("queue is empty")
        for i in range(self.tail - self.head):
            print("items[{}] = {} ".format(i, self.items[i]))

randomQueue = RandomQueue()
randomQueue.insert(2)
randomQueue.insert(3)
randomQueue.insert(1)
randomQueue.insert(7)
randomQueue.insert(5)
randomQueue.insert(11)
randomQueue.print_random_queue()
print("remove " + str(randomQueue.remove()))
randomQueue.print_random_queue()
print("remove " + str(randomQueue.remove()))
randomQueue.print_random_queue()
print("remove " + str(randomQueue.remove()))
randomQueue.print_random_queue()
randomQueue.clear()
randomQueue.print_random_queue()