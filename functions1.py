'''
Name: Elsie Amao
Date: 9/2/25
Class-section: CS-200-01
Assignment: Lab 1

File: functions1.py
'''
#name zip folder Elsie_Amao_Lab1.
def word_cound(n, word_list):
    for word in word_list:
        for chr in word:
        for num in range(0, n):


def prime_info(int_list):
    prime_list = [2,3,5,7,11,13,17,19,23,29,31,37,43,
                  47,53,59,61,67,71,73,79,83,89,97,101]
    primes = []
    
    for int in int_list:
        if int in prime_list:
            primes.append(int)

    max = 0
    for num in int_list:
        if num > max:
            max = num
    
    min = max
    for num in int_list:
        if (num < min and num > 1):
            min = num

    print(primes)
    print("the least number is", min)

#WIP cannot use count func
def redundance_info(int_list):
    number = 0
    num2 = 0
    nums = int_list
    for num in int_list:
        nums.remove(num)
        if num in nums:
            num2 += 1
            print(num, "has", num2, "duplicates")


def second_max(int_list):
    max = 0
    for num in int_list:
        if num > max:
            max = num

    zero = 0
    max2 = 0
    for num in int_list:
        if (num > zero and num < max):
            max2 = num

    print(max2)
    
#OUTPUT
prime_info([3,6,8,7])

