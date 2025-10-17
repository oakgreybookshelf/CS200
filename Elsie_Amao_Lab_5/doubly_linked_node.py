
class DoublyLinkedNode:
    '''
    A Node for a doubly linked list. Methods assume sentinels are used.
    '''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.previous = None

    def link_as_next(self, new_next):
        '''
        Link self and new_next so that new_next immediately follows self.
        Do not adjust links between any other nodes.
        '''
        # TODO: Your implementation here.

    def clear(self):
        '''
        Set all references to None. Use this after removing
        a node for a structure to prevent retension.
        '''
        # TODO: Your implementation here.

    def insert_before_next(self, node):
        '''
        Inserts node after self but before next, updating the doubly linked
        structure as necessary.

        Scenario: self has a next.
        before: a <-> b
        a.insert_before_next(c)
        after: a <-> c <-> b

        Scenario: self does not have a next.
        before: a
        a.insert_before_next(c)
        after: a <-> c

        Scenario: self does not have next and node does
        before: a   b <-> c
        a.insert_before_next(b)
        after: a <-> b <- c
        Notice c points to b, but b does not point to c. b points to None.

        Scenario: both have next.
        before: a <-> b   c <-> d
        a.insert_before_next(c)
        after: a <-> c <-> b
                     ^
                      `- d
        '''
        # TODO: Your implementation here. Hint: use link_as_next() a couple times.

    def delete_next(self):
        '''
        Delete the next node after this node.

        Scenario: next is None.
        before: a
        a.delete_next()
        side effect: raise error

        Scenario: next's next is None
        before: a <-> b
        a.delete_next()
        after: a <- b
        Notice that b still points to a.

        Scenario: general
        before: a <-> b <-> c
        a.delete_next()
        after: a <---> c
               ^       ^
                `- b -'
        Notice b still points to the others.
        '''
        # TODO: Your implementation here. Hint: use link_as_next().
