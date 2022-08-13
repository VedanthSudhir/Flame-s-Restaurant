


print("Welcome to the Ved's Online Restaurant")
name = input("What is your name?\n")

print("Hello " + name + ", Thank You for coming!")

########################################################################################

print("""Here is the menu :\n
0) Chicken Burger - Rs 40\n
1) Chicken Pizza   - Rs 60\n
2) Egg Sandwich   - Rs 30\n
3) Fried Chicken  - Rs 50\n
4) Veg Burger     - Rs 30\n""")

B = 40
P = 60
ES = 30
FS = 50
VB = 30
Food = [B,P,ES,FS,VB]


order = input("what would you like to order?\n*Write the number of order, \n\033[1m NUMBER ONlY\033\n->")

#########################################################################################

print("\n\033[1m ORDER TAKEN.\033[0m \n\nWould you like to buy any drinks?\n")

order = int(order)



print("we have a large variety of cool drinks:\n")


Order = input("""0) Mountain Dew - 20 Rs\n
0) 7 Up          - 20 Rs\n
1) CocaCola      - 25 Rs\n
2) Coffee        - 25 Rs\n
3) Tea           - 25 Rs\n
4) Lemon Nanari  - 30 Rs\n
*Pl type the number of the drink*\n\n->""")


###########################################################################


print("\n\033[1m ORDER TAKEN.\033")
Order = int(Order)
MD = 20
UP = 20
CC = 25
CF = 25
TE = 25
LN = 30
Drinks = [MD,UP,CC,CF,TE,LN]



print("Total Bill = " + str(Food[order]) + " + " + str(Drinks[Order]))

Total = Food[order] + Drinks[Order]
print("The value the bill is: Rs " + str(Total)) 

import time
time.sleep(2.5)

print("\n\nThank You for coming " + name + ", \nwe would like to see you again!")
