import random
import sys

# a = int(input("Enter Number "))
# x = 0
#
# if str.isdigit(a):
#     x = a
# else:
#     print("Not a valid number")
#     sys.exit()


#
# while x != y:
#     print(x)
#     x = random.randint(0, 100)
#
# print("You found {0}.  Congrats.".format(y))
# loop = 1
# while loop < 100:
#     x = random.randint(0, 100)
#     print ("Your random  number is:", x)
#     input("Press any key to continue")
#     loop = loop + 1

y = random.randint(1, 100)

while True:
    x = input("Enter Number ")
    if str.isdigit(x):
        if x > y:
            print(f'{x}' " is greater than " + f'{y}')
        elif x < y:
            print(f'{x}' " is less than " + f'{y}')
        else:
            print(f'{x}' " is equal to " + f'{y}')
            sys.exit()
    else:
        print("Not a valid number")
        sys.exit()