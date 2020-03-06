def binary_tree(root):
    return [root, [], []]


def insert_left(root, new_branch):
    left = root.pop(1)

    if len(left) > 1:
        root.insert(1, [new_branch, left, [] ])
    else:
        root.insert(1,[new_branch, [], []])

    return root


def insert_right(root, new_branch):
    right = root.pop(2)

    if len(right) > 1:
        root.insert(2, [new_branch, [], right])
    else:
        root.insert(2, [new_branch, [], []])

    return root


def get_root_value(root):
    return root[0]


def set_root_value(root,new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


root_node = binary_tree('a')
print('root node: ',root_node)

insert_left(root_node,'b')
print('left branch: ',get_left_child(root_node))

insert_right(root_node, 'c')
print('right branch: ',get_right_child(root_node))

insert_right(root_node, 'd')
print('right branch: ',get_right_child(root_node))

print('tree looks like: ',binary_tree(root_node))