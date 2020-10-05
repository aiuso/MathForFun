'''
Generates a random binary search tree using binary tree package.
Random integer k is assigned
Function sums left and right child nodes to see if equal to k.
Returns parent node; height; and child nodes
'''


import functions
from binarytree import build


k = functions.random_int(2, 40)
list = []
height_of_node = 0

functions.make_array(list, 127, 1, 20)
binary_tree = build(list)

# Take values from type:binary_tree into list; values contained under parent are nested
parent_nodes_same_height = binary_tree.levels


def find_ifchildren_sumk():
    h = 0
    for node in parent_nodes_same_height:
        bt_height = binary_tree.height + 1  # height is actually stored as depth
        left = 1
        right = 2

        for child in node:
            parent_node = child.values[0]  # parent node is listed in child.values at index 0

            try:
                if child.values[left] + child.values[right] == k:   #checks to see if child nodes sum to target value
                    if h == 0:
                        height_of_node = bt_height
                    else:
                        height_of_node = bt_height - h
                    print(f'Parent node {parent_node} of height {height_of_node} has a left node {child.values[left]} '
                          f'and a right node of {child.values[right]} that equal variable K ({k})')

                else:
                    pass

            except IndexError:  # Nodes without children return IndexError
                break
        h += 1


print(binary_tree, f'\nK = {k}\n')

find_ifchildren_sumk()
print('done')

