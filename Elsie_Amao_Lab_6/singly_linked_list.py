class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, new_data):
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data
        return new_data

    def insert_at_end(self, new_data):
        new_data = Node(new_data)
        if self.head is None:
            return new_data
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_data

        return self.head

    def delete(self, data):
        self.data = None
        self.next = None # use loop to find firs toccurence of element and delete one element 
        # use head node as starting point of list, check if head node is none and otherwise run code, maybe tail node
        # two classes, one for node crearion with init, then single linked class has head node
        # set self.head to next node after deletion
        """
        data = Node(data)
        current = self.head
        while current:
            if current.data == data:
                self.head = data.next
                del data
            current = current.next
        """
        if self is None or self.next is None:
            return False
        next_data = data.next
        data.next = next_data.next
        del data

    def search(self, element):
        #element = Node(element)
        current = self.head
        true = "false"
        while current:
            if current.data == element:
                true = "true"
            current = current.next
        if true == "true":
            return True
        else:
            return False

    def display(self):
        display = []
        current = self.head
        while current:
            display.append(current.data)
            current = current. next
        return display

    def reverse_display(self):
        display = []
        current = self.head
        while current:
            display.append(current.data)
            current = current. next

        i = len(display) - 1
        reverse = []
        while i >= 0:
            reverse.append(display[i])
            i -= 1
        return reverse