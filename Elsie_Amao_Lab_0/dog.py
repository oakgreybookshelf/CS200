'''
Name: Elsie Amao
Date: 8/28/25
Class-section: CS-200-01
Assignment: Lab 0

File: dog.py
'''

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_breed(self):
        return self.breed
    

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age
    
    def set_breed(self, breed):
        self.breed = breed
    
    def __str__(self):
        return "The dog named " + str(self.name) + " is a " + str(self.breed) + ", and is " + str(self.age) + " years old."