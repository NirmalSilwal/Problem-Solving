class DoublyLinkedListNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


doubly_node1 = DoublyLinkedListNode(10)
doubly_node2 = DoublyLinkedListNode(20)
doubly_node3 = DoublyLinkedListNode(30)
doubly_node4 = DoublyLinkedListNode(40)

doubly_node1.next = doubly_node2
doubly_node2.prev = doubly_node1
doubly_node2.next = doubly_node3
doubly_node3.prev = doubly_node2
doubly_node3.next = doubly_node4
doubly_node4.prev = doubly_node3

print(doubly_node2.prev.data)
print(doubly_node2.next.data)
print(doubly_node2.data)
print(doubly_node4.next)
print(doubly_node1.prev)



