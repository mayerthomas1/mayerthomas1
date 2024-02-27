#m= missionaries
#c = cannibals
print("\nThe task at hand is to move everyone to the right side of the river")
print("The rules are as follows:\n1. The boat can only hold two passengers at once\n2. If #number of cannibals is greater than the #number of missionaries then the cannibals will feast on the missionaries\n3. The boat is unable to go across the river with no passengers on board")
LeftM = 3            #LeftM = Missionaries on left side of River
LeftC = 3            #LeftC = Cannibals on left side
RightM=0             #RightM = Missionaries on right side of River
RightC=0             #RightC = Cannibals on right side
useRightM = 0        #useRightM = Input for right side to left side (missionaries)
useRightC = 0        #useRightC = Input for right side to left side (cannibals) 
X = 0
print("\nM M M C C C |     --- | \n")
try:
    while(True):
        while(True):
            print("From the Left side ---> to the Right side river travel")
            #UM = user input for number of missionaries for left to right travel
            #UC = user input for  number of cannibals for left to right travel
            uM = int(input("Enter # of Missionaries traveling => "))   
            uC = int(input("Enter # of Cannibals traveling => "))
 
            if((uM==0)and(uC==0)):
                print("Boat cannot cross with no passengers on board")
                print("Enter a correct value : ")
            elif(((uM+uC) <= 2)and((LeftM-uM)>=0)and((LeftC-uC)>=0)):
                break
            else:
                print("Incorrect input, please Re-enter : ")
        LeftM = (LeftM-uM)
        LeftC = (LeftC-uC)
        RightM += uM
        RightC += uC
 
        print("\n")
        for i in range(0,LeftM):
            print("M ",end="")
        for i in range(0,LeftC):
            print("C ",end="")
        print("| --> | ",end="")
        for i in range(0,RightM):
            print("M ",end="")
        for i in range(0,RightC):
            print("C ",end="")
        print("\n")
 
        X +=1
 
        if(((LeftC==3)and (LeftM == 1))or((LeftC==3)and(LeftM==2))or((LeftC==2)and(LeftM==1))or((RightC==3)and (RightM == 1))or((RightC==3)and(RightM==2))or((RightC==2)and(RightM==1))):
            print("Cannibals have eaten the missionaries:\nYou lose!")
 
            break
 
        if((RightM+RightC) == 6):
            print("You have won! : \n\tCongrats")
            
            
            print(X)
            break
        
        while(True):
            print("From the Right side <--- to the Left side river travel")
            useRightM = int(input("Enter the # of Missionaries traveling => "))
            useRightC = int(input("Enter the # of Cannibals traveling => "))
             
            if((useRightM==0)and(useRightC==0)):
                    print("Boat cannot cross with no passengers on board")
                    print("Enter a correct value : ")
            elif(((useRightM+useRightC) <= 2)and((RightM-useRightM)>=0)and((RightC-useRightC)>=0)):
                break
            else:
                print("Incorrect input, please Re-enter : ")
        LeftM += useRightM
        LeftC += useRightC
        RightM -= useRightM
        RightC -= useRightC
 
        X +=1
        print("\n")
        for i in range(0,LeftM):
            print("M ",end="")
        for i in range(0,LeftC):
            print("C ",end="")
        print("| <-- | ",end="")
        for i in range(0,RightM):
            print("M ",end="")
        for i in range(0,RightC):
            print("C ",end="")
        print("\n")
 
     
 
        if(((LeftC==3)and (LeftM == 1))or((LeftC==3)and(LeftM==2))or((LeftC==2)and(LeftM==1))or((RightC==3)and (RightM == 1))or((RightC==3)and(RightM==2))or((RightC==2)and(RightM==1))):
            print("Cannibals eat missionaries:\nYou lost the game")
            break
except EOFError as e:
    print("\nInvalid input please retry !!")