class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None


def display_next(node):
    while node.next is not None:
        print(node.next.data)
        node = node.next
    else:
        print(node.next)


def reverse_list(head):
    current_node = head
    prev_node = None
    next_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

print('before reversal')
display_next(node1)

print('after reversal')
display_next(reverse_list(node1))
