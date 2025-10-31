from doubly_linked_node import DoublyLinkedNode
import traceback

def test_node():
    '''
    A DoublyLinkedNode is constructed from an item.
    Its next and previous pointers are initially None.
    '''
    a = DoublyLinkedNode('a')
    if a.item != 'a':
        return False
    if a.next is not None:
        return False
    if a.previous is not None:
        return False
    return True

def test_link_as_next():
    '''link_as_next links two nodes together, modifying both.'''
    a = DoublyLinkedNode("a")
    b = DoublyLinkedNode("b")
    a.link_as_next(b)
    if a.next != b:
        return False
    if a != b.previous:
        return False
    return True

def test_link_as_next_None():
    '''Passing None is allowed. Doing so sets next to None.'''
    a = DoublyLinkedNode("a")
    a.link_as_next(None)
    if a.next is not None:
        return False
    return True

def test_link_as_next_to_a_different_node():
    '''
    Link a node after it has been linked to another only
    modifies the node it is called on and the new node. The
    other node is not modified, and still points back to
    the one that we are modifying.
    '''
    a = DoublyLinkedNode("a")
    b = DoublyLinkedNode("b")
    c = DoublyLinkedNode("c")
    a.link_as_next(b)
    a.link_as_next(c)
    if a.next != c:
        return False
    if a != c.previous:
        return False
    if a != b.previous:  # Check that b's previous is unchanged
        return False
    return True

def test_clear():
    '''
    Sets references in node to None. Does not modify others.
    '''
    a = DoublyLinkedNode("a")
    b = DoublyLinkedNode("b")
    c = DoublyLinkedNode("c")
    a.link_as_next(b)
    b.link_as_next(c)
    b.clear()
    # Checking modifications to b's pointers.
    if b.next is not None:
        return False
    if b.previous is not None:
        return False
    if b.item is not None:
        return False
    # Checking that a and c are unchanged.
    if a.next != b:
        return False
    if c.previous != b:
        return False

    return True

def test_insert_before_next():
    '''
    Scenario: self has a next.
    before: a <-> b
    a.insert_before_next(c)
    after: a <-> c <-> b
    '''
    a = DoublyLinkedNode("a")
    b = DoublyLinkedNode("b")
    c = DoublyLinkedNode("c")
    a.link_as_next(c)
    a.insert_before_next(b)
    if a.next != b:
        return False
    if a != b.previous:
        return False
    if b.next != c:
        return False
    if b != c.previous:
        return False
    return True

def test_insert_before_next_without_next():
    '''
    Scenario: self does not have a next.
    before: a
    a.insert_before_next(b)
    after: a <-> b
    '''
    a = DoublyLinkedNode("a")
    b = DoublyLinkedNode("b")
    a.insert_before_next(b)
    if a.next != b:
        return False
    if a != b.previous:
        return False
    return True

def test_insert_before_next_both_have_next():
    '''
    Scenario: node has a next.
    before: a <-> b   c <-> d
    a.insert_before_next(c)
    after: a <-> c <-> b
                 ^
                  `- d
    '''
    a = DoublyLinkedNode("a")
    b = DoublyLinkedNode("b")
    c = DoublyLinkedNode("c")
    d = DoublyLinkedNode("d")
    a.link_as_next(b)
    c.link_as_next(d)
    a.insert_before_next(c)
    if a.next != c:
        return False
    if a != c.previous:
        return False
    if c.next != b:
        return False
    if c != b.previous:
        return False
    if c != d.previous:   # d still points to c
        return False  
    return True

def test_insert_before_next_only_other_has_next():
    '''
    Scenario: self does not have next and node does
    before: a   b <-> c
    a.insert_before_next(b)
    after: a <-> b <- c
    Notice c points to b, but b does not point to c. b points to None.
    '''
    a = DoublyLinkedNode("a")
    b = DoublyLinkedNode("b")
    c = DoublyLinkedNode("c")
    b.link_as_next(c)
    a.insert_before_next(b)
    if a.next != b:
        return False
    if a != b.previous:
        return False
    if b.next is not None:
        return False
    if b != c.previous:
        return False
    return True

def test_delete_next_when_next_is_None():
    '''
    Scenario: next is None.
    before: a
    a.delete_next()
    side effect: raise error
    '''
    a = DoublyLinkedNode("a")
    try:
        a.delete_next()
        return False
    except Exception:
        return True

def test_delete_next_when_next_next_is_None():
    '''
    Scenario: next's next is None
    before: a <-> b
    a.delete_next()
    after: a <- b
    Notice that b still points to a.
    '''
    a = DoublyLinkedNode('a')
    b = DoublyLinkedNode('b')
    a.link_as_next(b)
    a.delete_next()
    if a.next is not None:
        return False
    if a != b.previous:
        return False
    return True

def test_delete_next_general():
    '''
    Scenario: general
    before: a <-> b <-> c
    a.delete_next()
    after: a <---> c
           ^       ^
            `- b -'
    Notice b still points to the others.
    '''
    a = DoublyLinkedNode('a')
    b = DoublyLinkedNode('b')
    c = DoublyLinkedNode('c')
    a.link_as_next(b)
    b.link_as_next(c)
    a.delete_next()
    if a.next != c:
        return False
    if a != c.previous:
        return False
    if a != b.previous:
        return False
    if b.next != c:
        return False
    return True

def run_all_tests():
    #try:
    print('Test node:', test_node())
    print('Test link as next:', test_link_as_next())
    print('Test link as next None:', test_link_as_next_None())
    print('Test link as next to a different node:', test_link_as_next_to_a_different_node())
    print('Test clear:', test_clear())
    print('Test insert before next:', test_insert_before_next())
    print('Test insert before next without next:', test_insert_before_next_without_next())
    print('Test insert before next both have next:', test_insert_before_next_both_have_next())
    print('Test insert before next only other has next:', test_insert_before_next_only_other_has_next())
    print('Test delete next when next is None:', test_delete_next_when_next_is_None())
    print('Test delete next when next next is None:', test_delete_next_when_next_next_is_None())
    print('Test delete next general:', test_delete_next_general())
    #except Exception as e:
        #print('FAILED one or more tests due to exception')
        #traceback.format_exc()

run_all_tests()