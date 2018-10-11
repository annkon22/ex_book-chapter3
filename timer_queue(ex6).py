#Design and implement an experiment to do benchmark comparisons
#of the two queue implementations. What can you learn
#from such an experiment?
import time
import queue

class Queue():
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop() 

my_q = Queue()
start_my = time.time()
for i in range(10000):
    my_q.enqueue(i)
for _ in range(10000):
    trash = my_q.dequeue()
end_my = time.time()


std_q = queue.Queue()
start_std = time.time()
for i in range(10000):
    std_q.put(i)
for i in range(10000):
    trash = std_q.get()
end_std = time.time()

print('My queue', end_my - start_my)
print('Standard queue', end_std - start_std)



