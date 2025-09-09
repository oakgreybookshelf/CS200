'''
Author: YOUR NAME
Assignment: Analysis Lab
Filename: main.py
Course: CSIT 200
'''

import timeit
from functions import (
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
    # Add calls to time_example2(), time_example3(), etc.
    # Define these functions below the definition of time_example1().


def time_example1():
    '''
    Time example1 when called on random lists of increasing lengths,
    and print the results.
    '''
    # The code below is to get you started. Feel free to modify.
    print("example1")
    for n in [500, 750, 1000, 1500, 2000]:
        sequence = generate_sequence(n)
        start_time = timeit.default_timer()
        example1(sequence)
        end_time = timeit.default_timer()
        time_elapsed = end_time - start_time
        print(str(n) + ": " + str(time_elapsed) + " seconds")


def generate_sequence(n):
    '''Generate a list of n random integers, each in the range of 0 to 10*n'''
    sequence = []
    # Complete the implementation.
    return sequence


main()
