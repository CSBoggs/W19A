def divide(num1, num2):
    try:
        quotient = num1 / num2
    except ZeroDivisionError:
        print("Do not divide by zero, please try again")
    else:
        print("The product is: ", quotient)