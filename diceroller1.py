import random
target = int(input("Enter the target sum to roll for: "))
die_1 = random.randint(1,6)
die2 = random.randint(1,6)
print("Roll: " + str(die_1) + " and " + str(die2) + ", sum is " + str(die_1 + die2))
count = 1
while(die_1 + die2 != target):
   die_1 = random.randint(1,6)
   die2 = random.randint(1,6)    
   print("Roll: " + str(die_1) + " and " + str(die2) + ", sum is " + str(die_1 + die2))
   count += 1
print("Got it in " + str(count) + " rolls!")