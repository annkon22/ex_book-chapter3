class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class Deque:
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_front(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
            

    def add_rear(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
        
    def list_print(self):
        print_value = self.head
        while print_value:
            print(print_value.data, end = ' ')
            print_value = print_value.next   

    
    def remove_front(self):
        current = self.head
        previous = None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        previous.set_next(None)        
          
    def remove_rear(self):            
        first_node = self.head
        if self.head is None:
            return
        else:
            self.head = first_node.next
            


    def __str__(self):
        current = self.head
        string = ''
        string += '[ '
        
        while current is not None:
            string += str(current.data) + ", "
            current = current.get_next()
        string += " ]"
        return string


my_deq = Deque()
my_deq.add_rear(5)
my_deq.add_rear(6)
my_deq.list_print()
print()
my_deq.add_front(8)
my_deq.add_front(9)
my_deq.list_print()
print()
my_deq.remove_front()
my_deq.list_print()
print()
my_deq.remove_rear()

my_deq.list_print()





