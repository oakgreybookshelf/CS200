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

def tree_height(root):
  # add your implementation for height calculation.
  # YOU MUST USE THE SAME IMPLEMENTATION FOR ALL THE TREES CREATED.
  # Meaning, it should be a generic one that can calculate height for any binary tree.
  if root is None:
    return 0
  else:
    leftheight = tree_height(root.left)
    rightheight = tree_height(root.right)
    return 1 + max(leftheight, rightheight) 
    """root = input[0]
    node = BinaryTreeNode(root)
    input.remove(input[0])"""

    if input.root is None:
        height = 0
        return height
    elif (root.left is None) and (root.right is None):
        height = 1
    elif root.left is not None:
        height += 1
        root = root.left
        tree_height(input)


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

def creat_tree(input):
    # Add your implementation here to create the binary trees specified in the lab instructions
    #root = input[0]
    #height = len()
    node = BinaryTreeNode(root)
    #input.remove(input[0])
    height = 0
    def fun(input, height):
        root = input[0]
        input.remove(input[0])
        if root is None:
            print(height)
        elif (root.left is None) and (root.right is None):
            print(height + 1)
        else:
            height += 1
            input.remove(input[0])
            fun(input, height)
    fun(input, height)
"""
    
    elif len(input) >= 1:
        if input[0] < root:
            if node.left is not None:
                height += 1
            else:
                next_node = BinaryTreeNode(input[0])
                node.left = next_node
            creat_tree(input)
        else:
            if node.right is not None:
                height += 1
            else:
                next_node = BinaryTreeNode(input[0])
                node.right = next_node
            creat_tree(input)
    else:
        print("k")
        print(height, 'l')
"""
def create_tree(input):
    # Add your implementation here to create the binary trees specified in the lab instructions
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
    root = input[0]
    node = BinaryTreeNode(root)
    input.remove(input[0])
    def create_ree(input, root):
        #node = BinaryTreeNode(root)
        if input != []:
            if input[0] < root:
                if node.left is None:
                    next_node = BinaryTreeNode(input[0])
                    node.left = next_node
                create_ree(input, node.left)
            else:
                if node.right is None:
                    next_node = BinaryTreeNode(input[0])
                    node.right = next_node
                create_ree(input, node.right)
        else:
            print('done')
    create_ree(input, root)
    """

def pre_order_dfs(node):
    if node is None:
        return
    print(node.data, end=' ')
    height += 1
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)


def main():
    # Call the function for each tree to find its height, and print the heights.
    tree1 = create_tree([35, 4, 80, 2, 20,45,15])
    tree2 = create_tree([35, 14, 68, 9, 24, 45, 75])
    tree3 = create_tree([50, 37, 98, 39, 85, 45, 75])
    #tree_height([35, 4, 80, 2, 20,45,15])
    tree_height(tree1.root)
    #creat_tree([35, 4, 80, 2, 20,45,15])
main()
