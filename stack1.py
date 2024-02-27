class Node:
      
    # Class to create nodes
    # initialize
    def __init__(self,data):
        self.data = data
        self.next = None
      
class Stack:
    
    def __init__(self):
        self.head = None
    # Check to see if empty
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    # add to stack
    def push(self,data):
          
        if self.head == None:
            self.head = Node(data)
              
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
      
    # Remove element that is the current head (start of the stack)
    def pop(self):
          
        if self.is_empty():
            return None
              
        else:
            # Removes the head node and makes 
            #the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
      
    # Returns the head node data
    def peek(self):
          
        if self.is_empty():
            return None
              
        else:
            return self.head.data
      
    # Prints out the stack     
    def display(self):
          
        iternode = self.head
        if self.is_empty():
            print("Stack Underflow")
          
        else:
              
            while(iternode != None):
                  
                print(iternode.data,"--",end = " ")
                iternode = iternode.next
            return
          
# Driver code
Stack_1 = Stack()
  
Stack_1.push(1) 
Stack_1.push(2)
Stack_1.push(3)
Stack_1.push(4)
  
# Display stack elements 
Stack_1.display()
  
# Print top element of stack 
print("\nTop element is ",Stack_1.peek())
  
# Delete an element in stack
Stack_1.pop()
# Display stack elements
Stack_1.display()
  
# Print top element of stack 
print("\nTop element is ", Stack_1.peek()) 