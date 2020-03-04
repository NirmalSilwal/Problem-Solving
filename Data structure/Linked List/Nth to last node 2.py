class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None


def nth_to_last_node(head, n_before):
    left_pointer = head
    right_pointer = head

    # moving right_pointer to 'n_before' position ahead of head/start node
    for i in range(n_before-1):
        if not right_pointer.next:
            raise LookupError('Error: n is larger than the linked list')

        right_pointer = right_pointer.next

    # while right_pointer.next is not None:   # below line and this line is same

    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer


node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)
node5 = Node(500)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = nth_to_last_node(node1, 2)
try:
    print(result.data)
except Exception:
    print(result)