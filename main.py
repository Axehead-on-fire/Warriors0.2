# [>---<][>-----------------------------------<][>---<] #
# [>---<][>------------ Warriors -------------<][>---<] #
# [>---<][>----------- Version 0.2 -----------<][>---<] #
# [>---<][>-----------------------------------<][>---<] #
# [>---<][>--- Dragon Warrior style 2D RPG ---<][>---<] # 
# [>---<][>------------ Python 3 -------------<][>---<] #
# [>---<][>----------- John Hughes -----------<][>---<] #
# [>---<][>-------- Born on 9/28/2015 --------<][>---<] #
# [>---<][>-----------------------------------<][>---<] #
# [>---<][>---- Last worked on 9/30/2015 -----<][>---<] #
# [>---<][>-----------------------------------<][>---<] #

#
# Organizing everything into classes.
#

import random



class Character(object):
    def __init__(self, name, hp, atk, inv, exp):
        self.name = name #input('What shall I call you?')
        self.hp = hp
        self.atk = atk
        self.inv = inv
        self.exp = exp # This gets transfered from enemy to player
    def set_name(self, name):
        self.name = name
    def get_name(self, name):
        return self.name
    def set_hp(self, hp):
        self.hp = hp
    def get_hp(self, hp):
        return self.hp
    def set_atk(self, atk):
        self.atk = atk
    def get_atk(self, atk):
        return self.atk
    def set_inv(self, inv):
        self.inv = inv
    def get_inv(self, inv):
        return self.inv
    def set_exp(self, exp):
        self.atk = exp
    def get_exp(self, exp):
        return self.exp
    
class Player(Character):
    def __init__(self):
        Character.__init__(self)

class Enemy(Character):
    def __init__(self):
        Character.__init__(self)

def fight(player, enemy):
    global game
    enemy.hp -= player.atk # Player atks enemy
    player.hp -= enemy.atk # Enemy atks player
    if player.hp <= 0:
        print('You died. Try harder.')
        game = False
        
    elif enemy.hp > 0 and player.hp > 0:
        #player.hp -= enemy.atk # Enemy atks player
        print (str(player.name) + " hits " + str(enemy.name) + " " + \
               str(player.atk) + " hitpoints.")
        print (str(enemy.name) + ": " + str(enemy.hp) + " Hitpoints.\n")
        print (str(enemy.name) + " hits " + str(player.name) + " " + \
               str(enemy.atk) + " hitpoints.")
        print (str(player.name) + ": " + str(player.hp) + " Hitpoints.\n")
        
    elif enemy.hp <= 0:
        player.exp += 3 # Change 3 to variable
        #player.inv += enemy.inv # Get enemies loot
        loot = player.inv
        loot.append(enemy.inv) # Get enemies loot
        print (str(player.name) + " hits " + str(enemy.name) + " " + \
               str(player.atk) + " hitpoints.")
        print (str(enemy.name) + ": " + str(enemy.hp) + " Hitpoints.\n")
        print('You gainted 3 exp!') # Change 3 to variable
        print('Your exp now is ' + str(player.exp) + '!')
        print('You looted ' + str(enemy.inv) + ' gold.')
        game = False

    return player.hp, enemy.hp

### Setup user profile
##name = ""
##while not name:
##    name = input("What's your name? ")
##print()
##
# Initialize some random ranges
r_100 = random.randrange(100)
rGold_10 = random.randrange(10)

# Items
gold = [0, 0, 1, 3, 5, 7, 10, 25, 50, random]

# Inventories
userInv  = []
batInv   = [gold[rGold_10]]
wolfInv  = [gold[rGold_10]]
snakeInv = [gold[rGold_10]]
orcInv   = [gold[rGold_10]]
giantInv = [gold[rGold_10]]

# Variables        name     hp  atk       inv    exp
player   = Character("John", 10000, 1000,      [],    0)


bat    = Character( "Bat",   1000,  500,   batInv,  3) 
wolf   = Character( "Wolf",  1500, 1000,  wolfInv,  5)
snake  = Character( "Snake", 1000, 1000, snakeInv,  4)
orc    = Character( "Orc",   2000, 1500,   orcInv, 10)
giant  = Character( "Giant", 4000, 2000, giantInv, 15)



enemyList =  [bat, wolf, snake, orc, giant]

random = random.randrange(len(enemyList)-1)
enemy = enemyList[random]






game = True

while game == True:
    decision = input("\n\n(F)ight \n(I)nventory \n(P)rofile \n(Q)uit\n\n")
    f = "F"
    i = "I"
    p = "P"
    q = "Q"
    
    ### QUIT GAME ###
    if decision == q.lower():
        print ("Goodbye.")
        game = False
        
    ### PROFILE PAGE ###
    elif decision == p.lower():
        print ("\nName = " + player.name + \
               "\nHitpoints = " + str(player.hp) + \
               "\nAttack = " + str(player.atk) + \
               "\nExp = " + str(player.exp) + "\n\n")
           

    ### INVENTORY PAGE ###
    elif decision == i.lower():
        if player.inv:
            print(str(player.inv))
        else:
            print("You don't have any items yet.")
        
    ### FIGHT ###
    elif decision == f.lower():
        fight(player, enemy)




