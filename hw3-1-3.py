# Author: MOG 9/28/21

number = input("What is your number? ")

if int(number) % 2 == 0:
    print(number + " is divisible by 2")
if int(number) % 3 == 0:
    print(number + " is divisible by 3")
if int(number) % 5 == 0:
    print(number + " is divisible by 5")