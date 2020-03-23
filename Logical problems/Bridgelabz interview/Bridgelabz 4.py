class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def traverse_list(head):
    while head.next is not None:
        print(head.data)
        head = head.next

    print(head.data)


def reverse_list(head):

    # edge case
    if head.next is None or head is None:
        return head

    arr_data = []
    cursor = head
    while cursor.next is not None:
        arr_data.append(cursor.data)
        cursor = cursor.next

    arr_data.append(cursor.data)

    index = len(arr_data)-1

    while head.next is not None:
        head.data = arr_data[index]
        print(head.data)
        index -= 1
        head = head.next
    else:
        head.data = arr_data[index]
    print(head.data)


first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)

# linking the nodes to make singly linked list

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

traverse_list(first_node)

print('after reversing the list: ')

reverse_list(first_node)
