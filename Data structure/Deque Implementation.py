class Dequeue(object):

    def __init__(self):
        self.lst = []

    def is_empty(self):
        return self.lst == []

    def get_size(self):
        return len(self.lst)

    def push_front(self, item):
        self.lst.append(item)

    def push_rear(self, item):
        self.lst.insert(0, item)

    def pop_front(self):
        if self.is_empty():
            return 'nothing to pop'
        return self.lst.pop(-1)

    def pop_rear(self):
        if self.is_empty():
            return 'nothing to pop'
        return self.lst.pop(0)

    def display(self):
        print(*self.lst)


deq = Dequeue()
# print(deq.get_size())
# print(deq.is_empty())
# print(deq.display())
# print(deq.pop_front())
# print(deq.pop_rear())
# deq.push_front([1,2])
# deq.display()