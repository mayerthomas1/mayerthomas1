#create classes
class Node:
      
    def __init__(self, data):
        self.data = data
        self.next = None
  
class Deque:
      
    def __init__(self):
        self.front = self.rear = None
#check if_empty  
    def is_Empty(self):
        return self.front == None
#deine node as alpha for letter in string
#deine addfront to deque
    def addFront(self, letter):
        alpha = Node(letter)
          
        if self.rear == None:
            self.front = self.rear = alpha
            return
        self.rear.next = alpha
        self.rear = alpha
#define addrear to deque     
    def addRear(self, letter):
        alpha = Node(letter)
          
        if self.rear == None:
            self.front = self.rear = alpha
            return
        self.rear.next = alpha
        self.rear = alpha   
#set d to deque and add to nodes  
if __name__== '__main__':
    d = Deque()
    d.addFront('a')
    d.addFront('b')
    d.addFront('c')
    d.addRear('q')
       
#print results   
    print("Deque Front : " + str(d.front.data))
    print("Deque Rear : " + str(d.rear.data))