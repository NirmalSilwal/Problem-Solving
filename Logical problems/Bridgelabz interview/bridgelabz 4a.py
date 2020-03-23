class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def traverse_list(head):
    while head.next is not None:
        print(head.data)
        head = head.next

    print(head.data)


def reverse_me(head):
    p1 = head
    p2 = head.next

    p1.next = None
    while p2 is not None:
        temp = p2
        p2 = p2.next

        temp.next = p1
        p1 = temp

    return p1


first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)

# linking the nodes to make singly linked list

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

rev = reverse_me(first_node)
traverse_list(rev)