from array_stack import ArrayStack

def empty_stack():
    return ArrayStack()

def test_lifo():
    stack = empty_stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_len():
    stack = empty_stack()
    assert len(stack) == 0
    stack.push(32)
    assert len(stack) == 1
    stack.push(32)
    assert len(stack) == 2
    stack.push(32)
    assert len(stack) == 3
    stack.pop()
    assert len(stack) == 2
    stack.pop()
    assert len(stack) == 1
    stack.pop()
    assert len(stack) == 0

def test_is_empty():
    stack = empty_stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()

def test_top():
    stack = empty_stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top() == 3
    assert not stack.is_empty()
    assert len(stack) == 3

def test_pop_empty_is_error():
    stack = empty_stack()
    try:
        stack.pop()
        assert False # should not get here
    except Exception:
        assert True

def test_top_empty_is_error():
    stack = empty_stack()
    try:
        stack.top()
        assert False # should not get here
    except Exception:
        assert True

def run_all_tests(function_list):
    import traceback
    
    for function in function_list:
        try:
            function()
            print('Passed test for', function.__name__)
        except AssertionError:
            print('Failed test for', function.__name__, '-- Assertion failed')
            print(traceback.format_exc())
        except Exception:
            print('Failed test for', function.__name__, '-- Another error occurred')
            print(traceback.format_exc())

test_functions = [test_lifo, test_len, test_is_empty, test_top, test_pop_empty_is_error, test_top_empty_is_error]
run_all_tests(test_functions)