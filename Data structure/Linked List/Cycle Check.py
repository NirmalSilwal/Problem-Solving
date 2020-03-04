class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None


def singly_linked_list_cycle_check(node):
    while node.next is not None:
        node = node.next
        if node.next == node1:
            return True

    return False


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

#making circulaly linked list for checking cycle
node3.next = node1

is_cycle = singly_linked_list_cycle_check(node1)
print(f'cycle present in this linked list: {is_cycle}')