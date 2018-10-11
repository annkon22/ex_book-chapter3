#Modify Hot Potato simulation to
#allow for a randomly chosen counting value so that each pass is not 
#predictable from the previous one


import module_queue as queue
import random as rnd

def hot_potato(name_list):
    sim_queue = queue.Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        num = rnd.randrange(1, 10)
        for _ in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()


print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent','Brad']))