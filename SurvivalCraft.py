import random
import time
import os

os.system("clear")
print("=====")
name = raw_input("Name: ")

#basic status
health = 100
day = 1
enemyatk = 20
playeratk = 20
maxhealth = 100
food = 0

#inventory
flint = 0
stick = 0
bark = 0
vine = 0
leather = 0
food = 0

#equipment
sword = False
shield = False
bag = False
wolf = False


def main():
  global health
  if (health == 0):
    end()
  else:
    os.system("clear")
    status()
    print("-----")
    action()
    option = raw_input(name + "> ")
    if ((option == "hunt") or (option == "h")):
      hunt()
    if ((option == "wait") or (option == "w")):
      wait()
    if ((option == "eat") or (option == "e")):
      eat()
    if ((option == "craft") or (option == "c")):
      craft()
    if ((option == "explore") or (option == "x")):
      explore()
    if ((option == "equipment") or (option == "q")):
      equ()
    if ((option == "inventory") or (option == "i")):
      inv()
    if ((option == "eat") or (option == "e")):
      eat()

def action():
  print("-hunt (h)")
  print("-wait (w)")
  print("-eat (e)")
  print("-explore (x)")
  print("-craft (c)")
  print("-equipment (q)")
  print("-inventory (i)")
  print("")

def explore():
  global wolf,flint,stick,bark,vine,health,day,playeratk
  chance = random.randint(1,20)
  if (1 <= chance <= 5):
    print("you found nothing...")
  if (6 <=  chance <= 8):
    print("you found a Vine!")
    vine += 1
  if (9 <= chance <= 11):
    print("you found a stick!")
    stick += 1
  if (12 <= chance <= 14):
    print("you found a Oak Bark!")
    bark += 1
  if (15 <= chance <= 17):
    print("you found a flint!")
    flint += 1
  if (18 <= chance <= 20):
    if (wolf == False):     
      print("You find a pup wolf")
      time.sleep(1)
      print("it followed you home")
      time.sleep(1)
      print("you keep it")
      wolf = True
      playeratk += 10
    else:
      print("You find a pup wolf")
      time.sleep(1)
      print("it ran away")
      time.sleep(1)
  print("Your Luck is : " + str(chance) )
  time.sleep(1)
  day += 1
  health -= 10
  main()



def status():
  print("=====")
  print("Name : " + name)
  print("Health : " + str(health))
  print("Food : " + str(food))
  print("Day : " + str(day))
  print("")


def hunt():
  global day, health, food,enemyatk,playeratk,leather
  num = random.randint(1, 10)
  enemy = random.randint(1, 10)
  if (wolf == True):
    num += 1
  if (sword == True):
    num += 1
  if (shield == True):
    enemy -= 1
  if (num >= 10):
    num = 10
  print("Your Luck : " + str(num) )
  print("Enemy Luck : " + str(enemy) )
  print("___________")
  if (num > enemy):
      food += playeratk
      if (8 <= num <= 10):
        print("you found a leather!")
        leather += 1
      print("Success hunt, food + " + str(playeratk))
      time.sleep(2)
  else:
      health -= enemyatk
      print("Failed hunt, food - " + str(enemyatk))
      time.sleep(2)
  day += 1
  main()


def wait():
  global day, health
  health -= 5
  day += 1
  main()

def craft():
  global stick,flint,bark,vine,sword,shield,bag,day,playeratk,enemyatk,maxhealth
  print("-----")
  print("flint : " + str(flint))
  print("stick : " + str(stick))
  print("bark : " + str(bark))
  print("vine : " + str(vine))
  print("food : " + str(food))
  print("")
  print("-----")
  print("Recepies :")
  print("Sword = 1 Stick + 2 flint")
  print("Shield = 3 Oak Bark + 2 vines")
  print("Bag = 2 Leather + 3 vines")
  print("")
  opt = raw_input("What you want to craft? ")
  if (opt == "sword"):
    if (sword == False):
      if ( (stick > 0 ) and (flint > 1) ):
        stick -= 1
        flint -= 2
        sword = True
        playeratk =+ 5
        print("You Craft a Sword!")
        day += 1
      else:
        print("Not enough resources to craft a sword!")
    else:
      print("you already have a sword!")
  if (opt == "shield"):
    if (shield == False):
      if ((bark > 2) and (vine > 1)):
        bark -= 3
        vine -= 2
        shield = True
        enemyatk -= 5
        print("You Craft a shield!")
        day += 1
      else:
        print("Not enough resources to craft a shield!")
    else:
      print("you already have a shield!")
  if (opt == "Bag"):
    if (Bag == False):
      if ((leather > 2) and (vine > 1)):
        leather -= 3
        vine -= 2
        Bag = True
        print("You Craft a Bag!")
        maxhealth += 40
        day += 1
      else:
        print("Not enough resources to craft a Bag!")
    else:
      print("you already have a Bag!")
  print("")
  dummy = raw_input("Press any key to continue!")
  main()

def inv():
  os.system("clear")
  status()
  print("-----")
  print("flint : " + str(flint))
  print("stick : " + str(stick))
  print("bark : " + str(bark))
  print("vine : " + str(vine))
  print("leather : " + str(leather))
  print("food : " + str(food))
  print("")
  dummy = raw_input("press any key to continue")
  main()

def equ():
  os.system("clear")
  status()
  print("-----")
  print("sword : " + str(sword))
  print("shield : " + str(shield))
  print("bag : " + str(bag))
  print("wolf : " + str(wolf))
  print("")
  dummy = raw_input("press any key to continue")
  main()

def eat():
  global food,health,maxhealth
  os.system("clear")
  status()
  eatq = input("how many do you want to eat? ")
  if (eatq > food):
    print("you dont have that many food")
    main()
  else:
    if (health == maxhealth):
      print("You already in full health")
      main()
    else:
      health += eatq
      food -= eatq
      print("you ate " + str(eatq) + " foods")
      main()

def end():
  os.system("clear")
  print("=====")
  print("You Died!")
  print( name +" Survive for " + str(day) + " Days")
  print("")

# Init
main()
