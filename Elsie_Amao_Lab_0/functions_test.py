'''
Name: Elsie Amao
Date: 8/26/25
Class-section:
Assignment: Lab 0

File: functions_test.py
'''


from functions import *


def test_difference():
    '''
    Check that difference() behaves correctly.
    '''
    num_tests = 4
    passes = 0

    if difference([1,2,3,4,5]) == 4:
        passes += 1
    else:
        print('Failed first difference test')
    
    if difference([10,7,42,107,53,99]) == 100:
        passes += 1
    else:
        print('Failed second difference test')
    
    if difference([0.5,0.25,0.4,0.9,-0.1]) == 1.0:
        passes += 1
    else:
        print('Failed third difference test')
    
    if difference([5,5,5,5,5]) == 0:
        passes += 1
    else:
        print('Failed fourth difference test')
    
    if passes == 4:
        print('Passed all difference() tests')


def test_sum_even_cubes():
    '''
    Check that sum_even_cubes() behaves correctly.
    '''
    num_tests = 4
    passes = 0

    if sum_even_cubes(5) == 72:
        passes += 1
    else:
        print('Failed first sum_even_cubes test')
    
    if sum_even_cubes(6) == 72:
        passes += 1
    else:
        print('Failed second sum_even_cubes test')
    
    if sum_even_cubes(9) == 800:
        passes += 1
    else:
        print('Failed third sum_even_cubes test')
    
    if sum_even_cubes(2) == 0:
        passes += 1
    else:
        print('Failed fourth sum_even_cubes test')
    
    if passes == 4:
        print('Passed all sum_even_cubes() tests')


def test_has_duplicate():
    '''
    Check that has_duplicate() behaves correctly.
    '''
    num_tests = 3
    passes = 0

    if has_duplicate([7,0,3,0]) == True:
        passes += 1
    else:
        print('Failed first has_duplicate test')
    
    if has_duplicate([7,6,5,4,3,2,1,0]) == False:
        passes += 1
    else:
        print('Failed second has_duplicate test')
    
    if has_duplicate([]) == False:
        passes += 1
    else:
        print('Failed third has_duplicate test')
    
    if passes == 3:
        print('Passed all has_duplicate() tests')


def test_list_product():
    '''
    Check that list_product() behaves correctly.
    '''
    num_tests = 2
    passes = 0

    if list_product([1,2,3],[4,5,6]) == [4,10,18]:
        passes += 1
    else:
        print('Failed list_product test')
    
    if list_product([2,2,2,2],[7,8,9,10]) == [14,16,18,20]:
        passes += 1
    else:
        print('Failed second list_product test')
    
    if passes == 2:
        print('Passed all list_product() tests')


#OUTPUT
test_difference()
test_sum_even_cubes()
test_has_duplicate()
test_list_product()