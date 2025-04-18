# Write a Python program to create a class representing a queue data structure. Include methods
# for enqueueing and dequeuing elements.

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,data):
        newNode = node(data)
        if(self.front == self.rear == None):
            self.front = self.rear =newNode
        else:
            self.rear = newNode
            newNode.next = self.rear
    def dequeue(self):
        if(self.rear == None):
            print("Queue is empty")
            return
        else:
            temp = self.rear
            num = temp.data
            self.rear = temp.next
            temp = None
            return num



q1 = Queue()
q1.enqueue(1)
print(q1.dequeue())
q1.dequeue()
    

        
                