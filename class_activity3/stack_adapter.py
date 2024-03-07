
from example_007_queue import Queue

class stack_adapter:

    def __init__(self):

       self.queue1 = Queue()

       self.queue2 = Queue()


    def push(self, item):
        self.queue2.enqueue(item)

        while not self.queue1.is_empty():
            self.queue2.enqueue(self.queue1.dequeue())

        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self):
        """
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())
        
        item = self.queue1.dequeue()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return item
        """
        if not self.queue1.is_empty():
           return self.queue1.dequeue()
        return None


 
    def peek(self):
        if not self.queue1.is_empty():
            return self.queue1.queue[self.queue1.size()-1]

#runtime of push: O(n) | pop: O(1) | peek: O(1)
    
stack = stack_adapter()
for i in range(9):
    stack.push(i)
    print("Pushed", i)
print(stack)
for i in range(9):
    stack.pop()
    print("Popped", i)
print(stack.__str__())


