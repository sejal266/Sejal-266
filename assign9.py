# Define functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: Division by zero"

# Operator-function mapping
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Call the function using dictionary
func = operations.get(operator)

if func:
    print("Result:", func(a, b))
else:
    print("Invalid operator")