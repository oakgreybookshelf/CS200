'''
Name: Elsie Amao
Date: 8/28/25
Class-section: CS-200-01
Assignment: Lab 0

File: dog_test.py
'''

import dog

def test_name():
    '''
    Test the name function.
    '''
    dog1 = dog.Dog("Fido", 4, "golden retriever")

    print("Dog 1's name is", dog1.get_name())

    dog1.set_name("Coco")

    print("Dog 1:", dog1.__str__())   


def test_age():
    '''
    Test the age function.
    '''
       
    dog2 = dog.Dog("Chichi", 6, "great pyrenese")

    print("Dog 2's age is", dog2.get_age())

    dog2.set_age(2)

    print("Dog 2:", dog2.__str__())


def test_breed():
    '''
    Test the breed function.
    '''
    dog3 = dog.Dog("Pluto", 9, "beagle")
    
    print("Dog 3's breed is", dog3.get_breed())

    dog3.set_breed("poodle")

    print("Dog 3:", dog3.__str__())  

#OUTPUT
test_name()
test_age()
test_breed()