class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

print(a.data,b.data,c.data)
print(a.nextnode,b.nextnode,c.nextnode)
print(a.nextnode.data)

'''
NOTE:
=====
PROS: Linked List has constant time O(1) Insertion and Deletions in any position. While array takes O(n).
Flexibility in dynamic memory allocation.

CONS: No random access of elements is allowed like in Array. Takes O(k) time to access kth element. You have to 
traverse from head/start node till you reach kth element, so no random access allowed in Linked List.

Thus depending upon the use case, you will be choosing Array or Linked List. If you are looking for fast and 
random access, then go with Array, else Linked list is the better option.
'''