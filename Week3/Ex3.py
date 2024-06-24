class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []
    
    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        return False
    
    def is_full(self):
        if len(self.__stack) == self.__capacity:
            return True
        return False
    
    def pop(self):
        if self.is_empty():
            print("Do nothing!")
            return None
        return self.__stack.pop()
    
    def push(self, value):
        if self.is_full():
            print("Do nothing!")
        else:
            self.__stack.append(value)

    def top(self):
        if self.is_empty():
            print("Do nothing!")
            return None
        return self.__stack[-1]
    
