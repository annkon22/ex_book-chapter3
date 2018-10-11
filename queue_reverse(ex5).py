#Implement the Queue ADT, using a list such that the rear of the queue
#is at he end of the list



class Queue():
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) 


my_q = Queue()
my_q.enqueue('hi')
my_q.enqueue('ok')
my_q.enqueue('bye')

print(my_q.dequeue())
print(my_q.dequeue())
print(my_q.dequeue())
