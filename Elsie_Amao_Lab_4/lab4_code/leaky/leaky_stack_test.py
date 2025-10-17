'''
Author: Elsie Amao
Assignment: Lab 4 - Stacks
Filename: leaky_stacks_test.py
Course: CSIT 200-01, Fall 2025
'''

# PUT YOUR TESTS HERE

from leaky_stack import LeakyStack
import time
#function = LeakyStack()
def run_all_tests(function_list):
    import traceback
    '''
    for function in function_list:
        start = time.time()
        try:
            function()
            print('Passed test for', function)
        except AssertionError:
            print('Failed test for', function.push, '-- Assertion failed')
            print(traceback.format_exc())
        except Exception:
            print('Failed test for', function.pop, '-- Another error occurred')
            print(traceback.format_exc())
        end = time.time() - start
        print(function, 'runtime:', end)
        '''
    '''
    test push
    lstack = 5
    push adds data, use for loop add 3 elements # check data without exceeding
    
    check top element, 

    push add more data to exceed LeakyStack # check data with exceeding, confirm leaking

    check top to see if new element is correctly reassigned
    '''
    for function in function_list:
        start = time.time()
        try:
            LeakyStack().push()
            print('Passed test for', function.push)
        except Exception:
            print('Failed test for', function.push, '-- Another error occurred')
            print(traceback.format_exc())
        end = time.time() - start
        print(function, 'runtime:', end)
    # another function for top and for each function

    for function in function_list:
        start = time.time()
        try:
            function()
            print('Passed test for', function)
        except Exception:
            print('Failed test for', function.pop, '-- Another error occurred')
            print(traceback.format_exc())
        end = time.time() - start
        print(function, 'runtime:', end)

    for function in function_list:
        start = time.time()
        try:
            function()
            print('Passed test for', function)
        except Exception:
            print('Failed test for', function.pop, '-- Another error occurred')
            print(traceback.format_exc())
        end = time.time() - start
        print(function, 'runtime:', end)

    for function in function_list:
        start = time.time()
        try:
            function()
            print('Passed test for', function)
        except Exception:
            print('Failed test for', function.pop, '-- Another error occurred')
            print(traceback.format_exc())
        end = time.time() - start
        print(function, 'runtime:', end)

test_functions = [LeakyStack(5).push(5), pop, top, is_empty, len] # Give the name of your test functions in this list. All functions must be *ABOVE* this line of code.
run_all_tests(test_functions)