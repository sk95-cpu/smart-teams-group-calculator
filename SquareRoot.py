import math
print("Choose the application :From Below list\n 1 for Addition \t 2 for Subtraction\t 3 for Multipication \t 4 for Division \t and 5 for Square Root")
# recieve the input form user
# we can use a catch case statement or if statement for menue selection
# we should use a loop to print the menue again after each application 



#  1:- if the user input 1 the user should enter two numbers to add 
    #check if the user enter a number not text and symbols
    # print the addition of two number 
#  2:- if the user input 2 the user should enter two numbers to subtract
    #check if the user enter a number not text and symbols
    # print the result of subtruction of two number
#  3:- if the user input 3 the user should enter two numbers to multiply
    #check if the user enter a number not text and symbols
    # print the result  of multipication of two number
#  4:- if the user input 4 the user should enter two numbers to devide
    #check if the user enter a number not text and symbols
    # print the result  of division  two number
#  5:- if the user input 5 the user should enter one  numbers to get the sqaure root of the entered number 
    #check if the user enter a number not text and symbols
    # print the sqaure root  of  the number
print("You Slect 5 Enter the num to get its Square Root\n")
num=  int(input("Enter a number to get its Square Root\n")) 
print ("You Entered ",+ num)
if num>0 :
    result = math.sqrt(num)
    print("The Squar Root is\n ",+result)
elif num<0:
    print("The number can not be minus\n")
else:
    print("Please Enter a Number\n")

    
    



 