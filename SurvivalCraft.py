import random
import time
import replit

replit.clear()
print("=====")
name = raw_input("Name: ")

#basic status
health = 100
day = 1
enemyatk = 20
food = 0

#inventory
flint = 0
stick = 0
bark = 0
vine = 0
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
    replit.clear()
    status()
    print("-----")
    action()
    option = raw_input(name + "> ")
    if ((option == "hunt") or (option == "h")):
      hunt()
    if ((option == "wait") or (option == "w")):
      wait()
    if ((option == "craft") or (option == "c")):
      craft()
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
  print("-craft (c) [WIP]")
  print("-equipment (q)")
  print("-inventory (i)")
  print("")


def status():
  print("=====")
  print("Name : " + name)
  print("Health : " + str(health))
  print("Food : " + str(food))
  print("Day : " + str(day))
  print("")


def hunt():
  global day, health, food
  num = random.randint(1, 10)
  enemy = random.randint(1, 10)
  if (num > enemy):
      food += enemyatk
      print("Success hunt, food + " + str(enemyatk))
      time.sleep(1)
  else:
      health -= enemyatk
      print("Failed hunt, food - " + str(enemyatk))
      time.sleep(1)
  day += 1
  main()


def wait():
  global day, health
  health -= 5
  day += 1
  main()

def craft():
  inv()
  print("-----")
  print("Recepies :")
  print("Sword = 1 Stick + 2 flint + 1 vines")
  print("Shield = 3 Oak Bark + 2 vines")
  print("Bag = 2 Leather + 3 vines")
  print("")
  dummy = raw_input("press any key to continue")
  main()

def inv():
  replit.clear()
  status()
  print("-----")
  print("flint : " + str(flint))
  print("stick : " + str(stick))
  print("bark : " + str(bark))
  print("vine : " + str(vine))
  print("food : " + str(food))
  print("")
  dummy = raw_input("press any key to continue")
  main()

def equ():
  replit.clear()
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
  global food,health
  replit.clear()
  status()
  eatq = raw_input("how many do you want to eat? ")
  if (eatq > food):
    print("you dont have that many food")
  else:
    if (health == 100):
      print("You already in full health")
    else:
      addhealth = food - eatq
      health += addhealth
      food -= eatq
      print("you ate " + str(addhealth) + " foods")

def end():
  replit.clear()
  print("=====")
  print("You Died!")

# Init
main()
