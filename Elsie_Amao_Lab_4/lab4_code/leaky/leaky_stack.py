'''
Author: Elsie Amao
Assignment: Lab 4 - Stacks
Filename: leaky_stacks.py
Course: CSIT 200-01, Fall 2025
'''

class LeakyStack:
    def __init__(self):
        self.capacity=1

    def make_array(self, n):                       
        """Return new array with capacity c.""" # T(n) = 
        return []
    
    def push():
        """Add element to the top of stack""" # T(n) = 
        self._data.append(e) # store newest item at end of list
    
    def pop():
        """Remove and return top element of stack.""" # T(n) = 
        if self.is_empty():
            raise IndexError('Stack is empty')      # raise IndexError if stack is empty.
        return self._data.pop()
    
    def top():
        """Return top element of the stack.""" # T(n) = 
        if self.is_empty():
            raise IndexError('Stack is empty')      # raise IndexError if stack is empty.
        return self._data[-1]
    
    def is_empty(self):
        """Return True if stack is empty""" # T(n) = 
        if len(self._data) == 0:
            return True
    
    def __len__(self):
        """Return number of elements in stack""" # T(n) = 
        return len(self._data)
    
    