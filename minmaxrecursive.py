import random
#start this program the same as the other one by returning none if the list is empty
def recursive_min(list_1):
    if len(list_1)== 0:return list_1
    if len(list_1)==1: return list_1[0]
    remain = list_1[1:]  # store values in a seperate list
    first = list_1[0] #start index value at zero
    min_remain = recursive_min(remain)  # calling recursively the function/ stacking 
    if first < min_remain:#if/else loop to find smallest value 
        return first
    else:
        return min_remain
#will repeat this function to find max value below
def recursive_maximum(list_1):
    if len(list_1) == 0:return list_1
    if len(list_1)==1: return list_1[0]
    remain = list_1[1:]  # store values in a seperate list
    first = list_1[0] #start index value at zero
    max_remain = recursive_maximum(remain)  # calling recursively the function 
    if first > max_remain:#if/else loop to find largest value 
        return first
    else:
        return max_remain
    
def mainfunc():
    list_1 = [random.randint(1,25) for x in range (5)]
    print("The Minimum value is {}".format(recursive_min(list_1)))
    print("The Maximum value is {}".format(recursive_maximum(list_1)))
mainfunc()