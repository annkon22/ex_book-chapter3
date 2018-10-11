# Implement a stack using a linked list

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

class UnorderedList:
    def __init__(self):
        self.head = None
        self.num = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.num += 1


    def size(self):
        return self.num

    def list_print(self):
        print_value = self.head
        while print_value:
            print(print_value.data, end = ' ')
            print_value = print_value.next   

    def queue(self, newdata):
        new_node = Node(newdata)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def stack(self, newdata):
        new_node = Node(newdata)
        if self.head is None:
            self.head = new_node
            return
      


  

    def __str__(self):
        current = self.head
        string = ''
        while current is not None:
            string += str(current) + ", "
            current = current.get_next()
        return string        

my_lst = UnorderedList()
my_lst.stack(1)
my_lst.stack(10)
my_lst.stack(100)
my_lst.stack(1000)
my_lst.stack(10000)
my_lst.stack(100000)
my_lst.stack(1000000)
my_lst.stack(10000000)

my_lst.list_print()
print()

  
