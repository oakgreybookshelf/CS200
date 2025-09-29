'''
Author: Elsie Amao
Assignment: Lab 4 - Stacks
Filename: leaky_stacks_test.py
Course: CSIT 200-01, Fall 2025
'''

# PUT YOUR TESTS HERE

from leaky_stack import LeakyStack
import time
function = LeakyStack()
def run_all_tests(function_list):
    import traceback
    
    for function in function_list:
        start = time.time()
        try:
            function()
            print('Passed test for', function.make_array)
        except AssertionError:
            print('Failed test for', function.push, '-- Assertion failed')
            print(traceback.format_exc())
        except Exception:
            print('Failed test for', function.pop, '-- Another error occurred')
            print(traceback.format_exc())
        end = time.time() - start
        print(function, 'runtime:', end)

test_functions = [function] # Give the name of your test functions in this list. All functions must be *ABOVE* this line of code.
run_all_tests(test_functions)