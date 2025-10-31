from singly_linked_list import SingleLinkedList, Node
import traceback

def test_insertion():
    a = SingleLinkedList()
    a.insert_at_start('a')
    #display = a.display()
    if a.head != 'a':
        return False
    return True

# INSER TAT END
def test_end_insert():
    pass

def test_deletion():
    a = SingleLinkedList()
    a.insert_at_start('b')
    a.insert_at_start('c')
    a.insert_at_start('d')
    a.delete('c')
    if a.data is not None:
        return False
    return True

def test_search():
    a = SingleLinkedList()
    a.insert_at_start('b')
    a.insert_at_start('c')
    a.insert_at_start('d')
    search = a.search('d')
    if search != 'd':
        return False
    return True

# test a different way, maybe with error and expect errer in tesT_search, if u recieve errro pass the ytest
def test_search_none():
    a = SingleLinkedList()
    a.insert_at_start('b')
    a.insert_at_start('c')
    a.insert_at_start('d')
    search = a.search('e')
    if search != None:
        return False
    return True

def test_display():
    a = SingleLinkedList()
    a.insert_at_start('b')
    a.insert_at_start('c')
    a.insert_at_start('d')
    display = a.display()
    if display != ['d']:
        return False
    return True

def test_reverse_display():
    a = SingleLinkedList()
    a.insert_at_start('b')
    a.insert_at_start('c')
    a.insert_at_start('d')
    display = a.reverse_display()
    if display is not None:
        return False
    return True

def run_all_tests():
    #try:
    print('Test Insertion:', test_insertion())
    print('Test Deletion:', test_deletion())
    print('Test Search:', test_search())
    print('Test Search None:', test_search_none())
    print('Test Display:', test_display())
    print('Test Reverse Display:', test_reverse_display())
    #except Exception as e:
        #print('FAILED one or more tests due to exception')
        #traceback.format_exc()

run_all_tests()
