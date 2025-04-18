# Write a Python program to create a class representing a linked list data structure. Include
# methods for displaying linked list data, inserting and deleting nodes.

class node:
    def __init__(self,data,next):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = node(data,None)
        new_node.data = data
        new_node.next = self.head
        self.head = new_node

    def delete(self,key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.key != None:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")


Llist = LinkedList()
for i in range(1,11):
    Llist.insert(i)

Llist.display()



                





    

        


    
        