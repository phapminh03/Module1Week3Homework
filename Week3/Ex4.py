class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []
    
    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        return False
    
    def is_full(self):
        if len(self.__queue) == self.__capacity:
            return True
        return False
    
    def dequeue(self):
        if self.is_empty():
            print("Do nothing!")
            return None
        return self.__queue.pop(0)
    
    def enqueue(self, value):
        if self.is_full():
            print("Do nothing!")
        else:
            self.__queue.append(value)

    def front(self):
        if self.is_empty():
            print("Do nothing!")
            return None
        return self.__queue[0]
    
q1 = MyQueue(5)
q1.enqueue(1)
q1.enqueue(2)
print(q1.is_full())
print(q1.front())
print(q1.dequeue())
print(q1.front())
print(q1.dequeue())
print(q1.is_empty())

