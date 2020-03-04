class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None


def nth_to_last_node(head, n_before):
    start_node = head
    counter = 0
    while head.next is not None:
        head = head.next
        counter += 1
    else:
        # tail = head
        counter += 1

    if n_before > counter:
        return 'invalid position'

    for node_position in range(counter - n_before):
        start_node = start_node.next

    return start_node


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