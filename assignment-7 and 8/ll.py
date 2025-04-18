#LinkedList in python using classes and objects
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode = node(data)
        newNode.data = data
        newNode.next = self.head
        self.head = newNode

    def delete(self,key):
        if self.head == None:
            print("Empty linked list")
            return
        else:
            temp = self.head
            prev = None
            while(temp != None and temp.data != key):
                prev = temp
                temp = temp.next
            if temp.data == key and prev == None:
                self.head = temp.next
            elif temp.data == key and prev != None:
                prev.next = temp.next
            elif temp == None:
                print("Match not found")


                
                


    def display(self):
        temp = self.head
        while(temp!= None):
            print(temp.data,end="->")
            temp = temp.next
        

Ll = Linkedlist()
for i in range(1,11):
    Ll.insert(i)

Ll.delete(9)
Ll.display()        