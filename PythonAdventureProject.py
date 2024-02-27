import random
enemy_name_list = ["Mr.Meeseeks", "Scary Terry", "An Elvis Impersonator", "King Jellybean"]
enemy_intro_list = ["I'm Mr. Meeseeks, Look at me!", "Better Run!", "I'm the King!", "Attack!"]

# Define your Adventurer class
class Adventurer:
    
    def __init__(self, name, position, Schmeckels, health_points,adventurerdmg):
        self.name = name
        self.position = 0
        self.Schmeckels = Schmeckels
        self.health_points = health_points
        self.adventurerdmg = adventurerdmg
    
    def __str__(self):
        Stat1 = "---------------------------------------------------------------\n"
        Stat1 += "Adventurer : " + self.name + "\n"
        Stat1 += "Position : " + str(self.position) + "\n"
        Stat1 += "Schmeckels : " + str(self.Schmeckels) + "\n"
        Stat1 += "Health Points : " + str(self.health_points) + "\n"
        Stat1 += "Adventurerdmg: " + str(self.adventurerdmg) + "\n"
        Stat1 += "---------------------------------------------------------------\n"
        return Stat1

# Defining an Enemy class
class Enemy:
    
    def __init__(self, name, position, introduction, damage,enemyhealth):
        self.name = name
        self.position = position
        self.introduction = introduction
        self.damage = damage
        self.enemyhealth = enemyhealth
    def __str__(self):
        Stat2 = "---------------------------------------------------------------\n"
        Stat2 += "Enemy : " + self.name + "\n"
        Stat2 += "Position : " + str(self.position)
        Stat2 += "Introduction : " + str(self.introduction) + "\n"
        Stat2 += "Damage : " + str(self.damage) + "\n"
        Stat2 += "Enemyhealth : " + str(self.enemyhealth) + "\n"
        Stat2 += "---------------------------------------------------------------\n"
        return Stat2

#Start the main loop for game
    
def play(adventurer, enemies, path_length):
    print("Start!")
    for x in range(1, path_length+1): 
        input("\nPress Enter to move forward.\n")
        adventurer.position = x #position on board
        print(adventurer.name + " is at " + str(adventurer.position))
        for enemy in enemies:
            #if enemy is on adventurer position
            if adventurer.position == enemy.position: 
                adventurer.health_points -= enemy.damage # it causes damage to the adventurer
                enemy.health -= adventurer.adventurerdmg #adventurer damages enemy
                print("Attacked" + enemy.name + " and it lost " + str(adventurer.adventurerdmg ) + " health")
                print("Got attacked by " + enemy.name + " and lost " + str(enemy.damage) + " health")
                break
        else: # execute if no enemy is on current space
            pickup = random.randint(10, 50)
            adventurer.Schmeckels += pickup
            print("Recieved " + str(pickup) + " Schmeckels")
        #if adventurer dies
        if adventurer.health_points <= 0: 
            print("\n\n" + adventurer.name + " lost")
            break
    else:
        print("\nYou Did It, Congrats! " + adventurer.name + " won!")


def main():
    path_length = 10
    adventurer = ("Rick Sanchez",0,150)
    
     
    num_enemies = random.randint(int(0.5*path_length), int(0.7*path_length)) 
    enemies = []
    for _ in range(num_enemies):
        enemy_name, enemy_intro = random.choice(enemy_name_list) , random.choice(enemy_intro_list)
        enemy_position, enemy_damage = random.randint(1, path_length), random.randint(15, 40)
        enemyhealth = random.randint(500,1000)
        enemies.append(Enemy(enemy_name, enemy_position, "It's " + enemy_name + enemy_intro, enemy_damage,enemyhealth))
    play(adventurer, enemies, path_length) 
    print("\n\nAt the end of the game:") 
    print(adventurer)

if __name__ == "__main__":
    main()
