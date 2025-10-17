'''
Author: Elsie Amao
Assignment: Lab 4 - Stacks
Filename: leaky_stacks.py
Course: CSIT 200-01, Fall 2025
'''

class LeakyStack:
    def __init__(self, c):
        self.stack = []
        self.capacity=c
        self.size=0
        self.top=None

    def make_array(self, n):                       
        """Return new array with capacity c.""" # T(n) = 
        return self.stack
    
    
    def push(self, element):
        """Add element to the top of stack""" # T(n) = 
        if self.size < self.capacity:
            self.stack.append(element) # store newest item at end of list
            self.size+=1
            self.top+=1
        else:
            for i in range(self.size):
                self.stack[i] = self.stack[i+1]
            self.stack.append(element) # store newest item at end of list

    def pop(self):
        """Remove and return top element of stack.""" # T(n) = 
        if self.is_empty():
            raise IndexError('Stack is empty')      # raise IndexError if stack is empty.
        self.top-=1
        self.size-=1
        return self.stack.pop()
    
    def top(self):
        """Return top element of the stack.""" # T(n) = 
        if self.is_empty():
            raise IndexError('Stack is empty')      # raise IndexError if stack is empty.
        return self.stack[-1]
    
    def is_empty(self):
        """Return True if stack is empty""" # T(n) = 
        return len(self.stack) == 0
    
    def __len__(self):
        """Return number of elements in stack""" # T(n) = 
        return len(self.stack)
    
    