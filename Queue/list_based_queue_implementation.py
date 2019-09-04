"""
    Implement Queue using list data structure

    Queues, like the name suggests, follow the First-in-First-Out (FIFO) principle. As if waiting 
    in a queue for the movie tickets, the first one to stand in line is the first one to buy a 
    ticket and enjoy the movie.

    Queue is a list or collection with restriction that insertion can be only perform at one end (rear)
    and deletion can be performed at other end (front).


    Implement the following functions for the queue;
    1. Enqueue - add the element at the end of
    2. Dequeue - remove the element from the begningof the queue
    3. size - size of the queue

    Applications:
    1. Network Printer - (Program manager puts request in a queue as long as someting printing on
       the printer)
    2. Process schduling
    3. Simulating wait

"""



class Queue:

    # initialize the queue
    def __init__(self):
        self.queue = list()

    
    # add element at the end of queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove element from the begning
    def dequeue(self):
        if self.queue_size > 0:
            self.queue.pop(0)

    # size of the queue
    def queue_size(self):
        return len(self.queue)



# initialize the queue
queue = Queue()
queue.enqueue(6)
queue.enqueue(7)
print(queue.queue_size)
queue.dequeue
print(queue.queue_size)