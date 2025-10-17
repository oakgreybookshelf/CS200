from deque import Deque
import traceback

def test_add_to_front_and_remove_from_front():
    '''First in last out'''
    deque = Deque()
    if len(deque) != 0:
        return False
    deque.add_to_front(3)
    if len(deque) != 1:
        return False
    deque.add_to_front(4)
    if len(deque) != 2:
        return False
    deque.add_to_front(5)
    if len(deque) != 3:
        return False

    if deque.remove_from_front() != 5:
        return False
    if len(deque) != 2:
        return False
    if deque.remove_from_front() != 4:
        return False
    if len(deque) != 1:
        return False
    if deque.remove_from_front() != 3:
        return False
    if len(deque) != 0:
        return False

    return True

def test_add_to_end_and_remove_from_end():
    '''First in last out'''
    deque = Deque()
    if len(deque) != 0:
        return False
    deque.add_to_end(3)
    if len(deque) != 1:
        return False
    deque.add_to_end(4)
    if len(deque) != 2:
        return False
    deque.add_to_end(5)
    if len(deque) != 3:
        return False
    
    if deque.remove_from_end() != 5:
        return False
    if len(deque) != 2:
        return False
    if deque.remove_from_end() != 4:
        return False
    if len(deque) != 1:
        return False
    if deque.remove_from_end() != 3:
        return False
    if len(deque) != 0:
        return False

    return True

def test_add_to_front_and_remove_from_end():
    '''First in first out'''
    deque = Deque()
    if len(deque) != 0:
        return False
    deque.add_to_front(3)
    if len(deque) != 1:
        return False
    deque.add_to_front(4)
    if len(deque) != 2:
        return False
    deque.add_to_front(5)
    if len(deque) != 3:
        return False

    if deque.remove_from_end() != 3:
        return False
    if len(deque) != 2:
        return False
    if deque.remove_from_end() != 4:
        return False
    if len(deque) != 1:
        return False
    if deque.remove_from_end() != 5:
        return False
    if len(deque) != 0:
        return False

    return True

def test_add_to_end_and_remove_from_front():
    '''First in first out'''
    deque = Deque()
    if len(deque) != 0:
        return False
    deque.add_to_end(3)
    if len(deque) != 1:
        return False
    deque.add_to_end(4)
    if len(deque) != 2:
        return False
    deque.add_to_end(5)
    if len(deque) != 3:
        return False

    if deque.remove_from_front() != 3:
        return False
    if len(deque) != 2:
        return False
    if deque.remove_from_front() != 4:
        return False
    if len(deque) != 1:
        return False
    if deque.remove_from_front() != 5:
        return False
    if len(deque) != 0:
        return False

    return True

def test_remove_from_front_of_empty_is_error():
    deque = Deque()
    try:
        deque.remove_from_front()
        return False
    except Exception:
        return True

def test_remove_from_back_of_empty_is_error():
    deque = Deque()
    try:
        deque.remove_from_end()
        return False
    except Exception:
        return True

def test_str():
    deque = Deque()
    if str(deque) != '[]':
        return False
    deque.add_to_end(1)
    if str(deque) != '[1]':
        return False
    deque.add_to_end(2)
    if str(deque) != '[1, 2]':
        return False
    deque.add_to_front(3)
    if str(deque) != '[3, 1, 2]':
        return False
    deque.remove_from_end()
    if str(deque) != '[3, 1]':
        return False

    return True

def run_all_tests():
    try:
        print('Test add/remove from front:', test_add_to_front_and_remove_from_front())
        print('Test add/remove from end:', test_add_to_end_and_remove_from_end())
        print('Test add to front/remove from end:', test_add_to_front_and_remove_from_end())
        print('Test add to end/remove from front:', test_add_to_end_and_remove_from_front())
        print('Test remove from front empty:', test_remove_from_front_of_empty_is_error())
        print('Test remove from back empty:', test_remove_from_back_of_empty_is_error())
        print('Test str:', test_str())
    except Exception as e:
        print('FAILED one or more tests due to exception')
        traceback.format_exc()

run_all_tests()