# Author: MOG 9/28/21

card1_value = input("What is the value of your first card? ")
card2_value = input("Second? ")

if int(card1_value) + int(card2_value) <= 21:
    print("you're safe")
else:
    print("You've busted")
