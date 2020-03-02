class Queue2Stack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


q2stack  = Queue2Stack()

for i in range(1,6):
    q2stack.enqueue(i)

for i in range(5):
    print(q2stack.dequeue())