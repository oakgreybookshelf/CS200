'''
Author: Elsie Amao
Assignment: Analysis Lab
Filename: main.py
Course: CSIT 200
'''

import random
import timeit
from functions2 import (
    example1,
    example2,
    example3,
    example4,
    example5,
    prefix_average1,
    prefix_average2,
    prefix_average3
)


def main():
    time_example1()
    time_example2()
    time_example3()
    time_example4()
    time_example5()
    # Define these functions below the definition of time_example1().


def time_example1():
    '''
    Time example1 when called on random lists of increasing lengths,
    and print the results.
    '''
    # The code below is to get you started. Feel free to modify.
    print("example1")
    for n in [10000, 50000, 100000, 500000, 1000000, 10000000]:
        sequence = generate_sequence(n)
        start_time = timeit.default_timer()
        example1(sequence)
        end_time = timeit.default_timer()
        time_elapsed = end_time - start_time
        print(str(n) + ": " + str(time_elapsed) + " seconds")


def time_example2():
    '''
    Time example2 when called on random lists of increasing lengths,
    and print the results.
    '''
    # The code below is to get you started. Feel free to modify.
    print("example2")
    for n in [500, 750, 1000, 1500, 2000, 10000, 50000, 100000, 500000, 1000000, 10000000]:
        sequence = generate_sequence(n)
        start_time = timeit.default_timer()
        example1(sequence)
        end_time = timeit.default_timer()
        time_elapsed = end_time - start_time
        print(str(n) + ": " + str(time_elapsed) + " seconds")


def time_example3():
    '''
    Time example3 when called on random lists of increasing lengths,
    and print the results.
    '''
    # The code below is to get you started. Feel free to modify.
    print("example3")
    for n in [500, 750, 1000, 1500, 2000, 10000, 50000, 100000, 500000, 1000000, 10000000]:
        sequence = generate_sequence(n)
        start_time = timeit.default_timer()
        example1(sequence)
        end_time = timeit.default_timer()
        time_elapsed = end_time - start_time
        print(str(n) + ": " + str(time_elapsed) + " seconds")


def time_example4():
    '''
    Time example4 when called on random lists of increasing lengths,
    and print the results.
    '''
    # The code below is to get you started. Feel free to modify.
    print("example4")
    for n in [500, 750, 1000, 1500, 2000, 10000, 50000, 100000, 500000, 1000000, 10000000]:
        sequence = generate_sequence(n)
        start_time = timeit.default_timer()
        example1(sequence)
        end_time = timeit.default_timer()
        time_elapsed = end_time - start_time
        print(str(n) + ": " + str(time_elapsed) + " seconds")

#500, 750, 1000, 1500, 2000, 10000, 50000, 100000, 500000, 1000000, 10000000]:
        sequence = generate_sequence(n)
def time_example5():
    '''
    Time example5 when called on random lists of increasing lengths,
    and print the results.
    '''
    # The code below is to get you started. Feel free to modify.
    print("example5")
    for n in [500, 750, 1000, 1500, 2000, 10000, 50000, 100000, 500000, 1000000, 10000000]:
        sequence = generate_sequence(n)
        start_time = timeit.default_timer()
        example1(sequence)
        end_time = timeit.default_timer()
        time_elapsed = end_time - start_time
        print(str(n) + ": " + str(time_elapsed) + " seconds")


def generate_sequence(n):
    '''Generate a list of n random integers, each in the range of 0 to 10*n'''
    sequence = []
    for num in range(n):
        sequence.append((random.randint(0,9)))
    return sequence


main()
