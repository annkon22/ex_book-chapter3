#Implement the remaining operations defined in the OrderedList ADT.

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


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None    

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

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
        else:
            previous.set_next(current.get_next())


    def list_print(self):
        print_value = self.head
        while print_value:
            print(print_value.data, end = ' ')
            print_value = print_value.next 

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found
    

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)

        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def pop(self):
        last_node = self.head
        previous = None
        while last_node.next != None:
            previous = last_node
            last_node = last_node.get_next()
        
        previous.set_next(None)

        return last_node.data


    def pop1(self, pos):
        current = self.head
        previous = None
        cur_pos = 0
        found = False
        while not found:
            if cur_pos == pos:
                found = True
            else:
                previous = current
                current = current.get_next()
                cur_pos += 1
        
        if previous == None:
            current = current.get_next()
        else:
            previous.set_next(current.get_next())   
        return current.get_data() 

    def index(self, item):
        current = self.head
        cur_pos = 0
        found = False
        while current.get_next() is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                cur_pos += 1
        return cur_pos




        
my_lst = OrderedList()
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
print(my_lst.pop1(5))

print(my_lst.index(100))


        

        
        
        











