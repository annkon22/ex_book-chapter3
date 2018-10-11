#create an implementation of a queue
#that would have an average performance of O(1)
#for enqueue and dequeue operations

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        rev = False
        while self.items is not None and not rev:
            rev = True
        return self.items.pop(0)


my_q = Queue()

my_q.enqueue(1)
my_q.enqueue(2)
my_q.enqueue(3)
my_q.enqueue(4)
my_q.enqueue(5)
my_q.enqueue(6)

print(my_q.dequeue())
print(my_q.dequeue())
print(my_q.dequeue())
print(my_q.dequeue())
print(my_q.dequeue())




    