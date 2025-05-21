#This is my first fully solo project. Super simple but is a good baby step
#A super basic calculator. Nothing special lol

#This is the introduction. Just something extra. I used time.sleep so its not overwhelming while running
import math 
import time
print('This is a basic calculator made by: NobleSparky')
time.sleep(2)
print('Starting the program')
time.sleep(3)
print('Please do not use capital letters. Still working on it')
time.sleep(2)
print("Type a math procedure. \nObtions are: \nadd \nsubtract \ndivide \nmultiply \nround \nexit")

#This is the command type system to do basic math operations
while True:
    start_math_procedure = input('Enter text >> ')
    if start_math_procedure == 'add':
        num1 = float(input('Enter your first number >> '))
        num2 = float(input('Enter your second number >> '))
        sum_result = num1 + num2
        print('The sum is: ', sum_result)
    elif start_math_procedure == 'subtract':
        num1 = float(input('Enter your first number >> '))
        num2 = float(input('Enter your second number >> '))
        difference_result = num1 - num2
        print('The difference is: ', difference_result)
    elif start_math_procedure == 'divide':
        num1 = float(input('Enter your first number >> '))
        num2 = float(input('Enter your second number >> '))
        quotient_result = num1 / num2
        print('The quotient is: ', quotient_result)
    elif start_math_procedure == 'multiply':
        num1 = float(input('Enter your first number >> '))
        num2 = float(input('Enter your second number >> '))
        product_result = num1 * num2
        print('The product is: ', product_result)
    elif start_math_procedure == 'round':
        num = float(input('Enter a number >> '))
        print('When rounding. Each negitive value represents a place \nSo -1 is tens, and etc. . .')
        round_to = int(input('Enter a number >> '))
        print(round(num, round_to))
    elif start_math_procedure == 'exit':
        print('Exiting program. . .')
        break
    else:
        print('Please enter a vaild operation')
        