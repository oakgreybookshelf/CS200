'''Professor's copy' '''

'''
Many of the tests repeatedly test operations as the array grows. This
is because we know that DynamicArrays distinguish between capacity
(the internal size of the array) and the length (the number of elements
stored in the array).

In all cases, test functions return True if the test was passed, False if failed.
'''

from dynamic_array import DynamicArray

b = [1,2,3]
print(b[-2])

def test_append_and_len():
    '''len(da) is the number of elements da contains.'''
    da = DynamicArray()
    for i in range(5):
        da.append(i)
        if len(da) != i+1:
            return False
    return True


def test_getitem():
    '''da[i] should return the item in the i_th position.'''
    da = DynamicArray()
    for i in range(5):
        da.append(i)
        if da[i] != i:
            return False
    return True


def test_getitem_raises_IndexError_if_index_is_too_large():
    '''
    With zero-indexing, indexing by the length of the array is one beyond
    the last legal index.
    '''
    da = DynamicArray()
    try:
        x = da[len(da)]
        print(x)
        return False
    except IndexError:
        pass
    return True

def test_getitem_raises_IndexError_if_index_is_too_small():
    '''
    -1 is the first index smaller than 0 that is invalid.
    '''
    da = DynamicArray()
    try:
        x = da[len(da) + 1]
        print(x)
        return False
    except IndexError:
        pass
    return True

def test_insert():
    '''
    Inserting a value at index k causes all the items at and above index
    k to shift up one index.
    '''
    da = DynamicArray()
    for i in range(5):
        da.append(i)

    da.insert(k=3, value=6)
    if da[3] != 6:
        return False

    # All items below position 3 remain.
    for i in range(0, 3):
        if da[i] != i:
            return False

    # All items at 3 or higher have shifted up one position.
    for i in range(4, len(da)):
        if da[i] != i-1:
            return False

    return True


def test_remove():
    '''
    Removing a value causes all the values above it to shift one index
    lower.
    '''
    da = DynamicArray()
    for i in range(5):
        da.append(i)

    da.remove(value=3)
    if da[3] == 3:
        return False

    # All items below 3 remain.
    for i in range(3):
        if da[i] != i:
            return False

    # All items above 3 shift down one position.
    for i in range(3, len(da)):
        if da[i] != i+1:
            return False

    return True


def test_remove_raises_error_if_value_does_not_exist():
    '''
    Trying to remove a value that doesn't exist raises a ValueError.
    '''
    da = DynamicArray()
    for i in range(5):
        da.append(i)

    try:
        da.remove(100)
        return False
    except ValueError:
        pass
    return True

def run_all_tests():
    '''
    True indicates test was passed, False indicates test failed
    '''
    try:
        print('Test_append_and_len:', test_append_and_len())
        print('Test_getitem:', test_getitem())
        print('Test_getitem_raises_IndexError_if_index_is_too_large:', test_getitem_raises_IndexError_if_index_is_too_large())
        print('Test_getitem_raises_IndexError_if_index_is_too_small:', test_getitem_raises_IndexError_if_index_is_too_small())
        print('Test_insert:', test_insert())
        print('Test_remove:', test_remove())
        print('Test_remove_raises_error_if_value_does_not_exist:', test_remove_raises_error_if_value_does_not_exist())
        
        # Add calls to your test functions here

    except Exception as e:
        print('FAILED one or more tests due to exception')
        print(e)

run_all_tests()