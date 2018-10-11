#Modify the Unordered list to rewrite the length list. 
#The strategy would be to store the number of nodes in the list 
# as an additional piece of data in the headof the list

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

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
            self.num -= 1
        else:
            previous.set_next(current.get_next())
            self.num -= 1


my_lst = UnorderedList()
my_lst.add(1)
my_lst.add(10)
my_lst.add(100)
my_lst.add(1000)
my_lst.add(10000)
my_lst.add(100000)
my_lst.add(1000000)
my_lst.add(10000000)

my_lst.list_print()
print()
print('number of items:', my_lst.size())

my_lst.remove(1)
my_lst.list_print()
print()
print('number of items:', my_lst.size())

