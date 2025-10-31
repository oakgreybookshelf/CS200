
class Deque:
    '''
    Provides O(1) add and remove operations from both ends
    of the sequence.
    '''

    def __init__(self):
        '''Create attributes and initialize empty Deque. '''
        self.deque = []
        self.next = None
        self.previous = None

    def add_to_front(self, x):
        '''Add the value x to the front. O(1).'''
        self.deque[0].previous = x
        x = self.deque[0].previous

    def add_to_end(self, x):
        '''Add the value x to the back. O(1).'''
        self.deque[-1].next = x
        x = self.deque[-1].next

    def remove_from_front(self):
        '''Remove and return the first element. O(1).'''
        self.deque[0] = None

    def remove_from_end(self):
        '''Remove and return the last element. O(1).'''
        self.deque[-1] = None

    def __len__(self):
        '''The number of items in the Deque. O(1).'''
        return len(self.deque)

    def __str__(self):
        '''A string with all of the elements in order. O(n).'''
        return self.deque
