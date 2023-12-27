# Threading
from time import sleep
from threading import Thread, Lock

""" class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)

first_thread = MyThread('First thread', 5)
first_thread.start()

for i in range(20):
    print(i)
    sleep(1) """

""" def thread_function(text, time):
    sleep(time)
    print(text)

t = Thread(target=thread_function, args=('Hello, world!', 5))
t.start()
t.join() """

# while t.is_alive():
#     print('Waiting thread')
#     sleep(2)

#print('Thread is done')

class Tickets:
    def __init__(self, inventory):
        self.inventory = inventory
        self.lock = Lock()

    def buy(self, quantity):
        self.lock.acquire()
        if self.inventory < quantity:
            print("We don't have tickets enough.")
            self.lock.release()
            return
        
        sleep(1)

        self.inventory -= quantity
        print(f'You bought {quantity} tickets. We still have {self.inventory} tickets.')

        self.lock.release()

if __name__ == '__main__':
    tickets = Tickets(10)
    
    for i in range(1, 20):
        t = Thread(target=tickets.buy, args=(i, ))
        t.start()

    print(tickets.inventory)