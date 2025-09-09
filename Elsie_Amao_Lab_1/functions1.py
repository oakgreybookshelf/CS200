'''
Name: Elsie Amao
Date: 9/2/25
Class-section: CS-200-01
Assignment: Lab 1

File: functions1.py
'''

def word_cound(n, word_list):
    leng = 0
    number = 0
    for word in word_list:
        for chr in word:
            number += 1
        if number >= n:
            leng += 1
        number = 0
    print(leng, "words are more than", n, "characters long.")

#WIP
def prime_info(int_list):
    digits = [2,3,4,5,6,7,8,9]
    primes = []
    passes = 0
    
    for int in int_list:
        for dig in digits:
            if int % dig != 0:
                passes += 1
        if passes >= 7:
            print(passes)
            primes.append(int)
        passes = 0

    max = 0
    for num in int_list:
        if num > max:
            max = num
    
    min = max
    for num in int_list:
        if (num < min and num > 1):
            min = num

    print(primes)
    print("the least prime number is", min)


'''def redundance_info(int_list):
    num2 = 0
    nums = int_list
    for num in int_list:
        if num in nums:
            int_list.remove(int_list[0])
            num2 += 1
            print(num, "has", num2, "duplicates")


def redundance_info(int_list):
    number = 0
    num2 = 0
    nums = int_list
    for num in int_list:
        while num in nums:
            num2 += 1
            nums.remove(num)
            if num2 >= 2:
                number += 1
        print(num, "has", num2, "duplicates")
        num2 = 0
    print(number, "numbers have duplicates")

            
'''
def redundance_info(int_list):
    number = 0
    num2 = 0
    nums = int_list
    for num in nums:
        while num in nums:
            num2 += 1
            nums.remove(num)
            if num2 == 2:
                number += 1
        num2 = 0
    print(number, "numbers have duplicates")


def second_max(int_list):
    max = 0
    for num in int_list:
        if num > max:
            max = num

    max2 = 0
    for num in int_list:
        if (num > max2 and num < max):
            max2 = num

    print(max2)
    
#OUTPUT
word_cound(5, ['green', 'blue', 'marigold'])
print()
prime_info([2, 3, 13, 15, 17, 18, 18, 14])
redundance_info([3,6,8,7])
second_max([12, 34, 203, 98, 67]) # output should be 98
