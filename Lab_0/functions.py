'''
Name: Elsie Amao
Date: 8/26/25
Class-section: CS200-01
Assignment: Lab 0

File: functions.py
'''

def difference(numbers_list):
    '''
    Return the difference between the largest and smallest number in
    given list of numbers. Assumes numbers is not empty.
    '''
    max = 0
    for num in numbers_list:
        if num > max:
            max = num
    
    min = max
    for num in numbers_list:
        if num < min:
            min = num
    
    sub = max - min
    return sub

def sum_even_cubes(pos_integer):
    '''
    Returns a sum after adding the cubes of all even numbers less than
    given positive integer. Assumes integer greater than zero.
    '''
    list1 = []
    list2 = []
    total = 0
    for num in range(1,pos_integer):
        list1.append(num)

    for num in list1:
        if num % 2 == 0:
            list2.append(num)

    for num in list2:
        num = num * num * num
        total += num

    return total

def has_duplicate(num_list):
    '''
    Returns True if a given list has an element that appears more
    than twice, returns False othewise. Assumes list is not empty.
    '''
    num2 = 0
    nums = num_list
    for i in range(0, len(num_list)):
        num2 += 1
        nums.remove(nums[i])
        if num in nums:
            return True
        else:
            return False

def list_product(numbers_list, num_list):
    '''
    Returns the product of integers at the same index from two
    lists. Assumes both lists are the same length, and are not empty.
    '''
    list3 = []
    for i in range(0, len(num_list)):
        answer = num_list[i] * numbers_list[i]
        list3.append(answer)
    return list3

#OUTPUT
#print(has_duplicate([7,3,0,0]))