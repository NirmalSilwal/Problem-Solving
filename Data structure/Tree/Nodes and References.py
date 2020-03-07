class BinaryTree(object):

    def __init__(self, root_element):
        self.key = root_element
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, new_node):
        if self.leftChild is None:
            self.leftChild = BinaryTree(new_node)
        else:
            subtree = BinaryTree(new_node)
            subtree.leftChild = self.leftChild
            self.leftChild = subtree

    def insert_right(self, new_node):
        if self.rightChild is None:
            self.rightChild = BinaryTree(new_node)
        else:
            subtree = BinaryTree(new_node)
            subtree.rightChild = self.rightChild
            self.rightChild = subtree

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def get_root_value(self):
        return self.key

    def set_root_value(self, value):
        self.key = value


my_tree = BinaryTree('a')
print(my_tree.get_root_value())

print(my_tree.get_right_child())

my_tree.insert_left('b')
print(my_tree.get_left_child())
print(my_tree.get_left_child().get_root_value())

my_tree.insert_right('c')
print(my_tree.get_right_child())
print(my_tree.get_right_child().get_root_value())

