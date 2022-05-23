'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''

num = int(input("How many times do you want to say Hunter: "))
amount = 1
while amount <= num:
  print("Hunter")
  amount += 1

#DONE