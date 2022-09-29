#methods 2

class Counter:
    def __init__(self):  # i don't want the user to pass a specific count value so I am just initializing it to "0".
        self.count = 0
        self.locked = False
    
    def toggle_lock(self):
        self.locked = not self.locked
                                                                        #insted if self.locked == True:
                                                                        #           self.locked = False
                                                                        #       else:
                                                                        #           self.locked = False
    def increment(self):
        if self.locked:
            raise Exception("The counter is locked!!")
        self.count += 1
    
    def decrement(self):
        if self.locked:
            raise Exception("The counter is locked!!")
        self.count -= 1
    
    def print_count(self, name):
        self.name = name
        print(f"The current count for {self.name} is {self.count}")

counter = Counter()   # here we are not passing any values because we initialized count to 0 in the init method.
counter2 = Counter()    #2nd counter, doesn't effect the other counter...

counter.increment()
counter2.increment()
counter2.increment()
counter.print_count('counter')
counter2.print_count('counter2')
counter.decrement()
counter.print_count()
counter.increment()
counter.increment()
counter.increment()
counter.print_count()
counter.toggle_lock()
counter.increment()
counter.print_count()

#how to differentiat the both counters while printing

