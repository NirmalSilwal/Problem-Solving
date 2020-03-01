class Stack(object):

    def __init__(self):
        self.lst = []

    def is_empty(self):
        return self.lst == []

    def get_size(self):
        return len(self.lst)

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        if self.is_empty():
            return 'stack underflow'
        return self.lst.pop()

    def display(self):
        print(*self.lst)


stack = Stack()
# print(stack.is_empty())
# print(stack.get_size())
# print(stack.pop())
stack.push(1)
stack.push(2)
stack.push(3)
# print(stack.get_size())
print(stack.pop())
print(stack.display())
print(stack.pop())
print(stack.display())