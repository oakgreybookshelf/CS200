'''
Nov 6, 2025
CSIT 200 
Elsie Amao

TODO
1. add task
2. get highest priority task
3. check if list is empty
4. exit
enter your choice: 1
enter task desription:
enter task priority (1 is highest): 
Task added

'''
class PQ:
    def __init__(self, tasklist=[]):
        self.tasklist = tasklist

    def add_task(self, task, priority):
        task = [task, priority]
        self.tasklist.append(task)

    def highest(self):
        max = [0,5]
        if self.tasklist == []:
            return("None")
        else:
            for i in self.tasklist:
                if int(i[1]) < int(max[1]):
                    max = i
            return(max[0])

    def empty(self):
        if self.tasklist == []:
            print("Empty")
        else:
            print("Not empty")

PQ = PQ()

Y="Y"
while Y == "Y":

    print("Options:")
    print("1. Add Task")
    print("2. Get Highest Priority Task")
    print("3. Check if List is Empty")
    print("4. Exit")
    response = input("Enter your choice: ")

    if response == '1':
        name = input("Enter task description: ")
        priority = input("Enter task priority (1 is highest): ")
        PQ.add_task(name, priority)
        print("Task added!")
    elif response == '2':
        print("The highest priortiy task is:", PQ.highest())
    elif response == '3':
        PQ.empty()
    elif response == '4':
        print("Done!")
        exit
    else:
        print("Please enter a number between 1 and 4")

    Y = input("Enter Y to continue: ")

'''
PQ = PQ()
print("Test if Empty")
if PQ.empty() == True:
    print("Test passed")
else:
    print("Test failed")
print()


print("Test Add Task")
PQ.add_task("Laundry", 2)
if PQ.highest() == "Laundry":
    print("Test passed")
else:
    print("Test failed")
print()


print("Test Highest Priority")
PQ.add_task("Homework", 1)
if PQ.highest() == "Homework":
    print("Test passed")
else:
    print("Test failed")
print()
'''