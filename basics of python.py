# Function definitions for operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == '+':
    print(add(num1, num2))
elif operation == '-':
    print(subtract(num1, num2))
else:
    print("Invalid input")

