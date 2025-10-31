'''
Author: Elsie Amao
Course: CSIT 200
'''


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Uncomment the following functions and implement them.

def tree_height(input):
  # add your implementation for height calculation.
  # YOU MUST USE THE SAME IMPLEMENTATION FOR ALL THE TREES CREATED.
  # Meaning, it should be a generic one that can calculate height for any binary tree.
    height =
    root = input[0]
    node = BinaryTreeNode(root)
    input.remove(input[0])
# leaf node is base case, left and right would be none
# Base case: when root is none return -1, one node height is 0
    if input != []:
        if input[0] < root:
            if node.left is not None:
                height += 1
                input.remove(input[0])
            #tree_height(input)
        else:
            if node.left is not None:
                height += 1 
            tree_height()
    print(height)
    """
    height += 1
    b = BinaryTreeNode(root)
    if root is None:
        return height
    else:
        print(root.data, end=' ')
        tree_height(root.left)
        tree_height(root.right)
        height += 0
    """



# a, b, c, d, e, f, g, h, i, j, k
def create_tree(input):
    # Add your implementation here to create the binary trees specified in the lab instructions
    """
    for i in input:
        if i is not None:
            i = input[]
    """
    root = input[0]
    node = BinaryTreeNode(root)
    input.remove(input[0])
    if input != []:
        if input[0] < root:
            if node.left is None:
                next_node = BinaryTreeNode(input[0])
                node.left = next_node
            create_tree(input)
        else:
            if node.right is None:
                next_node = BinaryTreeNode(input[0])
                node.right = next_node
            create_tree(input)
    else:
        print('done')

"""
    node1 = BinaryTreeNode(a)
    if (b < a) and (c > a):
        node1.left = BinaryTreeNode(b)
        node1.right = c
    elif (b < a) and (c < a):
        node1.left  = BinaryTreeNode(b)
        BinaryTreeNode(b).left = BinaryTreeNode(c)
    elif (b > a) and (c < a):
        node1.right  = BinaryTreeNode(b)
        node1.left  = BinaryTreeNode(c)
    else:
        node1.right = BinaryTreeNode(b)
        BinaryTreeNode(b).right = BinaryTreeNode(c)


    node4 = BinaryTreeNode(d)
    node5 = BinaryTreeNode(e)
    node6 = BinaryTreeNode(f)
    node7 = BinaryTreeNode(g)
    node8 = BinaryTreeNode(h)
    node9 = BinaryTreeNode(i)
    node10 = BinaryTreeNode(j)
    node11 = BinaryTreeNode(k)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9
    node5.left = node10
    node5.right = node11

"""

def main():
    # Call the function for each tree to find its height, and print the heights.
    tree1 = create_tree([35, 4, 80, 2, 20,45,15])
    tree2 = create_tree([35, 14, 68, 9, 24, 45, 75])
    tree3 = create_tree([50, 37, 98, 39, 85, 45, 75])
    tree_height([35, 4, 80, 2, 20,45,15])
main()
