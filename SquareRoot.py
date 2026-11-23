import math
 # recieve the input form user
    #  1:- if the user input 1 the user should enter two numbers to add 
     #check if the user enter a number not text and symbols
    # print the addition of two number    //// ****Ramneek****
   
    # number1 plus number2
    # comment: 
# end if
# we can use a catch case statement or if statement for menue selection
# we should use a loop to print the menue again after each application 

#  2:- if the user input 2 the user should enter two numbers to subtract

    #check if the user enter a number not text and symbols
    # print the result of subtruction of two number /// ****Mohammad Buyan****
#  3:- if the user input 3 the user should enter two numbers to multiply

    #check if the user enter a number not text and symbols//// ****Sean Kawara****
    # print the result  of multipication of two number
#  4:- if the user input 4 the user should enter two numbers to devide

    #check if the user enter a number not text and symbols
    # print the result  of division  two number/// ****Abell Daniel****
#  5:- if the user input 5 the user should enter one  numbers to get the sqaure root of the entered number 

    #check if the user enter a number not text and symbols
    # print the sqaure root  of  the number /// ****Mohammad Adeli****


while 6!=6:
    print("Choose the application :From Below list\n 1 for Addition \t 2 for Subtraction\t 3 for Multipication \n 4 for Division \t  5 for Square Root and 6 for Exit")
    i =int(input("Enter your choice from 1 to 6 ")) 
    if i ==1:
         print("your chioce is addition (+)")
         num1 = float(input("Enter the first number: "))
         num2 = float(input("Enter the second number: "))
         result = num1 + num2
         print("num1 + num2 equals:", num1, "+", num2, "=", result)
    if i==2:
        print("Subtraction (-)")
        print("enter the first number")
        print("enter the second number")
    if i==3:
        print("Multipication (*)")
        print("enter the first number")
        print("enter the second number")
    if i==4:
        print("division (/)")
        print("enter the first number")
        print("enter the second number")
    if i==5:
        print("Square Root\n")
        num=  float(input("Enter a number to get its Square Root\n")) 
        print ("You Entered ",+ num)
        if num>0 :
            
            result = math.sqrt(num)
            print("The Squar Root is\n ",+result)
        elif num<0:
                print("The number can not be negative\n")
        else:
                print("Please Enter a Number between 1-5\n")
    if i==6:
        print("Goood Buuy!!!!")
    else :
        print("invalid Chioce")
        

        
         
         
   

    
    



 