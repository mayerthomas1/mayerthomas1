#define the sort method
def bubbleSort(array):
#set length of array to variable    
    x = len(array)
  
    # Move through array 
    for i in range(x):
  
        for y in range(0, x-i-1):
  
            # from 0 to x-i-1 range
            # the Swap if >
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
  
array = [2, 1, 3, 4, 6, 5, 7, 8, 9, 10]

bubbleSort(array)
#print statement  
print("Bubble sorted array:")
#for range length in array print end= so newline is not used for each value
for i in range(len(array)):
    print(array[i], end=" ")