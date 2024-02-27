class MinBinHeap:#define class
    def __init__(self):
        self.heapList = [0] #set to zero
        self.currentSize = 0

    def add_up(self,i): #add up one node
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]: #check incase of swapping
             temp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = temp #swap here
          i = i // 2

    def add_down(self,i): #add down one node
      while (i * 2) <= self.currentSize:
          minC = self.min_child(i) #get index of min child
          if self.heapList[i] > self.heapList[minC]: #if greater than min child
              temp = self.heapList[i]
              self.heapList[i] = self.heapList[minC]
              self.heapList[minC] = temp #swap 
          i = minC

    def insert(self,k):
      self.heapList.append(k) #first in last out
      self.currentSize = self.currentSize + 1 #size updated here
      self.add_up(self.currentSize) #add up if smaller than parent

    def min_child(self,i): #smallest index returned here
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self): #deletes min and returns 
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize] #root equals last part of tree
      self.currentSize = self.currentSize - 1 #update size 
      self.heapList.pop() 
      self.add_down(1) #swaps root when larger than the child
      return retval

    def buildHeap(self,alist): 
      i = len(alist) // 2 #use for level in tree/s
      self.currentSize = len(alist) #update the current size
      self.heapList = [0] + alist #changes/replaces the list here
      while (i > 0): #brings root down when larger than child nodes
          self.add_down(i)
          i = i - 1

    def Get_List(self): #return the array
        return self.heapList[1:]


randomList = [12,40,6,13,17,29,28,2,8]

problem_1 = MinBinHeap()

for x in randomList:
    problem_1.insert(x)

print("Answer for problem 1:")
print(problem_1.Get_List())
print()



problem_2 = MinBinHeap()

problem_2.buildHeap(randomList)

print("Answer for problem 2:")
print(problem_2.Get_List()) 