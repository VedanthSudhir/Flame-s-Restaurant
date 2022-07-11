
from turtle import Vec2D


print("Welcome to the restaurant")
name = input("What is your name?\n")

print("Hello " + name + ", Thank You for coming!")


print("Here is the menu :\n1) Burger - Rs 40\n2) Pizza  - Rs 60\n")

B = 40
P = 60
Food = [B,P]


order = input("what would you like to order?\n->")

print("okay. Here is your " + order + ".\n\nWould you like to buy any drinks?\n")

order = int(order)



print("we have a large variety of cool drinks:\n")

print(P)
Order = input(
    "1) Mountain Dew - 20 Rs\n2) 7 Up  - 20 Rs\n3) CocaCola - 25 Rs\n*Pl type the initials of the drink*\n\n->")

print("okay. here is your " + Order +
      "\n\nNow I would like to make the payment\n")

Order = int(Order)
MD = 20
UP = 20
CC = 25
Drinks = [MD,UP,CC]



print("Total Bill = " + str(Food[order]) + " + " + str(Drinks[Order]))

Total = Food[order] + Drinks[Order]
print("The value the bill is: Rs " + str(Total)) 

import time
time.sleep(2.5)

#print("\n\nThank You for coming " + name + ", \nwe would like to see you again!")
