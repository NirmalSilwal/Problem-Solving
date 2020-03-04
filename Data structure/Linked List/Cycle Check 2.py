"""
Followed pattern: PEP8, python3
@aurthor: Nirmal Silwal
@github: https://github.com/NirmalSilwal
@linkedln: https://www.linkedin.com/in/nirmal-silwal-827341139/
@twitter: https://twitter.com/silwal_nirmal
"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def check_cycle(node):
    marker1 = node
    marker2 = node
    while marker2 is not None and marker2.next is not None:
        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker2 == marker1:
            return True

    return False


# adding nodes in linked list
first_node = Node(1)
second_node = Node(2)
third_node = Node(3)

# forming singly linked list
first_node.next = second_node
second_node.next = third_node

# adding nodes in new linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# forming cycled linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1

# testing
print(f'cycle present: {check_cycle(node1)}')
print(f'cycle present: {check_cycle(first_node)}')
