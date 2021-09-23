import addition as addmod
import subtraction as submod
import multiplication as multmod
import division as divmodu
import sys
class SelectionInputError(Exception):
    pass

def calc_loop():

    print("Welcome to a simple python calculator, please select from the following options:")
    print("1.   Addition")
    print("2.   Subtraction")
    print("3.   Multiplication")
    print("4.   Division")
    print()

    operation_selection = 0
    operation_selection = int(input("Please select by entering the number of the operation: "))
    if (operation_selection <1 or operation_selection > 4):
        calc_loop()
        raise SelectionInputError("Invalid operation selection, please try again")
    else:
        print("Please enter your operation selection")

    try:
        num1 = int(input("Please enter your 1st number: "))
    except ValueError:
        print("Please enter a valid integer")

    try:      
        num2 = int(input("Please enter your 2nd number: "))
    except ValueError:
        print("Please enter a valid integer")

    if operation_selection == 1:
        addmod.addition(num1, num2)
    elif operation_selection ==2:
        submod.subtraction(num1, num2)
    elif operation_selection ==3:
        multmod.multiply(num1, num2)
    elif operation_selection ==4:
        divmodu.divide(num1, num2)

    restart = input("Would you like to restart? Y/n")
    if (restart == "Y" or restart == "y"):
        calc_loop()
    else:
        sys.exit("Goodbye!")

calc_loop()