#Cars lined up in a car wash
import random as rnd
import module_queue as queue

class Wash:                                 #tracks if it has a current task

    def __init__(self, cph):
        self.car_rate = cph
        self.current_task = None
        self.time_remaining = 0
        
    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
    
    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_cars() *60/self.car_rate  #smth about timing



class Task:                                     #timestamp represents the time that the task was created and placed in the washing queue
    def __init__(self, time):
        self.timestamp = time
        self.cars = rnd.randrange(1, 6)

    def get_stamp(self):
        return self.timestamp

    def get_cars(self):
        return self.cars

    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulation(num_minute, cars_per_hour):

    washing = Wash(cars_per_hour)
    wash_queue = queue.Queue()
    waiting_times = []

    for current_minute in range(num_minute):

        if new_wash_task():     #create
            task = Task(current_minute)
            wash_queue.enqueue(task) #create

        if (not washing.busy()) and (not wash_queue.is_empty()):
            next_task = wash_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_minute))
            washing.start_next(next_task)

        washing.tick()

    average_wait = sum(waiting_times) / (len(waiting_times))
    print('Average Wait %6.2f min %3d tasks remaining.' %(average_wait, wash_queue.size()))


def new_wash_task():
    num = rnd.randrange(1, 21) 
    if num == 20:
        return True
    else:
        return False



for i in range(10): #10 independent trials
    simulation(180, 4)      #in 3 hours, 4 cars per hour

