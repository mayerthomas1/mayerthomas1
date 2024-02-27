class Node:
      
    def __init__(self, data):
        self.data = data
        self.next = None
  
class Queue:
      
    def __init__(self):
        self.front = self.rear = None
  
    def is_Empty(self):
        return self.front == None
      
    def EnQueuing(self, letter):
        alpha = Node(letter)
          
        if self.rear == None:
            self.front = self.rear = alpha
            return
        self.rear.next = alpha
        self.rear = alpha
  
if __name__== '__main__':
    q = Queue()
    q.EnQueuing('a')
    q.EnQueuing('b')
    q.EnQueuing('c')
    q.EnQueuing('d')
    q.EnQueuing('e') 
    q.EnQueuing('f')
    q.EnQueuing('g')
    q.EnQueuing('h')
    q.EnQueuing('i')
    q.EnQueuing('j')   
    
    print("Queue Front : " + str(q.front.data))
    print("Queue Rear : " + str(q.rear.data))