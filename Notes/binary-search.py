'''
Author name:
CS 200
'''
# VALUE IS MIDDLE
# implement the functions that are not implemented

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # you may initilalize the right, left and data references here.

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)


    def _insert_recursive(self, root, key):
        ''' implement this recursive function to figure out 
        where to insert the new element '''
        if root is None:
            return Node(key)
        if key < root.value:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root


    def search(self, value):
        return self._search_recursive(self.root, value)


    def _search_recursive(self, root, key):
        ''' Search is also a recursive process'''
        if root is None or root.value == key:
            return root.value
        if key < root.value:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)


    def in_order_traversal(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result


    def _in_order_recursive(self, root, result):
        '''Similarly, traversal/visiting is also a recursive function'''
        if root is not None:
            self._in_order_recursive(root.left, result)
            result.append(root.value)
            self._in_order_recursive(root.right, result)


# Example usage:
bst = BinarySearchTree()
bst.insert(10)
print("Search:", bst.search(10))
bst.insert(20)
print("Insert:", bst.search(20))
print("In-order traversal:", bst.in_order_traversal())
#  add function calls to perform other operations





'''
def binary_search(array, target):
    left = 0
    right = 0 len(array) - 1

    while (left <= right):
        mid = (right + left) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid  - 1
    return -1
'''