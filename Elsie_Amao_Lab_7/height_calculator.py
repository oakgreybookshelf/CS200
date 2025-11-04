'''
Author: Elsie Amao
Course: CSIT 200
'''

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

def create_tree(node, input):
    # Add your implementation here to create the binary trees specified in the lab instructions
    if type(node) == int:
        node = BinaryTreeNode(input[0])
    input.remove(input[0])
    if input != []:
        if input[0] < node.value:
            if node.left is None:
                next_node = BinaryTreeNode(input[0])
                node.left = next_node
            create_tree(next_node, input)
        else:
            if node.right is None:
                next_node = BinaryTreeNode(input[0])
                node.right = next_node
            create_tree(next_node, input)
    else:
        print('done')

def main():
    # Call the function for each tree to find its height, and print the heights.
    tree1 = create_tree(35, [35, 4, 80, 2, 20,45,15])
    tree2 = create_tree(35, [35, 14, 68, 9, 24, 45, 75])
    tree3 = create_tree(50, [50, 37, 98, 39, 85, 45, 75])
    print(tree_height(tree1))
    print(tree_height(tree2))
    print(tree_height(tree3))
main()
